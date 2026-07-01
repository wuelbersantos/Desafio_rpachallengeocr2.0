import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PASTA_FATURAS = os.path.join(BASE_DIR, "faturas")
NOME_ARQUIVO_CSV = "resultado_desafio.csv"
CAMINHO_CSV_FINAL = os.path.join(PASTA_FATURAS, NOME_ARQUIVO_CSV)


SELETORES = {
    "tabela_sandbox": "tableSandbox",  #Espera tabela
    "linhas_tabela": "//table[@id='tableSandbox']/tbody/tr",  # Todas as linhas da tabela
    "coluna_id": "./td[2]",
    "coluna_due_date": "./td[3]",
    "link_download": "./td[4]/a"
}

URL_DESAFIO = "https://rpachallengeocr.azurewebsites.net/"
TIMEOUT_PADRAO = 10  # Tempo máximo de espera do WebDriverWait

IDIOMAS_OCR = ['en', 'pt']
USAR_GPU = False
