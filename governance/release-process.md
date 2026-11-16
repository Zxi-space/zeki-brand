<!--
File: governance/release-process.md
Purpose: 定义品牌仓库变更级别、发布检查和版本记录要求。
Layer: Governance / Release
-->

# Brand Repository Release Process

## 1. 变更级别

- Patch：错别字、链接、非实质性说明修订；
- Minor：新增产品档案、规范章节、获批准的品牌资产；
- Major：主品牌名称、品牌架构、核心定位或治理模型发生不兼容变化。

版本号仅在品牌主决定发布 Tag 时生效；日常提交不要求每次打版本。

## 2. 发布检查

- [ ] `AGENTS.md` 和相关治理规范已遵循；
- [ ] Registry 校验通过；
- [ ] 产品档案与 Registry 一致；
- [ ] 原始角色素材未被修改；
- [ ] 对外使用的素材许可已确认；
- [ ] 没有密钥、私人数据或未批准公开内容；
- [ ] `CHANGELOG.md` 已更新；
- [ ] 重大决策已写入 `decision-log.md`。

## 3. 推荐提交信息

```text
docs: initialize zeki brand foundation
brand: approve brand messaging baseline
identity: add approved logo assets
products: register a new product
governance: update domain assignment policy
```

## 4. 发布事实

只有在真实创建 Git Tag、发布 Release 后，才能在文档中记录对应版本已发布。不要仅因文档写了版本号就声称 GitHub Release 已创建。
