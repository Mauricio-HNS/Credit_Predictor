# Credit Predictor

Credit Predictor is a lightweight machine learning project for default-risk prediction using Python and Gradio.

## What it does

- trains a simple credit-risk model
- predicts default tendency from user inputs
- exposes a small Gradio interface for interactive testing

## Stack

- Python
- scikit-learn
- Gradio

## Local run

```bash
cd credit_predictor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python train_model.py
python app_ui.py
```

## Project structure

```text
Credit_Predictor/
  credit_predictor/
    app_ui.py
    train_model.py
    requirements.txt
    model.pkl
```

## Positioning

This repository is intentionally simple: it is a compact ML demo focused on explainable local experimentation rather than a production-grade risk platform.

## Next upgrades

1. add evaluation metrics to the README
2. persist experiments and model versions
3. expose a small REST API
4. improve the feature set beyond age, income and debt
