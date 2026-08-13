# Drug–Gene RAG

这是一个基于 PubMed API 和智谱大模型 API 的入门项目。用户输入基因、药物和癌症类型后，程序会检索相关 PubMed 文献，并让大模型依据检索结果分析药物与基因的关系。

## 功能流程

1. 接收基因、药物和癌症类型。
2. 使用 NCBI Entrez API 检索 PubMed。
3. 获取相关文献摘要。
4. 将文献证据发送给智谱大模型。
5. 输出药物–基因关系分析结果。

## 环境要求

- Python 3.8 或更高版本
- NCBI 联系邮箱
- 智谱开放平台 API Key

## 使用方法

安装项目依赖：

```powershell
python -m pip install -r requirements.txt
```

将 `.env.example` 复制为 `.env`，然后填写自己的配置：

```text
ZAI_API_KEY=你的智谱API密钥
email=你的联系邮箱
```

运行程序：

```powershell
python main.py
```

Windows 用户也可以双击 `run.bat`。

## 安全说明

`.env` 含有私人 API Key，已通过 `.gitignore` 排除，请勿上传或分享。大模型输出仅用于学习和文献辅助分析，不能替代专业医学判断。

## 参考论文

Lai Y-J, Wang L-J, et al. *Inferring Drug–Gene Relationships in Cancer Using Literature-Augmented Large Language Models*. Cancer Research Communications, 2025.
