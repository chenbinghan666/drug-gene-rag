# Drug–Gene RAG

**简体中文** · [English](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.en.md) · [日本語](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.ja.md) · [Deutsch](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.de.md) · [Français](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.fr.md) · [Español](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.es.md) · [Português](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.pt.md)

输入基因、药物和癌症类型，从 PubMed 检索摘要，再用智谱模型整理文献中的关联证据。面向学习和文献辅助阅读。

Python · PubMed · Zhipu AI

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
