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
<summary>想核对文件或查看报错？点这里</summary>

GTNH 2.9.0 正式版装好后，游戏的 `mods` 里应有：

```text
qz_miner-5.5.1.jar
qz_uilib-5.0.0-beta5.jar
qz_uilib-core-java8.jar
qz_uilib-font-adapter-java8.jar
qz_uilib_compat-1.0.0-beta3.jar
```

这些文件全部一起用。文件名里有 `java8` 的也要复制。

| 日志中出现 | 检查这个文件是否已经放进游戏的 mods |
| --- | --- |
| `FontTextService` | `qz_uilib-core-java8.jar` |
| `Lwjgl3GlApi` | `qz_uilib_compat-…jar` |

如果去了 GitHub 的下载页，安装包是名字以 `qz-gtnh` 开头的 ZIP。`Source code` 是源码，其他清单和校验文件供维护者使用。上面的蓝色下载链接已经替你选好了安装包。

</details>

[开发与打包说明](<specs/combinations.md>) · [许可证](<LICENSE>)
