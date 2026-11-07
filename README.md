# Qz-GTNH

为指定 GTNH 版本提供 Qz 生态的固定版本组合与补充安装包。

| GTNH | Qz-Miner | Qz-UILib | Qz-UILib-Compat | 精确清单 |
| --- | --- | --- | --- | --- |
| 2.9.0-RC-2 | 5.5.0 | 5.0.0-beta4 | 1.0.0-beta2 | [RC2](<combinations/2.9.0-RC-2.json>) |
| 2.9.0 | 5.5.1 | 5.0.0-beta5 | 1.0.0-beta3 | [正式版](<combinations/2.9.0.json>) |

版本表用于说明项目配对。完整安装集合包含 Miner、UILib Minecraft 宿主、Core Java8、字体适配 Java8 和 Compat，全部运行 Jar 一起安装。来源固定到上游 Release，所有下载及缓存均核对 SHA256。

## 安装

1. 从本仓 [Releases](https://github.com/QuanhuZeYu/Qz-GTNH/releases) 下载与当前 GTNH 版本相同的 `qz-gtnh-<GTNH版本>-r<修订>.zip`，按随附 `.sha256` 校验。源码中的组合修订为 `r2`，已发布修订以 Releases 为准。
2. 备份实例，移除旧 Qz-Miner、UILib、Compat 及旧拆分运行件，保留已有配置。
3. 将 ZIP 内容合并到实例的 `.minecraft` 目录；将 `mods/` 内的全部 Jar 一起安装，按随包 `INSTALL.txt` 核对文件；`upstream/` 保留上游说明。
4. 沿用目标 GTNH 的 Java、UniMixins 及其他原有依赖，客户端与服务端安装同一组合。

首批组合依据上游已发布依赖配对；RC2 组合沿用正式版升级前的一组制品。制品校验与打包验证覆盖来源和完整性，目标实例的启动、联机与渲染待实机验证。

## 手动下载与启动排查

手动组装时，从 [UILib Releases](https://github.com/QuanhuZeYu/Qz-UILib/releases) 下载对应版本的 `qz-uilib-minecraft-<版本>-1.7.10.zip`，将其中宿主、Core 和字体适配三个 Jar 一起放入 `mods/`，再加入版本表对应的 Miner 和 Compat。Core 与字体适配文件名中的 `java8` 表示字节码兼容目标，GTNH 的新版 Java 实例也使用这套运行库。

GTNH 2.9.0 的完整集合：

```text
qz_miner-5.5.1.jar
qz_uilib-5.0.0-beta5.jar
qz_uilib-core-java8.jar
qz_uilib-font-adapter-java8.jar
qz_uilib_compat-1.0.0-beta3.jar
```

| 启动报错 | 检查与处理 |
| --- | --- |
| `NoClassDefFoundError: ...FontTextService` | 核对 Core 来自同版本完整 UILib ZIP，且已放入当前实例的 `mods/`。 |
| `ClassNotFoundException: ...Lwjgl3GlApi` | 核对当前实例已安装版本表对应的 Compat；LWJGL3 binding 由 Compat 提供。 |
| 补齐文件后仍有缺类 | 核对当前实例路径与完整组合，附新的完整启动日志，继续定位加载路径。 |

上述两类缺依赖对应 [Qz-Miner#259](https://github.com/QuanhuZeYu/Qz-Miner/issues/259)。打包时检查宿主、Core、字体适配与 Compat 中的关键类，缺失即失败。

## 本地构建

使用 Python 3.12+ 标准库：

```text
python tools/bundle.py check
python tools/bundle.py build
python tools/bundle.py build --target 2.9.0-RC-2
```

输出位于 `build/dist/`：每个目标各有 ZIP、精确 JSON 清单和 SHA256 文件。缓存位于 `build/cache/`。同一环境的固定输入重复构建得到相同 ZIP。

## 发布

每个目标使用独立组合修订，标签格式为 `gtnh-<GTNH版本>-r<修订>`，首批为 `gtnh-2.9.0-RC-2-r1` 与 `gtnh-2.9.0-r1`。上游项目继续独立维护版本与发布。

分支 CI 构建两个组合并保留产物。用户创建并推送对应 annotated tag 后，在 Release 工作流输入目标、标签和 `PUBLISH <tag>`。工作流从标签提交重新构建并发布正式 Release，附清单、安装包、摘要与本次工作流证据。每次组合更新递增修订并使用新标签。

合同见[组合规格](<specs/combinations.md>)。仓库自有代码采用 [MIT](<LICENSE>)，上游与第三方许可随原 Jar 保留。
