<!--
File: CONTRIBUTING.md
Purpose: 说明品牌仓库变更、校验、审批和提交约定。
Layer: Repository / Contribution
-->

# Contributing to Zeki Brand

本仓库目前由品牌主维护。协作者和 AI Agent 提交变更时遵循以下约定。

## 变更类型

- 品牌策略：定位、故事、核心表达、人格、命名；
- 视觉识别：Logo、颜色、字体、角色素材、设计 Tokens；
- 产品治理：产品提案、Registry、产品档案、生命周期；
- 基础治理：域名、发布、资产、隐私与决策记录。

## 提交前检查

1. 阅读根目录 `AGENTS.md`。
2. 确认变更是否影响已确认的品牌事实。
3. 确认产品 Registry 与产品档案一致。
4. 对角色素材确认原始文件未被修改。
5. 运行 `python scripts/generate_file_tree.py` 更新文件树。
6. 运行 `python scripts/check_file_headers.py` 检查文件头。
7. 运行 `python scripts/validate_registry.py`。
8. 更新 `CHANGELOG.md` 和必要的决策记录。

## Commit Message

使用 Conventional Commits 风格，建议类型：

- `docs`
- `brand`
- `identity`
- `products`
- `governance`
- `content`
- `chore`

示例：

```text
docs: initialize zeki brand foundation
products: add zeki personal website proposal
identity: document original character asset policy
governance: define domain assignment process
```

## 变更审批

品牌主名称、定位、核心表达、角色身份、素材授权、产品所有权、域名分配及仓库可见性等重大事项，必须由品牌主明确确认。协作者可以提出方案，但不能自行将提案升级为正式决策。
