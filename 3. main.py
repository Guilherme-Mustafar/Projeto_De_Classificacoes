from extracao import extrair_arquivo_mais_recente
from limpeza import limpar_dados
import pandas as pd
import numpy as np

def classificar_outlier(df_limpo, limite_min=720):
    df_limpo["flag_outlier"] = (df_limpo["tempo_atendimento_min"] > limite_min).astype(int)
    return df_limpo


def main():
    pd.set_option("display.max_rows", 10)
    pd.set_option("display.max_columns", 10)
    pd.set_option("display.width", 10)
    pd.set_option("display.max_colwidth", 10)

    df_bruto = extrair_arquivo_mais_recente("data/raw")
    df_limpo = limpar_dados(df_bruto)

    df_limpo = df_limpo.drop(columns=['tempo_de_atendimento', 'tempo_atendimento'])
    df_limpo = classificar_outlier(df_limpo)

    print("\n=== LIMPO ===")
    df_limpo.info()

    df_limpo.to_csv('DadosTratados1-Atendimento.csv', index=False)


if __name__ == "__main__":
    main()

