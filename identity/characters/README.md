<!--
File: identity/characters/README.md
Purpose: 说明 Zeki 与 Kiki 角色原画、衍生素材和许可管理规则。
Layer: Identity / Character Assets
-->

# Character Assets

本目录保存 Zeki 与 Kiki 的角色原画及其衍生素材。

## 1. 角色清单

| 角色 | 原始文件 | 说明 |
|---|---|---|
| Zeki | `zeki/original/zeki-original.png` | 第一张原画，代表 Zeki |
| Kiki | `kiki/original/kiki-original.png` | 第二张原画，代表 Kiki |

两张原画由 Kiki 创作。原始文件从品牌主在本次 B0 工作中提供的图片直接复制，未裁切、重绘或压缩。

## 2. 目录规则

```text
characters/
├── README.md
├── asset-manifest.yaml
├── zeki/
│   ├── original/
│   │   └── zeki-original.png
│   └── derived/
│       └── README.md
└── kiki/
    ├── original/
    │   └── kiki-original.png
    └── derived/
        └── README.md
```

## 3. 原始素材规则

- `original/` 中的文件是源资产，禁止修改或覆盖。
- 使用原画时应优先直接引用原文件。
- 不允许把裁切、抠图、调色、重绘或压缩后的版本放回 `original/`。
- 新版本进入 `derived/`，并记录原始文件、处理方式、日期、用途和创作者/操作者。
- 不得把“仓库中存在原图”解释为“允许无限制商业使用或第三方授权”。

## 4. 许可与署名

创作者：Kiki。

具体著作权归属、对外传播、商业使用、第三方授权及衍生创作许可范围尚未形成书面约定。涉及上述用途时，先与 Kiki 确认并记录授权范围。
