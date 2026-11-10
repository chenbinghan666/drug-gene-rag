# Drug–Gene RAG

[简体中文](https://github.com/chenbinghan666/drug-gene-rag/blob/main/README.md) · **English** · [日本語](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.ja.md) · [Deutsch](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.de.md) · [Français](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.fr.md) · [Español](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.es.md) · [Português](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.pt.md)

Enter a gene, a drug, and a cancer type. The tool retrieves PubMed abstracts and uses a Zhipu model to summarize evidence of associations. Built for learning and literature exploration.

Python · PubMed · Zhipu AI

## How it works

1. Receive genes, drugs, and cancer types.
2. PubMed was searched using the NCBI Entrez API.
3. Get abstracts of relevant literature.
4. Send documentary evidence to the Zhipu AI model.
5. Output the results of drug-gene relationship analysis.

## Requirements

- Python 3.8 or higher
- NCBI contact email
- Zhipu Open Platform API Key

## How to use

Install project dependencies:

```powershell
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env`, and then fill in your own configuration:

```text
ZAI_API_KEY=your_zhipu_api_key
email=you@example.com
```

Run the program:

```powershell
python main.py
```

Windows users can also double-click `run.bat`.

## API keys and use of results

`.env` contains a private API Key, which has been excluded by `.gitignore`. Please do not upload or share it. The large model output is only used for learning and literature auxiliary analysis, and cannot replace professional medical judgment.

## Reference

Lai Y-J, Wang L-J, et al. *Inferring Drug–Gene Relationships in Cancer Using Literature-Augmented Large Language Models*. Cancer Research Communications, 2025.
