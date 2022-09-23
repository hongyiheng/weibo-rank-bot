# weibo-rank-bot

企业微信微博热搜信息推送 bot

## 示例

### 1. 创建 workflow

在你的任意一个 GitHub 仓库 `.github/workflows/` 文件夹下创建一个 `.yml` 文件，如 `cc.yml`，内容如下：

```yml
name: weibo-rank-bot

on:
  schedule:
    - cron: '30 9,12,14,17 * * *'
  workflow_dispatch:

jobs:
  checkin:
    runs-on: ubuntu-latest
    steps:
      - uses: hongyiheng/weibo-rank-bot@v0.0.5
        with:
          WEBHOOK: ${{ secrets.WEBHOOK }}
```

### 2. 配置 secrets 参数

在 GitHub 仓库的 `Settings -> Secrets` 路径下配置好 `WEBHOOK`

参数获取：

- WEBHOOK： [企业微信群机器人WEBHOOK](https://zhuanlan.zhihu.com/p/370006823)

### 运行结果示例
![image](https://user-images.githubusercontent.com/48740408/191908521-638c2f58-8c3b-4ebc-96f4-6e068751fe34.png)
