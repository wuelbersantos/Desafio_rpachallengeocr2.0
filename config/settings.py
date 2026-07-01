import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PASTA_FATURAS = os.path.join(BASE_DIR, "faturas")
NOME_ARQUIVO_CSV = "resultado_desafio.csv"
CAMINHO_CSV_FINAL = os.path.join(PASTA_FATURAS, NOME_ARQUIVO_CSV)


#SELETORES = {
#    "tabela_sandbox": "tableSandbox",  #Espera tabela
#    "linhas_tabela": "//table[@id='tableSandbox']/tbody/tr",  # Todas as linhas da tabela
#    "coluna_id": "/html/body/div/div/div[2]/div/div[1]/div[1]/table/tbody/tr[1]/td[2]",            # Relativo à linha atual
#    "coluna_due_date": "/html/body/div/div/div[2]/div/div[1]/div[1]/table/tbody/tr[1]/td[3]",      # Relativo à linha atual
#    "link_download": "/html/body/div/div/div[2]/div/div[1]/div[1]/table/tbody/tr[1]/td[4]/a"       # Relativo à linha atual
#}

SELETORES = {
    "tabela_sandbox": "tableSandbox",  #Espera tabela
    "linhas_tabela": "//table[@id='tableSandbox']/tbody/tr",  # Todas as linhas da tabela
    "coluna_id": "./td[2]",            # Relativo à linha atual
    "coluna_due_date": "./td[3]",      # Relativo à linha atual
    "link_download": "./td[4]/a"       # Relativo à linha atual
}

URL_DESAFIO = "https://rpachallengeocr.azurewebsites.net/"
TIMEOUT_PADRAO = 10  # Tempo máximo de espera do WebDriverWait

IDIOMAS_OCR = ['en', 'pt']
USAR_GPU = False
