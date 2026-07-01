import os
import re
from threading import local

import easyocr
from config.settings import IDIOMAS_OCR, USAR_GPU

def extrairDadosFaturas(caminho_imagem, id_fatura, due_date):
    if not os.path.exists(caminho_imagem):
        print(f"Error arquivo {caminho_imagem} nao encontrado!")
        return None

    print(f" iniciando OCR no arquivo {caminho_imagem}")
    leitor = easyocr.Reader(IDIOMAS_OCR, gpu=USAR_GPU)
    resultado = leitor.readtext(caminho_imagem, detail=0)

    dados_extraidos = {
        "ID": id_fatura,
        "due_date": due_date,
        "company_name": None,
        "invoice_number": None,
        "invoice_date": None,
        "total_due": None
    }

    print("--- TEXTO EXTRAÍDO DA IMAGEM ---")
    for linha in resultado:
        print(linha)
    print("--------------------------------")

    # 1. Nome da Empresa para quando a primeira linha é INVOICE
    if len(resultado) > 0:
        primeira_linha = resultado[0].strip()
        if primeira_linha.upper() == "INVOICE" and len(resultado) > 2:
            dados_extraidos["company_name"] = resultado[2].strip()
        else:
            dados_extraidos["company_name"] = primeira_linha

    # 2. Varre as linhas
    for i, linha in enumerate(resultado):
        linha_limpa = linha.upper().strip()

        #  CAPTURA INVOICE NUMBER
        # Procura por "INVOICE" seguido ou não de "#" e captura os números na mesma linha
        if "INVOICE" in linha_limpa:
            numeros = re.findall(r'(?:INVOICE|#)\s*(\d+)', linha_limpa)
            if numeros:
                dados_extraidos["invoice_number"] = numeros[0]
            # Se a palavra INVOICE estiver sozinha, olha proxima linha
            elif (i + 1) < len(resultado):
                proxima_linha = resultado[i + 1].strip()
                apenas_numeros = re.sub(r'\D', '', proxima_linha)
                if apenas_numeros:
                    dados_extraidos["invoice_number"] = apenas_numeros

        # CAPTURA INVOICE DATE
        if not dados_extraidos["invoice_date"]:
            #  Procura pelo padrão data com traço
            padrao_iso = re.search(r'\d{4}-\d{2}-\d{2}', linha)
            # Procura por padrão de data com barras ou traços
            padrao_comum = re.search(r'\d{2}[-/]\d{2}[-/]\d{4}', linha)

            if padrao_iso:
                dados_extraidos["invoice_date"] = padrao_iso.group(0)
            elif padrao_comum:
                dados_extraidos["invoice_date"] = padrao_comum.group(0)
            # layout dependa da palavra "DATE" Layout 1
            elif "DATE" in linha_limpa:
                if ":" in linha and len(linha.split(":")[-1].strip()) > 0:
                    dados_extraidos["invoice_date"] = linha.split(":")[-1].strip()
                elif (i + 2) < len(resultado):
                    mes = resultado[i + 1].strip()
                    ano = resultado[i + 2].strip()
                    dados_extraidos["invoice_date"] = f"{mes} {ano}"

        # CAPTURA TOTAL DUE
        if (linha_limpa == "TOTAL" or linha_limpa == "TOTAL:") and (i + 1) < len(resultado):
            dados_extraidos["total_due"] = resultado[i + 1].strip()

    print(f" Dados extraídos com sucesso: {dados_extraidos}")
    print("*" * 50)


    return dados_extraidos

