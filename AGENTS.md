<!--
File: AGENTS.md
Purpose: 规定 AI Agent 与协作者执行品牌治理任务时必须遵循的规则。
Layer: Repository / Governance
-->

# AGENTS.md — Zeki Brand Governance

本文件是 `zeki-brand` 仓库中所有 AI Agent、自动化代理和协作者的强制执行规范。发生冲突时，优先遵循品牌主在当前任务中的明确指示；但不得违反隐私、安全和原始素材保护要求。

## 1. 工作前置阅读

开始任何任务前：

- 通用任务：阅读 `README.md`、本文件和相关 `governance/` 规范。
- 品牌策略任务：额外阅读 `brand/` 中相关文档。
- 视觉资产任务：额外阅读 `identity/README.md`、`identity/visual-guidelines.md` 和 `identity/characters/README.md`。
- 产品任务：额外阅读 `products/README.md`、`products/registry.yaml`、`products/product-lifecycle.md` 和对应产品档案。
- 域名任务：额外阅读 `governance/domain-management.md`。

不要只根据文件名或旧对话摘要推断仓库当前事实；以当前分支中的文件为准。

## 2. 品牌事实与决策边界

- 主品牌名称为 `Zeki`；伴侣称呼为 `Kiki`；品牌域名为 `zekiki.cc`。
- Zeki 是主品牌。Kiki 是伴侣及初始角色原画创作者；双方共同项目必须单独标记所有权和参与关系。
- 不得自行更改品牌主名称、品牌关系、核心定位、角色身份或授权规则。
- 未获品牌主确认的名称、Slogan、产品、域名和视觉方案必须标注为 `proposed`、`provisional` 或等价状态。
- 不得将建议、假设、示例、占位值描述为已批准或已上线事实。
- 不得推断域名 DNS、部署、GitHub 仓库或第三方服务已经配置。


## 2A. 文件头（File Header）规范

所有新增或修改的**文本文件**必须在文件开头提供可机器检索的元信息，至少包含：

- `File`：从仓库根目录开始的相对路径；
- `Purpose`：用一句话说明文件职责；
- `Layer`：所属治理层或技术层。

按文件格式使用合法语法：

- Markdown：文件开头使用 HTML 注释块 `<!-- ... -->`。
- YAML、TXT、EditorConfig、Git 配置：使用 `#` 注释行。
- Python：使用模块级 docstring。
- JSON：JSON 不支持注释，使用顶层 `$comment` 字段记录同样的元信息；不得写入非法 JSON 注释。
- 带 YAML Front Matter 的 Markdown（例如 GitHub Issue 模板）：保持 `---` Front Matter 位于文件第一行，在 Front Matter 内使用 YAML 注释记录元信息，避免破坏平台识别。

二进制文件（PNG、JPG、字体、压缩包等）不能添加文本文件头，必须在对应 Manifest 或资产文档中记录路径、用途、来源和校验信息。

文件移动或重命名时，必须同步更新文件头中的 `File` 路径。

## 2B. 文件树（File Tree）规范

- `FILE-TREE.md` 是面向 AI Agent 和协作者的仓库结构导航。
- 开始跨目录任务前，先阅读 `FILE-TREE.md`，再打开目标文件确认实际内容。
- 文件树只负责定位，不代替源文件；文件内容和实际文件系统始终是事实来源。
- 新增、删除、移动或重命名文件/目录后，必须运行：

```bash
python scripts/generate_file_tree.py
```

- 提交前运行：

```bash
python scripts/check_file_headers.py
python scripts/validate_registry.py
```

- 不要手工猜测文件路径；文件树未更新时先重新生成。

## 3. 产品注册规则

- `products/registry.yaml` 是产品清单的唯一结构化事实来源。
- 每个产品必须有唯一、稳定、全小写 kebab-case 的 `id`。
- 新产品先创建提案，再经品牌主确认后登记；尚未批准的方向可登记为 `idea`，但必须标明名称为暂定或提案。
- 更新产品状态、域名、仓库地址、所有权、可见性时，必须同步更新 Registry 和产品档案。
- 不允许重复使用已归档产品的 ID。
- 不允许将多个独立产品的源码放入本仓库；产品代码应位于各自独立仓库。
- 未知值使用 `null` 或 `unknown`，不要猜测。
- 修改 Registry 后运行：

```bash
python scripts/validate_registry.py
```

## 4. 产品生命周期

允许状态：

`idea` → `planned` → `prototype` → `development` → `active` → `maintenance` → `archived`

状态可以根据真实项目情况跳过不适用阶段，但不得仅为了展示进度而虚报状态。状态定义和变更要求见 `products/product-lifecycle.md`。

## 5. 原始角色素材保护

- `identity/characters/**/original/` 是原始素材区。
- 原始图片是不可变资产：禁止覆盖、裁切、压缩、调色、描边、抠图、重绘或转换格式后替代原图。
- 禁止将衍生版本写入 `original/`。
- 新的表情、动作、贴纸、动画帧、透明底版本等必须放入对应角色的 `derived/` 目录。
- 每个衍生素材必须记录原始素材路径、生成/编辑方式、日期、用途和创作者/操作者。
- 不得仅凭文件已在仓库中，就推断获得了公开传播、商业使用或再授权许可。
- 对外公开、商业使用、第三方授权或重大角色改造前，先确认 Kiki 的许可范围。

## 6. 文档与命名

- 默认使用简体中文编写治理文档；品牌名、技术名词和必要的英文表达保留原文。
- 文件名使用小写 kebab-case；目录名使用小写。
- Markdown 标题层级从 `#` 开始，不跳级。
- 日期使用 `YYYY-MM-DD`。
- 产品 ID 使用稳定的英文标识，不随展示名称变化而随意修改。
- 不把密钥、个人隐私、私人日记或用户数据写入文档、示例、Issue 或日志。

## 7. 域名与外部资源

- `zekiki.cc` 是品牌主提供的域名；当前 DNS、证书、托管和子域名状态均未在本仓库验证。
- 只有在品牌主确认后才能将某个域名分配给产品。
- 不创建虚构的仓库 URL、线上地址、部署状态或服务状态。
- 变更域名记录时，更新 `products/registry.yaml`（如涉及产品）及 `governance/domain-management.md`。

## 8. 变更与交付

每次变更应：

1. 明确修改目的和影响范围；
2. 保持单一职责，不顺手改写无关品牌决策；
3. 更新对应文档、Registry 和变更记录；
4. 运行适用的校验；
5. 汇报实际修改文件、校验结果和未完成事项。

推荐 Commit Message：

- `docs: initialize zeki brand foundation`
- `brand: refine brand positioning and messaging`
- `identity: add approved character assets`
- `products: register a new product`
- `governance: define product lifecycle rules`
- `chore: validate brand registry`

不要声称执行了未实际运行的测试或校验。

## 9. 默认禁止事项

- 未经确认修改主品牌方向或把 Kiki 变成默认共同经营者；
- 未经确认新增正式产品、子品牌或域名分配；
- 覆盖原始角色素材；
- 将私人仓库改为公开；
- 将产品源码、密钥或私密内容混入品牌仓库；
- 为追求“完整”而编造产品状态、用户数据、上线信息或外部链接。
