<!--
File: products/product-creation-guide.md
Purpose: 规定新产品从提案、注册到独立开发和发布的流程。
Layer: Products / Governance
-->

# Product Creation Guide

新增任何 Zeki 生态产品时，按本流程执行。

## Step 1 — 提交 Idea

复制 `templates/product-brief.md`，回答：

- 要解决什么问题？
- 谁会使用？
- 为什么值得做？
- 首期最小范围是什么？
- 是否涉及 Zeki、Kiki 或双方共同参与？
- 是否会处理私人或敏感数据？

信息不足时保留 `TBD`，不要编造。

## Step 2 — 品牌与产品评审

检查：

- 名称是否清晰，是否与现有产品冲突；
- 产品归属是 `zeki`、`kiki` 还是 `joint`；
- 公开/私有边界是否清楚；
- 是否需要独立品牌或独立视觉系统；
- 是否涉及第三方素材、商标或授权；
- 域名是否可用（需外部实际核验）。

## Step 3 — 注册产品

品牌主确认后：

1. 分配唯一 `id`；
2. 在 `registry.yaml` 增加产品条目；
3. 复制 `templates/product.yaml`，建立产品元数据；
4. 创建 `projects/<product-id>/README.md`；
5. 状态设为 `planned`；若仍在等待评审则保留 `idea`。

## Step 4 — 建立独立代码仓库

产品源码独立管理。建立仓库后，再把真实仓库 URL 写入 Registry。

不得提前编造 GitHub URL，也不得将所有产品代码合并进 `zeki-brand`。

## Step 5 — 开发与品牌接入

产品按自身用户和场景设计 UI。需要使用品牌资产时：

- 引用正式批准的 Logo、Tokens 或角色衍生素材；
- 不修改原始角色图片；
- 产品 About/Footer 中使用准确的品牌归属说明；
- 不将未授权素材打包到公开或商业产品中。

## Step 6 — 发布与归档

发布前核对：

- 产品功能和隐私边界；
- 域名、证书和部署状态；
- 对外介绍与实际能力一致；
- 角色、字体、图标和第三方资源许可；
- Registry、产品档案和变更记录同步。

发布后将状态更新为 `active`，记录真实发布日期和 URL。
