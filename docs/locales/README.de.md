# Drug–Gene RAG

[简体中文](https://github.com/chenbinghan666/drug-gene-rag/blob/main/README.md) · [English](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.en.md) · [日本語](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.ja.md) · **Deutsch** · [Français](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.fr.md) · [Español](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.es.md) · [Português](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.pt.md)

Nach Eingabe eines Gens, eines Wirkstoffs und einer Krebsart ruft das Tool PubMed-Abstracts ab. Ein Zhipu-Modell fasst die Hinweise auf Zusammenhänge zusammen. Gedacht für Lernzwecke und Literaturrecherche.

Python · PubMed · Zhipu AI

## Funktioneller Ablauf

1. Erhalten Sie Gene, Medikamente und Krebsarten.
2. PubMed wurde mithilfe der NCBI Entrez API durchsucht.
3. Erhalten Sie Abstracts relevanter Literatur.
4. Senden Sie dokumentarische Beweise an das Intellectual Spectrum-Modell.
5. Geben Sie die Ergebnisse der Drogen-Gen-Beziehungsanalyse aus.

## Umweltanforderungen

- Python 3.8 oder höher
- NCBI-Kontakt-E-Mail
- Zhipu Open Platform API-Schlüssel

## Wie zu verwenden

Projektabhängigkeiten installieren:

```powershell
python -m pip install -r requirements.txt
```

Kopieren Sie `.env.example` nach `.env` und geben Sie dann Ihre eigene Konfiguration ein:

```text
ZAI_API_KEY=your_zhipu_api_key
email=you@example.com
```

Führen Sie das Programm aus:

```powershell
python main.py
```

Windows-Benutzer können auch auf `run.bat` doppelklicken.

## Sicherheitshinweise

`.env` enthält einen privaten API-Schlüssel, der von `.gitignore` ausgeschlossen wurde. Bitte laden Sie es nicht hoch oder teilen Sie es nicht. Die große Modellausgabe wird nur für Lern- und Literaturhilfsanalysen verwendet und kann eine professionelle medizinische Beurteilung nicht ersetzen.

## Referenzpapiere

Lai Y-J, Wang L-J, et al. *Inferring Drug–Gene Relationships in Cancer Using Literature-Augmented Large Language Models*. Cancer Research Communications, 2025.
