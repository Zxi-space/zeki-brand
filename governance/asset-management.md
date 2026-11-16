<!--
File: governance/asset-management.md
Purpose: 规定原始、衍生、发布和第三方视觉资产的管理方式。
Layer: Governance / Assets
-->

# Asset Management

## 1. 资产分类

- Original：原始创作文件，不可覆盖；
- Derived：从原始资产派生的文件；
- Published：已批准用于公开渠道的输出；
- Third-party：第三方素材，必须记录来源和许可。

## 2. 原始资产要求

- 保留原始文件名或稳定的归档文件名；
- 不覆盖、不压缩、不裁切、不重绘；
- 记录创作者、来源、日期、校验和及许可状态；
- 如需迁移目录，必须同步更新 manifest 和引用。

## 3. 衍生资产要求

每项衍生资产至少记录：

```yaml
id: zeki-character-expression-001
source: identity/characters/zeki/original/zeki-original.png
path: identity/characters/zeki/derived/example.png
created_at: "YYYY-MM-DD"
creator: "TBD"
method: "TBD"
purpose: "TBD"
permission_status: "pending"
```

## 4. 发布前检查

- 是否获得创作者许可；
- 是否包含私人或不适合公开的信息；
- 是否误用第三方素材；
- 输出是否正确标注来源；
- 是否保留原始文件。
