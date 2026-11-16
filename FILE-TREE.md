<!--
File: FILE-TREE.md
Purpose: 提供由当前仓库文件系统生成的目录树，帮助 AI Agent 和协作者定位文件。
Layer: Repository / Navigation
-->

# Repository File Tree

> 本文件由 `python scripts/generate_file_tree.py` 生成。新增、删除、移动或重命名文件后必须重新生成。
>
> 文件树仅用于定位；文件内容、权限和实际存在状态以当前工作区为准。

```text
zeki-brand/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── product-proposal.md
│   └── PULL_REQUEST_TEMPLATE.md
├── brand/
│   ├── brand-architecture.md
│   ├── messaging.md
│   ├── naming-conventions.md
│   ├── personality.md
│   ├── positioning.md
│   ├── README.md
│   └── story.md
├── content/
│   ├── about.md
│   ├── README.md
│   ├── short-bio.md
│   └── slogans.md
├── governance/
│   ├── asset-management.md
│   ├── decision-log.md
│   ├── domain-management.md
│   └── release-process.md
├── identity/
│   ├── characters/
│   │   ├── kiki/
│   │   │   ├── derived/
│   │   │   │   └── README.md
│   │   │   └── original/
│   │   │       └── kiki-original.png
│   │   ├── zeki/
│   │   │   ├── derived/
│   │   │   │   └── README.md
│   │   │   └── original/
│   │   │       └── zeki-original.png
│   │   ├── asset-manifest.yaml
│   │   └── README.md
│   ├── README.md
│   └── visual-guidelines.md
├── products/
│   ├── projects/
│   │   └── README.md
│   ├── templates/
│   │   ├── product-brief.md
│   │   └── product.yaml
│   ├── product-creation-guide.md
│   ├── product-lifecycle.md
│   ├── README.md
│   └── registry.yaml
├── schemas/
│   └── product-registry.schema.json
├── scripts/
│   ├── check_file_headers.py
│   ├── generate_file_tree.py
│   └── validate_registry.py
├── .editorconfig
├── .gitattributes
├── .gitignore
├── AGENTS.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── FILE-TREE.md
├── README.md
└── requirements-dev.txt
```
