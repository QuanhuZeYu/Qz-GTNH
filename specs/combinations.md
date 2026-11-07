# GTNH 版本组合

Qz-GTNH 为指定 GTNH 版本固定一套已发布 Qz 运行制品，提供补充安装包。业务源码、版本和发布归各上游仓。

## 范围

- 初始目标为 GTNH `2.9.0-RC-2` 与 `2.9.0`，Minecraft `1.7.10`。
- 组合包含 Qz-Miner、Qz-UILib 必需运行件、Qz-UILib-Compat，消费上游公开 Release。
- 采用 Python 3.12+ 标准库完成下载、校验与 ZIP 打包。
- 自有代码采用 MIT；上游及第三方许可随安装包保留。

## 职责

`combinations/<GTNH版本>.json` 决定目标版本、组合修订、项目版本、固定下载地址及 SHA256。UILib 使用其 Forge 1.7.10 完整安装 ZIP 提供运行文件与许可；必需 Jar 显式选择，其他资源和许可保留。

`tools/bundle.py` 校验清单并构建 `build/dist/qz-gtnh-<GTNH版本>-r<修订>.zip`。下载及缓存均核对 SHA256；清单字段、下载失败、摘要不符、归档路径越界或输出冲突使构建失败。ZIP 包含 `mods/`、组合清单、逐文件摘要与安装说明，文件顺序和时间戳固定。

安装包仅补充选定 GTNH 实例。使用者备份实例，移除旧 Qz-Miner、UILib、Compat 及旧拆分运行件后，将内容合并到实例目录；保留整合包的 Java 与 UniMixins 等运行依赖。客户端与服务端使用同一组合。

## 发布

组合修订独立于各项目版本。标签为 `gtnh-<GTNH版本>-r<修订>`，已发布标签及制品保持不变。新增组合修订通过新标签发布。

分支 CI 构建全部组合。发布工作流仅手动触发，输入已有 annotated tag 及 `PUBLISH <tag>`；从标签不可变提交重新校验、打包并创建正式 Release，附完整安装 ZIP、组合清单和 SHA256。push、tag 与 Release 沿工作站授权边界执行。

发布说明面向玩家，用短句写适用版本、完整安装包下载链接和文件复制步骤；明确旧 Qz 文件的处理方法与包内 Jar 全部安装。构建日志保留在 Actions，实机记录独立维护。

## 维护命令

使用 Python 3.12+ 标准库。组合输入见[正式版清单](<../combinations/2.9.0.json>)与 [RC2 清单](<../combinations/2.9.0-RC-2.json>)。

```text
python tools/bundle.py check
python tools/bundle.py build
python tools/bundle.py build --target 2.9.0-RC-2
```

安装包、组合清单和 SHA256 输出到 `build/dist/`；下载缓存放在 `build/cache/`。所有下载及缓存均核对摘要，宿主、Core、字体适配与 Compat 的关键类在打包时校验。

发布时创建并推送对应修订的 annotated tag，再运行 Release 工作流，填写目标、标签及 `PUBLISH <tag>`。上游项目继续独立维护版本与发布。
