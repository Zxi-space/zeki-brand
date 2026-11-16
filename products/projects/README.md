<!--
File: products/projects/README.md
Purpose: 说明该文件的用途和维护边界。
Layer: Repository / Documentation
-->

# Product Project Records

每个已登记产品可以在这里建立一个独立档案目录，目录名必须与 `products/registry.yaml` 中的产品 `id` 一致。

建议结构：

```text
projects/
└── <product-id>/
    ├── README.md
    ├── product.yaml
    ├── scope.md
    └── decisions.md
```

创建新目录前先阅读 `products/product-creation-guide.md`。不要在此目录存放产品业务源码；产品源码应放在独立 Git 仓库。
