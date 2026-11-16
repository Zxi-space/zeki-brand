<!--
File: products/README.md
Purpose: 说明产品 Registry、产品档案和新增产品的管理入口。
Layer: Products / Navigation
-->

# Product Registry

本目录是 Zeki 产品生态的管理入口。

## 1. 单一事实来源

- `registry.yaml`：所有产品的机器可读总清单；
- `projects/<product-id>/`：后续产品档案目录（按需创建）；
- `templates/product.yaml`：产品元数据模板；
- `templates/product-brief.md`：产品提案模板；
- `product-lifecycle.md`：状态定义；
- `product-creation-guide.md`：新增产品流程。

不要在 README、聊天记录或个人笔记中维护第二份互相独立的产品清单。

## 2. B0 初始登记

B0 登记两个用户已经明确表达的产品方向：

1. Zeki 个人品牌网站；
2. Zeki 与 Kiki 的情侣数字空间。

两者目前均为 `idea`，展示名为暂定提案；尚未确定产品域名、代码仓库、详细功能和发布日期。

其他 Idea 网站应在形成具体提案后再登记，不预先创建虚构项目。

## 3. 新增产品

1. 复制 `templates/product-brief.md` 并填写；
2. 明确产品归属、目标用户、问题、核心范围和隐私级别；
3. 品牌主确认产品方向与名称；
4. 复制 `templates/product.yaml`，分配唯一 ID；
5. 更新 `registry.yaml`；
6. 创建 `projects/<product-id>/README.md` 产品档案；
7. 运行 Registry 校验；
8. 通过独立 Git 仓库管理产品源码。

## 4. 产品与品牌关系

不是所有产品都必须叫 `Zeki Something`。产品可以建立独立视觉系统，但必须在档案中说明品牌归属、署名方式和双方参与关系。
