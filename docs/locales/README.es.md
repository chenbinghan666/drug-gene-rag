# Drug–Gene RAG

[简体中文](https://github.com/chenbinghan666/drug-gene-rag/blob/main/README.md) · [English](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.en.md) · [日本語](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.ja.md) · [Deutsch](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.de.md) · [Français](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.fr.md) · **Español** · [Português](https://github.com/chenbinghan666/drug-gene-rag/blob/main/docs/locales/README.pt.md)

Tras introducir un gen, un fármaco y un tipo de cáncer, la herramienta recupera resúmenes de PubMed. Un modelo de Zhipu resume la evidencia sobre sus asociaciones. Está orientada al aprendizaje y a la exploración bibliográfica.

Python · PubMed · Zhipu AI

## Flujo funcional

1. Recibir genes, medicamentos y tipos de cáncer.
2. Se buscó en PubMed utilizando la API NCBI Entrez.
3. Obtenga resúmenes de literatura relevante.
4. Envío de evidencia documental al modelo Espectro Intelectual.
5. Generar los resultados del análisis de la relación fármaco-gen.

## Requisitos medioambientales

- Python 3.8 o superior
- Correo electrónico de contacto del NCBI
- Clave API de plataforma abierta Zhipu

## como usar

Instalar dependencias del proyecto:

```powershell
python -m pip install -r requirements.txt
```

Copie `.env.example` a `.env` y luego complete su propia configuración:

```text
ZAI_API_KEY=your_zhipu_api_key
email=you@example.com
```

Ejecute el programa:

```powershell
python main.py
```

Los usuarios de Windows también pueden hacer doble clic en `run.bat`.

## Instrucciones de seguridad

`.env` contiene una clave API privada, que ha sido excluida por `.gitignore`. Por favor no lo subas ni lo compartas. El resultado del modelo grande solo se utiliza para el aprendizaje y el análisis auxiliar de la literatura y no puede reemplazar el juicio médico profesional.

## Artículos de referencia

Lai Y-J, Wang L-J, et al. *Inferring Drug–Gene Relationships in Cancer Using Literature-Augmented Large Language Models*. Cancer Research Communications, 2025.
