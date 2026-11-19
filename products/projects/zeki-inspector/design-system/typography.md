# Zeki Inspector — Typography

<!--
File: zeki-brand/products/zeki-inspector/design-system/typography.md
Purpose: 统一 UI 字体、代码字体、字号、行高与字重使用规则。
Layer: Design System / Typography
Source: brand/visual-identity.md and design-system/tokens.json
-->

## 1. Typography Direction

字体气质服务于 **Warm Precision / 温和的精确**：UI 字体圆润、友好、易读；技术内容使用清晰的等宽字体。避免过度装饰或影响长时间阅读的字体。

## 2. Font Families

### UI Font

```css
font-family: Nunito, Quicksand, "Baloo 2", system-ui, sans-serif;
```

用于产品名称、标题、按钮、工具栏标签、表单、说明和状态文本。

### Code Font

```css
font-family: "JetBrains Mono", "Fira Code", "Source Code Pro",
  ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
```

用于 CSS Selector、Playwright Locator、XPath、HTML/CSS/DOM、Class、Attribute、Node 信息及 AI Context 技术片段。

## 3. Type Scale

| Token | Font size | Line height | Typical use |
|---|---:|---:|---|
| `xs` | 11px | 16px | 辅助标签、极短元信息 |
| `sm` | 12px | 16px | 次要说明、状态标签 |
| `md` | 13px | 18px | 紧凑型工具栏文本 |
| `base` | 14px | 20px | 默认 UI 正文 |
| `lg` | 16px | 22px | 卡片标题、强调文本 |
| `xl` | 20px | 26px | 页面/面板标题 |
| `display` | 28px | 32px | 欢迎页或展示型标题 |

## 4. Font Weights

| Token | Weight | Usage |
|---|---:|---|
| `regular` | 400 | 正文与常规说明 |
| `medium` | 500 | 按钮、导航与次级标题 |
| `semibold` | 600 | 卡片标题、重要字段 |
| `bold` | 700 | 品牌标题、关键状态 |

## 5. Usage Rules

- 同一信息层级保持字号和字重一致。
- 工具栏优先使用 `md` / `base`，避免挤压操作空间。
- Selector / Locator 展示使用等宽字体，并允许换行或横向滚动。
- 代码值与普通说明文字必须有明确的视觉区分。
- 不通过大量粗体制造层级；优先使用字号、颜色和间距。
- `xs` 不用于长段正文。

## 6. CSS Tokens

```css
:root {
  --font-ui: Nunito, Quicksand, "Baloo 2", system-ui, sans-serif;
  --font-code: "JetBrains Mono", "Fira Code", "Source Code Pro",
    ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}
```

## 7. Status

字体家族和基础字号来自当前品牌基线。字体文件是否随产品打包、字体加载策略及最终渲染效果，应在浏览器扩展实际 UI 中验证后再冻结。
