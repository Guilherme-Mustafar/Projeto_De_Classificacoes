import os
import pandas as pd

def extrair_arquivo_mais_recente(pasta="data/raw"):
    arquivos = [
        os.path.join(pasta, f)
        for f in os.listdir(pasta)
        if f.endswith(".csv")
    ]

    if not arquivos:
        raise FileNotFoundError("Nenhum arquivo CSV encontrado na pasta.")

    arquivo_recente = max(arquivos, key=os.path.getctime)

    print(f"Arquivo selecionado: {arquivo_recente}")

    df = pd.read_csv(arquivo_recente, sep=",", encoding="utf-8")

    return df