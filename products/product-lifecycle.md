<!--
File: products/product-lifecycle.md
Purpose: 定义产品从 Idea 到归档的状态和状态变更条件。
Layer: Products / Lifecycle
-->

# Product Lifecycle

## 1. 状态定义

| 状态 | 含义 | 进入条件 |
|---|---|---|
| `idea` | 已记录的产品想法，尚未批准进入正式规划 | 有基本问题描述和提案 |
| `planned` | 已确认值得推进，准备排期和拆分范围 | 品牌主明确批准 |
| `prototype` | 正在验证关键假设或交互 | 有可验证的原型/实验 |
| `development` | 正式开发中 | 技术方案和首期范围明确 |
| `active` | 已对目标用户提供可用版本 | 已完成发布检查并确认可访问 |
| `maintenance` | 暂停主要功能开发，保留维护 | 明确维护责任和范围 |
| `archived` | 已停止维护或正式退役 | 完成数据、域名和用户影响评估 |

## 2. 状态变更

- 状态必须反映真实进度，不得为了展示而提前升级。
- `idea` → `planned` 需要品牌主确认。
- `prototype` 不等于正式上线。
- `active` 必须有可验证的发布地址或明确的交付渠道。
- 进入 `maintenance` 或 `archived` 时，应记录原因和用户影响。
- 归档产品保留历史 ID，不得将 ID 分配给新产品。

## 3. 状态与可见性不是一回事

`status` 表示生命周期；`visibility` 表示信息或产品的可见范围。

允许的 `visibility`：

- `public`：可公开展示；
- `private`：仅授权人员访问；
- `unlisted`：不主动公开，但可通过链接访问；
- `internal`：仅内部工作使用。

产品即使状态为 `active`，也可以是 `private`。
