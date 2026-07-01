import os
import pandas as pd
from config.settings import CAMINHO_CSV_FINAL


def salvar_dados_em_csv(lista_faturas):

    try:
        if not lista_faturas:
            print(" Nenhuma fatura na lista para salvar.")
            return False

        df = pd.DataFrame(lista_faturas)
        df.to_csv(CAMINHO_CSV_FINAL, index=False, encoding="utf-8")

        print(f"\n CSV gerado com sucesso! Total de registros: {len(lista_faturas)}")
        print(f" Arquivo salvo em: {CAMINHO_CSV_FINAL}")
        return True

    except Exception as e:
        print(f" ERRO Falha ao salvar o arquivo CSV: {e}")
        return False

