# Drug–Gene RAG

[简体中文](https://github.com/chenbinghan666/drug-gene-rag/blob/main/README.md) · [English](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.en.md) · **日本語** · [Deutsch](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.de.md) · [Français](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.fr.md) · [Español](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.es.md) · [Português](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.pt.md)

遺伝子、薬剤、がんの種類を入力すると、PubMed の抄録を検索し、智譜のモデルで関連を示す文献の根拠を整理します。学習や文献調査向けです。

Python · PubMed · Zhipu AI

## 機能フロー

1. 遺伝子、薬剤、がんの種類を受け取ります。
2. PubMed は、NCBI Entrez API を使用して検索されました。
3. 関連する文献の要約を入手します。
4. 証拠書類を知的スペクトル モデルに送信します。
5. 薬剤と遺伝子の関連解析結果を出力します。

## 環境要件

- Python 3.8以降
- NCBI の連絡先メールアドレス
- Zhipu オープン プラットフォーム API キー

## 使用方法

プロジェクトの依存関係をインストールします。

```powershell
python -m pip install -r requirements.txt
```

`.env.example` を `.env` にコピーし、独自の構成を入力します。

```text
ZAI_API_KEY=your_zhipu_api_key
email=you@example.com
```

プログラムを実行します。

```powershell
python main.py
```

Windows ユーザーは、`run.bat` をダブルクリックすることもできます。

## 安全上の注意事項

`.env` には、`.gitignore` によって除外されたプライベート API キーが含まれています。アップロードしたり共有したりしないでください。大規模なモデル出力は学習および文献の補助分析にのみ使用され、専門的な医学的判断に代わることはできません。

## 参考文献

Lai Y-J, Wang L-J, et al. *Inferring Drug–Gene Relationships in Cancer Using Literature-Augmented Large Language Models*. Cancer Research Communications, 2025.
