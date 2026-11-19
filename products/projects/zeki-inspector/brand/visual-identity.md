# Zeki Inspector — Visual Identity

<!--
File: zeki-brand/products/zeki-inspector/brand/visual-identity.md
Purpose: 定义品牌色彩、字体、插画、图标、界面视觉语言与主题策略。
Layer: Brand / Visual Identity
Source: Zeki Inspector brand guide board.
-->

## 1. Visual Direction

**Warm Precision / 温和的精确**

视觉语言：

- 温暖；
- 手绘；
- 轻量；
- 清晰；
- 精确；
- 友好；
- 低装饰。

核心视觉不是“AI 科技感”，而是“一个懂开发工具、但不冰冷的检查助手”。

## 2. Color Palette

| Token | Name | Hex | Role |
|---|---|---|---|
| `brand.cream` | Cream / 暖米色 | `#FFF8EB` | Background |
| `brand.ink` | Ink / 墨色 | `#2E2A24` | Text / Linework |
| `brand.mint` | Mint Green / 薄荷绿 | `#7DBA8A` | Primary |
| `brand.blue` | Soft Blue / 柔和蓝 | `#A7C2F3` | Secondary |
| `brand.pink` | Blush Pink / 腮红粉 | `#F8C9CF` | Accent |
| `brand.yellow` | Highlight Yellow / 暖黄 | `#FFE39F` | Highlight |

### Color Principle

- Cream 是主要画布色。
- Ink 是主要文字与手绘线稿色。
- Mint Green 是主要操作色和品牌强调色。
- Soft Blue 用于辅助操作、次级状态和结构信息。
- Blush Pink 用于少量情绪化/强调细节。
- Highlight Yellow 用于提示、点缀和视觉引导。

## 3. Typography

### UI Font

推荐圆润无衬线：

- Nunito
- Quicksand
- Baloo 2

用途：

- 产品名称；
- 标题；
- 按钮；
- UI 文本；
- 标签。

### Code Font

推荐等宽字体：

- JetBrains Mono
- Fira Code
- Source Code Pro

用途：

- Selector；
- Locator；
- Class；
- XPath；
- DOM；
- CSS；
- AI Context；
- 技术信息。

## 4. Illustration

角色保持原 Zeki 手绘角色资产。

产品插画应该：

- 使用柔和 Cream 背景；
- 保持 Ink 手绘轮廓；
- 使用 Mint / Blue / Pink / Yellow 点缀；
- 保持轻微手绘不完美感；
- 不使用 3D、玻璃、霓虹或写实风格。

## 5. Iconography

功能图标建议使用简洁的线性图标体系。

原则：

- 线性；
- 圆角；
- 中等视觉重量；
- 与 Ink 线稿保持一致；
- 小尺寸仍然清晰。

品牌角色 Logo 不等同于功能图标。

## 6. UI Shape

界面组件：

- 圆角；
- 轻量边框；
- 手绘感视觉细节；
- 明确的 hover / selected / success 状态；
- 避免过度阴影；
- 避免过度透明。

## 7. Light Theme

Light 是默认主题。

主要视觉关系：

`Cream background → White / Cream surface → Ink text → Mint primary`

## 8. Dark Theme

Dark 主题必须保留 Warm Precision，而不是转换成传统“纯黑科技风”。

Dark Theme 的具体数值目前属于**实现草案**，品牌板只确认了深色预览，没有冻结完整 Dark Token。

实现时应优先保持：

- 暖黑背景；
- 低亮度 Surface；
- Cream/浅色文字；
- 降低 Mint 饱和度；
- 保留 Blue/Pink/Yellow 作为状态色。

正式 Dark Token 在实际工具栏完成后进行截图验收并冻结。

## 8. Component Language

The confirmed component set from the brand board is:

### Buttons

- **Primary** — Mint Green
- **Secondary** — Soft Blue
- **Ghost** — Cream/transparent surface with Ink border

### Pills / Tags

- HTML — Soft Blue
- CSS — light Mint
- XPath — Highlight Yellow
- Selected — light Mint
- Multi — light Blue

### Icon Buttons

Use compact rounded-square controls with Ink line icons.

Confirmed examples:

- Select
- Copy
- Screenshot
- More
- Close

### Status Chips

- Selected — Mint / success
- Multi (N) — Blue
- Located — Blush Pink
- Info — Highlight Yellow

### Card

Element Info card:

- white / Cream surface;
- Ink title;
- code values in Code Font;
- subtle border;
- rounded corners;
- light shadow.

### Popover

Tip / contextual information:

- compact;
- rounded;
- clear pointer relationship to the triggering element;
- Yellow used for informational emphasis.

### Toolbar

The main product surface is a horizontal floating toolbar.

The toolbar should visually read as a single lightweight control surface, while each action remains individually discoverable.

Recommended grouping:

`Select → Multi → Parent → Child → Prev → Next → Copy Selector → Copy Locator → Screenshot → AI Context → More → Close`


## 9. Icon Rules

- Functional icons should use a consistent line icon family.
- Rounded corners are preferred.
- Icons should remain legible at 16px and 20px.
- Use Ink as the default icon color.
- Use Mint for primary/selected actions.
- Use Blue for secondary navigation.
- Use Yellow/Pink only for semantic emphasis.
- The mascot logo is not a substitute for generic UI icons.

The product toolbar should avoid icon-only ambiguity for unfamiliar actions; where necessary, pair the icon with a short text label.
