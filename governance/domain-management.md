<!--
File: governance/domain-management.md
Purpose: 管理品牌主域名、产品域名分配和 DNS 状态记录规则。
Layer: Governance / Domains
-->

# Domain Management

## 1. 已知域名

| 域名 | 来源 | 规划角色 | DNS 状态 |
|---|---|---|---|
| `zekiki.cc` | 品牌主提供 | 品牌生态主域名 | 未验证 |

`zekiki.cc` 的域名信息来自品牌主陈述。本仓库没有验证注册商、到期时间、DNS、证书或托管配置。

## 2. 域名分配规则

- 根域名和子域名的用途由品牌主确认后登记。
- 不因产品名称推断子域名已经分配。
- 未核验可用性前，候选域名只能记录为候选，不得写入正式 `domain` 字段。
- 域名分配后同步更新 `products/registry.yaml` 和产品档案。
- DNS、TLS、托管与重定向应分别记录状态。

## 3. 推荐记录字段

- 域名；
- 用途/角色；
- 归属人或管理账号（不要记录密码和 Token）；
- 注册状态；
- 到期日期（如有可靠信息）；
- DNS 状态；
- TLS 状态；
- 关联产品；
- 变更日期和决策记录。

## 4. 安全

不要把注册商密码、API Token、Cloudflare API Key、私钥或恢复码写入仓库。通过密码管理器或平台 Secret 管理。
