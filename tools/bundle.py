"""按已审核组合下载、验证并生成 GTNH 补充安装包。"""

import argparse
import hashlib
import io
import json
import re
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
REPOSITORIES = {"miner": "Qz-Miner", "uilib": "Qz-UILib", "compat": "Qz-UILib-Compat"}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def asset_name(project, version):
    return {
        "miner": f"qz_miner-{version}.jar",
        "uilib": f"qz-uilib-minecraft-{version}-1.7.10.zip",
        "compat": f"qz_uilib_compat-{version}.jar",
    }[project]


def load_combination(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data["schemaVersion"] != 1 or data["minecraft"] != "1.7.10":
        raise ValueError(f"不支持的组合格式：{path.name}")
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+(?:-[A-Za-z0-9.-]+)?", data["gtnh"]) or path.stem != data["gtnh"]:
        raise ValueError(f"GTNH 版本与文件名不一致：{path.name}")
    if type(data["revision"]) is not int or data["revision"] < 1:
        raise ValueError("组合修订必须为正整数")
    artifacts = data["artifacts"]
    if len(artifacts) != len(REPOSITORIES) or {a["project"] for a in artifacts} != set(REPOSITORIES):
        raise ValueError("组合须各包含一份 Miner、UILib、Compat")
    for artifact in artifacts:
        project, version = artifact["project"], artifact["version"]
        if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+(?:-[A-Za-z0-9.-]+)?", version):
            raise ValueError(f"项目须固定精确版本：{project}")
        expected = f"https://github.com/QuanhuZeYu/{REPOSITORIES[project]}/releases/download/{version}/{asset_name(project, version)}"
        if artifact["url"] != expected or artifact["format"] != ("zip" if project == "uilib" else "jar"):
            raise ValueError(f"项目版本、来源或制品格式不一致：{project}")
        if not re.fullmatch(r"[a-f0-9]{64}", artifact["sha256"]):
            raise ValueError(f"SHA256 格式错误：{project}")
    return data


def download(artifact):
    cache = ROOT / "build/cache" / (artifact["sha256"] + "." + artifact["format"])
    if cache.exists():
        content = cache.read_bytes()
    else:
        request = urllib.request.Request(artifact["url"], headers={"User-Agent": "Qz-GTNH"})
        with urllib.request.urlopen(request, timeout=60) as response:
            content = response.read()
    if sha256(content) != artifact["sha256"]:
        raise ValueError(f"制品 SHA256 不符：{artifact["url"]}")
    if not cache.exists():
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_bytes(content)
    return content


def add_file(files, name, content):
    path = PurePosixPath(name)
    if not name or "\\" in name or ":" in name or path.is_absolute() or any(part in ("", ".", "..") for part in name.split("/")):
        raise ValueError(f"归档路径无效：{name}")
    # Windows 实例也须保持路径唯一，避免大小写覆盖。
    if name.casefold() in {key.casefold() for key in files}:
        raise ValueError(f"组合文件冲突：{name}")
    files[name] = content


def install_files(combination):
    files = {}
    for artifact in combination["artifacts"]:
        content = download(artifact)
        if artifact["format"] == "jar":
            with zipfile.ZipFile(io.BytesIO(content)) as jar:
                if jar.testzip() is not None:
                    raise ValueError(f"Jar 内容损坏：{artifact["project"]}")
            add_file(files, "mods/" + asset_name(artifact["project"], artifact["version"]), content)
            continue
        # 复用上游完整安装包；显式约束运行 Jar，许可和其他随包文本一并保留。
        expected_jars = {f"qz_uilib-{artifact["version"]}.jar", "qz_uilib-core-java8.jar", "qz_uilib-font-adapter-java8.jar"}
        with zipfile.ZipFile(io.BytesIO(content)) as archive:
            entries = [entry for entry in archive.infolist() if not entry.is_dir()]
            actual_jars = {entry.filename for entry in entries if entry.filename.lower().endswith(".jar")}
            if actual_jars != expected_jars:
                raise ValueError(f"UILib 必需运行 Jar 不符：{sorted(actual_jars)}")
            for entry in entries:
                destination = ("mods/" if entry.filename in expected_jars else "upstream/uilib/") + entry.filename
                add_file(files, destination, archive.read(entry))
    verify_runtime(files, combination)
    return files


def verify_runtime(files, combination):
    versions = {a["project"]: a["version"] for a in combination["artifacts"]}
    # Qz-Miner#259：主 Mod 齐全仍可能缺 Core，LWJGL3 binding 则由 Compat 提供。
    required = {
        f"qz_uilib-{versions['uilib']}.jar": "club/heiqi/uilib/UILib.class",
        "qz_uilib-core-java8.jar": "club/heiqi/uilib/ui/scene/text/font/FontTextService.class",
        "qz_uilib-font-adapter-java8.jar": "club/heiqi/uilib/host/font/freetype/NativeFontService.class",
        f"qz_uilib_compat-{versions['compat']}.jar": "club/heiqi/uilib/host/client/gl/Lwjgl3GlApi.class",
    }
    for name, class_name in required.items():
        with zipfile.ZipFile(io.BytesIO(files["mods/" + name])) as jar:
            if jar.testzip() is not None:
                raise ValueError(f"运行 Jar 内容损坏：{name}")
            if class_name not in jar.namelist():
                raise ValueError(f"运行依赖缺失：{name} 须包含 {class_name}")


def tag_name(combination):
    return f"gtnh-{combination["gtnh"]}-r{combination["revision"]}"


def build(combination, manifest_path):
    files = install_files(combination)
    add_file(files, "combination.json", manifest_path.read_bytes())
    add_file(files, "LICENSE", (ROOT / "LICENSE").read_bytes())
    instructions = (
        f"Qz-GTNH / GTNH {combination["gtnh"]} / r{combination["revision"]}\n\n"
        "备份对应 GTNH 实例，移除旧 Qz-Miner、UILib、Compat 和旧拆分运行件，保留原配置。\n"
        "将本包内容合并到实例的 .minecraft 目录；mods 内的全部 Jar 一起安装，upstream 保留上游说明。\n"
        "必需运行文件（含独立 Core 与字体适配库）：\n"
        + "".join(f"- {name}\n" for name in sorted(files) if name.startswith("mods/"))
        + "\n"
        "沿用目标 GTNH 整合包的 Java、UniMixins 与其他原有依赖，客户端与服务端使用同一组合。\n"
        "文件摘要见 files.sha256，来源与精确版本见 combination.json。\n"
        "已验证制品来源及打包完整性；目标版本游戏启动、联机和渲染待实机验证。\n"
    )
    add_file(files, "INSTALL.txt", instructions.encode("utf-8"))
    checksums = "".join(f"{sha256(files[name])}  {name}\n" for name in sorted(files))
    add_file(files, "files.sha256", checksums.encode("utf-8"))
    output = ROOT / "build/dist"
    output.mkdir(parents=True, exist_ok=True)
    basename = f"qz-gtnh-{combination["gtnh"]}-r{combination["revision"]}"
    result = output / (basename + ".zip")
    # 固定顺序、权限与时间戳，使同一运行环境的重复构建字节一致。
    with zipfile.ZipFile(result, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, files[name], compresslevel=9)
    lock = output / (basename + ".json")
    lock.write_bytes(manifest_path.read_bytes())
    summary = "".join(f"{sha256(p.read_bytes())}  {p.name}\n" for p in (result, lock))
    (output / (basename + ".sha256")).write_text(summary, encoding="utf-8", newline="\n")
    print(f"构建完成：{result.name}；运行 Jar：{sum(name.startswith("mods/") for name in files)}；SHA256：{sha256(result.read_bytes())}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "build"))
    parser.add_argument("--target", default="all", help="GTNH 版本，默认 all")
    parser.add_argument("--expect-tag", help="发布时核对标签与组合修订一致")
    args = parser.parse_args()
    paths = sorted((ROOT / "combinations").glob("*.json"))
    selected = [p for p in paths if args.target == "all" or p.stem == args.target]
    if not selected or (args.expect_tag and len(selected) != 1):
        parser.error("请选择有效目标；发布标签校验须选择单个目标")
    for path in selected:
        combination = load_combination(path)
        if args.expect_tag and args.expect_tag != tag_name(combination):
            parser.error("标签与组合目标或修订不一致")
        print(f"清单有效：{tag_name(combination)}")
        if args.command == "build":
            build(combination, path)


if __name__ == "__main__":
    main()
