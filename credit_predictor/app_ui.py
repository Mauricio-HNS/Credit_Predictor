import gradio as gr
import joblib
import pandas as pd

model = joblib.load("model.pkl")

def prever(idade, renda, divida):
    df = pd.DataFrame([{"idade": idade, "renda": renda, "divida": divida}])
    pred = model.predict(df)[0]
    return "Inadimplente" if pred == 1 else "Adimplente"

iface = gr.Interface(
    fn=prever,
    inputs=[
        gr.Number(label="Idade"),
        gr.Number(label="Renda (R$)"),
        gr.Number(label="Dívida (R$)")
    ],
    outputs="text",
    title="Previsão de Inadimplência",
    theme="compact"
)

iface.launch(share=True)