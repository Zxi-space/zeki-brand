<!--
File: README.md
Purpose: 说明 Zeki Brand 仓库定位、结构、使用方式和当前基线。
Layer: Repository / Overview
-->

# Zeki Brand

> Zeki 个人品牌与数字产品生态的治理仓库（Brand Source of Truth）。

**仓库建议名称：** `zeki-brand`  
**品牌主名称：** Zeki  
**共同生活与创作关系：** Zeki & Kiki  
**品牌域名：** `zekiki.cc`（由品牌主提供；DNS 与部署状态尚未在本仓库验证）  
**当前基线：** B0 — Brand Foundation  
**仓库可见性：** Private

---

## 1. 仓库定位

`zeki-brand` 集中管理 Zeki 品牌的长期有效信息、视觉资产索引、产品注册信息和治理规范。它是品牌生态的**事实来源**，不是所有产品代码的 monorepo，也不是产品运行时依赖。

本仓库负责：

- 品牌定位、故事、核心表达、人格和命名规范；
- Zeki、Kiki 及双人角色的原始视觉资产与使用规则；
- 所有品牌产品的统一注册表和产品档案入口；
- 产品新增、状态变更、域名登记、发布与归档流程；
- AI Agent 和协作者执行品牌相关工作的约束。

本仓库不负责：

- 存放各产品的业务源码；
- 管理生产环境密钥、访问令牌、用户数据或私人日记；
- 自动创建 DNS 记录、GitHub 仓库或云资源；
- 在未获确认时将提案描述为已批准决策。

## 2. 品牌关系

- **Zeki**：主品牌与个人创造者品牌，聚焦技术、产品和持续创造。
- **Kiki**：Zeki 的伴侣，也是本仓库所收录两张初始角色原画的创作者。
- **Zeki & Kiki**：用于表达双方共同生活、共同创作或共同拥有的项目。具体参与关系应在每个产品档案中单独说明。

Zeki 是主品牌。Kiki 不会被默认视为所有 Zeki 产品的共同所有者；同样，双人项目也不得默认归为 Zeki 单方项目。

## 3. 文件导航

完整、自动生成的仓库文件树见 [`FILE-TREE.md`](FILE-TREE.md)。

常用目录：

- `brand/`：品牌定位、故事、核心表达和命名规范；
- `identity/`：视觉规范、角色原画和衍生素材；
- `products/`：产品 Registry、产品档案和新增流程；
- `schemas/`：结构化数据校验 Schema；
- `governance/`：域名、资产、决策和发布规范；
- `content/`：个人介绍和对外表达；
- `scripts/`：文件树生成、文件头检查和 Registry 校验工具。

新增、删除、移动或重命名文件后，运行 `python scripts/generate_file_tree.py` 更新文件树。

## 4. 快速开始

### 阅读顺序

1. `AGENTS.md`：所有协作者和 AI Agent 的执行规则；
2. `brand/positioning.md`：品牌定位；
3. `brand/brand-architecture.md`：Zeki、Kiki 与双人项目的关系；
4. `identity/characters/README.md`：原始角色素材保护规则；
5. `products/README.md`：产品注册和维护入口；
6. `governance/decision-log.md`：已经确认的治理决策及待确认事项。

### 验证仓库元信息与产品注册表

需要 Python 3.10 或更高版本：

```bash
python -m pip install -r requirements-dev.txt
python scripts/generate_file_tree.py
python scripts/check_file_headers.py
python scripts/validate_registry.py
```

验证脚本检查 `products/registry.yaml` 是否符合 `schemas/product-registry.schema.json`。

## 5. 当前产品登记原则

`products/registry.yaml` 是产品清单的唯一结构化事实来源。

B0 仅登记当前已经明确表达的两个产品方向：

- Zeki 个人品牌网站；
- Zeki 与 Kiki 的情侣数字空间。

这两个条目暂时使用提案名称和 `idea` 状态。名称、具体功能、产品域名、代码仓库和发布日期均未最终批准。其他 Idea 网站不预先虚构条目；确定具体方向后再按产品新增流程登记。

## 6. 当前品牌表达状态

- 主品牌名称 `Zeki`：已确认。
- 伴侣称呼 `Kiki`：已确认。
- 品牌域名 `zekiki.cc`：由品牌主提供。
- “Independent Maker”定位：当前工作定位，后续可调整。
- “Make ideas real.”：候选英文表达，不是已批准的唯一 Slogan。
- 两张角色原画：作为原始素材保留，不在 B0 中进行重绘、裁切或风格化。

## 7. 变更原则

- 品牌核心定位、主品牌名称、角色身份和授权规则属于受控信息，修改前需要品牌主明确确认。
- 新产品必须先有提案，再登记 `registry.yaml`，之后建立独立代码仓库。
- 产品状态、域名、仓库地址等事实必须有明确依据；未知信息使用 `null` 或 `unknown`，不得猜测。
- 原始角色图不可覆盖。所有衍生图进入 `derived/`，并记录来源和处理信息。
- 重要决策写入 `governance/decision-log.md`；可见变更写入 `CHANGELOG.md`。

## 8. 隐私与版权

本仓库初始设置为 Private。不要在仓库中提交密码、Token、私钥、生产配置、私人聊天记录或未经双方同意公开的情侣内容。

角色原画由 Kiki 创作。收录原图不等于自动取得任意商业授权或第三方再授权权利。公开发布、商业使用、对外授权及重大衍生创作，应先与创作者确认并记录许可范围。

## 9. 当前阶段

| 阶段 | 内容 | 状态 |
|---|---|---|
| B0 | 品牌基础、治理规则、产品注册基线 | 本仓库初始化交付 |
| B1 | 完整视觉识别、Logo、设计 Tokens、角色衍生素材 | 待启动 |
| B2 | 产品治理自动化、更多产品档案与发布流程完善 | 待启动 |

B0 的目标是建立稳定、可维护的治理基线，不代表所有视觉与产品决策已经最终定稿。
