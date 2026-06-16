import pandas as pd
import numpy as np

def remover_geral_se_multiplas(valor):
    
    if pd.isna(valor):
        return valor
        
    partes = [p.strip() for p in valor.split(',')]
        
    if len(partes) > 1:
         partes = [p for p in partes if p != 'Atendimento em Geral']
        
    return ', '.join(partes)


def limpar_dados(df):
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df["data_inicio"] = pd.to_datetime(df["data_inicio"], errors="coerce")
    df["data_encerramento"] = pd.to_datetime(df["data_encerramento"], errors="coerce")

    df["tempo_atendimento"] = pd.to_timedelta(
        df["tempo_de_atendimento"],
        errors="coerce"
    )

    df["tempo_atendimento_min"] = (
        df["tempo_atendimento"].dt.total_seconds() / 60
    ).round(2)

    df["classificação"] = df["classificação"].fillna("Não Avaliado")

    return df
