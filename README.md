# Qz-GTNH · Qz 系列模组包

给已经装好的 GTNH 安装 Qz 系列模组。模组和需要的文件都放在一个包里，下载后一起安装。

## ① 下载

先看你的 GTNH 版本，再点右边的蓝字。

| 你的游戏版本 | 点这里下载 |
| --- | --- |
| **2.9.0 正式版** | **[下载正式版 Qz 模组包](https://github.com/QuanhuZeYu/Qz-GTNH/releases/download/gtnh-2.9.0-r2/qz-gtnh-2.9.0-r2.zip)** |
| **2.9.0-RC-2 测试版** | **[下载 RC2 测试版 Qz 模组包](https://github.com/QuanhuZeYu/Qz-GTNH/releases/download/gtnh-2.9.0-RC-2-r2/qz-gtnh-2.9.0-RC-2-r2.zip)** |

不知道版本？打开 GTNH，看看主菜单底部的版本号。写着 `2.9.0-RC-2` 就选测试版，写着 `2.9.0` 就选正式版。

**选一个和游戏版本相同的包就够了。包里的文件要全部一起用。**

[只想单独安装或更新 UILib？看搭配教程](#uilib-怎么搭配)。

## ② 安装

先关掉游戏，备份游戏文件夹。

<details>
<summary>以前装过 Qz？复制新文件前先看这里</summary>

先把这次要更新的旧 Qz 文件移到备份文件夹，再复制新文件。当前包对应的旧文件以 `qz_miner` 或 `qz_uilib` 开头，后缀是 `.jar`。其他模组和游戏配置照常保留。

</details>

1. **找到游戏的 `mods` 文件夹。** 在启动器里点“游戏文件夹”或“打开实例文件夹”，再打开 `mods`。找不到？先打开里面的 `.minecraft`，再找 `mods`。
2. **解压刚才下载的包。** 再打开解压出来的 `mods` 文件夹。
3. **把里面的文件全部复制过去。** 放进第 1 步找到的游戏 `mods` 文件夹。
4. **打开游戏。** 还是用原来的启动器启动。

📦 下载 → 📂 解压 → 📋 全部复制到游戏的 `mods` → 🎮 开游戏

## UILib 怎么搭配

UILib 给 Qz 系列模组提供界面、字体等功能。多个 Qz 模组可以共用一套 UILib。

**从上面下载完整 Qz 模组包时，UILib 已经配好了。把包里的文件全部复制过去即可。** 下面教你单独安装、更新 UILib，或检查自己有没有装齐。

### 先选与你的 GTNH 相同的一行

| 你的 GTNH | UILib 完整安装包 | 还要一起安装的 Compat |
| --- | --- | --- |
| **2.9.0 正式版** | [UILib 5.0.0-beta5 · Minecraft 1.7.10](https://github.com/QuanhuZeYu/Qz-UILib/releases/download/5.0.0-beta5/qz-uilib-minecraft-5.0.0-beta5-1.7.10.zip) | [Compat 1.0.0-beta3](https://github.com/QuanhuZeYu/Qz-UILib-Compat/releases/download/1.0.0-beta3/qz_uilib_compat-1.0.0-beta3.jar) |
| **2.9.0-RC-2 测试版** | [UILib 5.0.0-beta4 · Minecraft 1.7.10](https://github.com/QuanhuZeYu/Qz-UILib/releases/download/5.0.0-beta4/qz-uilib-minecraft-5.0.0-beta4-1.7.10.zip) | [Compat 1.0.0-beta2](https://github.com/QuanhuZeYu/Qz-UILib-Compat/releases/download/1.0.0-beta2/qz_uilib_compat-1.0.0-beta2.jar) |

**同一行的 ZIP 和 Compat 要一起下载、一起安装。** Compat 有自己的版本号，照表配套即可。GTNH 使用 Minecraft 1.7.10，下载时认准文件名里的 `1.7.10`。

### 照着做：以 GTNH 2.9.0 正式版为例

1. 下载上表的 **UILib 5.0.0-beta5 ZIP** 和 **Compat 1.0.0-beta3 Jar**。
2. 解压 UILib ZIP。里面的宿主、Core、字体适配库这三个 `.jar` **全部保留**。
3. 从启动器打开游戏文件夹，再打开 `mods`。找不到就先打开 `.minecraft`。
4. 关掉游戏，把原有的旧 UILib、Core、字体适配库和 Compat 移到备份文件夹，再把新文件放进 `mods`。Qz 模组自己的文件照常保留。

装好后，游戏的 `mods` 里应同时有这四个文件：

```text
qz_uilib-5.0.0-beta5.jar
qz_uilib-core-java8.jar
qz_uilib-font-adapter-java8.jar
qz_uilib_compat-1.0.0-beta3.jar
```

**前三个来自同一个 UILib ZIP，最后一个是单独下载的 Compat。四个全部一起用。** 你要玩的 Qz 模组也要装，例如 Qz-Miner；UILib 是它们共用的基础。

RC2 按表格另一行操作：宿主文件是 `qz_uilib-5.0.0-beta4.jar`，Compat 是 `qz_uilib_compat-1.0.0-beta2.jar`；Core 和字体适配库也要从 **beta4 ZIP** 中取。

### Core、Platform、Minecraft、Compat 分别是什么

| 名字 | 做什么 | 你安装时怎么处理 |
| --- | --- | --- |
| **Core** | 提供界面的基础功能 | 用完整 ZIP 里的 `qz_uilib-core-java8.jar`。 |
| **Platform** | 提供字体、绘制等功能 | 当前 1.7.10 ZIP 已把所需部分配好：字体适配库单独提供，部分绘制代码已装进宿主。把 ZIP 内的 Jar 全部一起复制即可。 |
| **Minecraft 宿主** | 把 UILib 接入游戏 | 用完整 ZIP 里的 `qz_uilib-版本.jar`，它还需要同包的 Core 和字体适配库。 |
| **Compat** | 让 UILib 配合 GTNH 里的其他模组工作 | 按上表另装 Compat。当前 GTNH 组合需要它。 |

Core、Platform、Minecraft 按同一个 UILib 版本配套，完整 ZIP 已经把它们组合好。**玩家下载表格中的 Minecraft 完整 ZIP，再加 Compat，就能拿齐当前 GTNH 组合需要的 UILib 文件。**

如果打开上游发布页看见很多附件，按名字区分：

| 附件名字中有 | 是什么，怎么选 |
| --- | --- |
| `minecraft-…-1.7.10.zip` | GTNH 使用的完整 UILib 包，解压后把里面的 Jar 全部安装。 |
| `forge112`、`forge116`、`neoforge263` | 给其他 Minecraft 版本使用的包；GTNH 按上表选 1.7.10。 |
| `maven`、`sources` | 开发用的文件。 |
| `manualtest`、`media` | 测试或媒体附加包，本页当前组合按上表安装即可。 |

### 更新时最容易漏掉的事

- **Core 和字体适配库也要换。** 它们的文件名里没有 beta4、beta5，更新时一起移走旧文件，再从新 ZIP 复制，才能保证整套版本一致。
- **文件名里的 `java8` 也照常安装。** 它表示兼容的 Java 字节码版本，GTNH 使用新版 Java 时同样用这两个文件。
- **多个 Qz 模组共用一套。** 增加模组前看它要求的 UILib 版本，选能共同使用的版本组合；同一个 `mods` 里保留一套对应的 UILib 和 Compat。
- **更新一个组件时，检查整行配套。** 表格中的 UILib 完整包与 Compat 是当前搭配，其他版本按对应发布说明选择。

### 遇到这些报错，先检查对应文件

| 日志里出现 | 先做什么 |
| --- | --- |
| `FontTextService` | 从同版本 UILib ZIP 重新复制 Core。 |
| `NativeFontService` | 从同版本 UILib ZIP 重新复制字体适配库。 |
| `Lwjgl3GlApi` | 按上表补上或更新 Compat。 |

还是打不开时，附上新的完整启动日志[反馈问题](https://github.com/QuanhuZeYu/Qz-GTNH/issues/new)，并写明 GTNH 版本。

## 包里有哪些模组

这里会随 Qz 系列模组的加入而更新。当前包含：

| 模组 | 能做什么 |
| --- | --- |
| [Qz-Miner](https://github.com/QuanhuZeYu/Qz-Miner) | 连锁挖矿 |

模组需要的运行库也在包里，安装时全部一起复制。

<details>
<summary>Qz-Miner：怎么连锁挖矿</summary>

进入存档，拿着镐，**按住 `~` 键，再挖方块**。连着的同类方块会一起挖掉。

按键不顺手？打开“选项 → 控制”，找到 `Qz-Miner` 下的“连锁按键”，就能换按键。

</details>

## 没装上怎么办

先检查：**下载的包已经解压，里面的全部文件都放进了正在玩的游戏的 `mods` 文件夹。**

还是打不开？[点这里反馈问题](https://github.com/QuanhuZeYu/Qz-GTNH/issues/new)，写上 GTNH 版本，并附上启动器导出的完整日志。

<details>
<summary>GitHub 下载页里的其他附件是什么？</summary>

安装包是名字以 `qz-gtnh` 开头的 ZIP。`Source code` 是源码，其他清单和校验文件供维护者使用。首页的下载链接已经选好了完整安装包。

</details>

[开发与打包说明](<specs/combinations.md>) · [许可证](<LICENSE>)
