# Qz-GTNH

为 GTNH 提供配齐依赖的 Qz 模组补充安装包。

## 下载哪个文件

打开本仓 [下载页面（Releases）](https://github.com/QuanhuZeYu/Qz-GTNH/releases)，找到与你的 GTNH 版本一致的发布，在 **Assets（附件）** 中下载下表对应的完整安装包。文件名末尾的 `r数字` 是修订号，选择该 GTNH 版本已发布的最新修订。

| 你正在玩的 GTNH 版本 | 下载这个完整安装包 |
| --- | --- |
| 2.9.0 正式版 | 文件名以 `qz-gtnh-2.9.0-r` 开头、以 `.zip` 结尾 |
| 2.9.0-RC-2 | 文件名以 `qz-gtnh-2.9.0-RC-2-r` 开头、以 `.zip` 结尾 |

**每个完整安装包都已配齐 Miner、UILib、Core、字体适配库和 Compat。下载与你的 GTNH 版本对应的一个完整包即可。**

下载页中的 `Source code (zip)`、`Source code (tar.gz)` 是开发源码；`.json`、`.sha256` 是清单和校验信息。玩家安装使用上表中的 `qz-gtnh-…zip`。

## 怎么安装

1. 关闭游戏，备份当前实例。在启动器中选中该 GTNH 实例，通过“文件夹 / 打开实例文件夹”打开游戏目录，找到里面已有的 `mods` 文件夹。Prism Launcher 可右键实例选择“文件夹”，再进入 `.minecraft`。
2. 从实例的 `mods` 中移出旧 Qz-Miner、Qz-UILib、Qz-UILib-Compat 和旧拆分运行库，保留配置与其他整合包模组。
3. 用文件管理器解压下载的完整安装包，打开解压出来的 `mods` 文件夹。
4. **选中这个文件夹里的全部 Jar，一起复制到游戏实例原有的 `mods` 文件夹中。每个 Jar 都要安装，它们共同组成一套。**
5. 在启动器中照常启动游戏。Java、UniMixins 等沿用 GTNH 实例原有设置。联机时，客户端与服务端使用同一套 Qz 组合。

GTNH 2.9.0 安装完成后，游戏实例的 `mods` 中应同时有以下文件：

```text
mods/
  qz_miner-5.5.1.jar
  qz_uilib-5.0.0-beta5.jar
  qz_uilib-core-java8.jar
  qz_uilib-font-adapter-java8.jar
  qz_uilib_compat-1.0.0-beta3.jar
```

**上面的全部 Jar 都是必需文件，一起放入游戏实例的 `mods` 文件夹。** 其中 `java8` 是库的兼容目标，GTNH 的新版 Java 实例同样安装这两个文件。

## 启动时提示缺少类

| 日志中出现 | 操作 |
| --- | --- |
| `FontTextService` | 检查当前游戏实例的 `mods` 中有 `qz_uilib-core-java8.jar`；从完整安装包重新复制全部 Jar。 |
| `Lwjgl3GlApi` | 检查当前游戏实例的 `mods` 中有对应的 `qz_uilib_compat-…jar`；从完整安装包重新复制全部 Jar。 |
| 文件齐全后仍无法启动 | 在启动器中导出新的完整启动日志，提交到本仓 Issues，并附 GTNH 版本。 |

相关问题：[Qz-Miner#259](https://github.com/QuanhuZeYu/Qz-Miner/issues/259)。安装包已校验来源、文件完整性和关键类；游戏启动、联机与渲染待目标实例实机验证。

<details>
<summary>维护者说明：版本清单、构建与发布</summary>

## 固定版本组合

| GTNH | Qz-Miner | Qz-UILib | Qz-UILib-Compat | 精确清单 |
| --- | --- | --- | --- | --- |
| 2.9.0-RC-2 | 5.5.0 | 5.0.0-beta4 | 1.0.0-beta2 | [RC2](<combinations/2.9.0-RC-2.json>) |
| 2.9.0 | 5.5.1 | 5.0.0-beta5 | 1.0.0-beta3 | [正式版](<combinations/2.9.0.json>) |

源码组合修订为 `r2`，已发布修订以 Releases 为准。来源固定到上游 Release，下载及缓存均核对 SHA256。UILib 使用对应版本的 Forge 1.7.10 完整安装 ZIP，打包时校验宿主、Core、字体适配与 Compat 中的关键类。

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

</details>
