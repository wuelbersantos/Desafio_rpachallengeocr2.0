import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import URL_DESAFIO, TIMEOUT_PADRAO, SELETORES, PASTA_FATURAS

def acessar_pagina_desafio(driver):
    try:
        print(f"Acessando a pagina {URL_DESAFIO}")

        driver.get(URL_DESAFIO)

        wait = WebDriverWait(driver,TIMEOUT_PADRAO)

        wait.until(EC.presence_of_element_located((By.ID, SELETORES["tabela_sandbox"])))
        print(f"Tabela carregada e pronto para Scraping")
        return True

    except Exception as e:
        print(f"error falha ao acessar a pagina do desafio {e}")
        return False


def raspar_dados_tabela(driver):
    lista_faturas_web = []

    try:

        linhas = driver.find_elements(By.XPATH, SELETORES["linhas_tabela"])
        print(f" Encontradas {len(linhas)} linhas na tabela para processar.")

        for linha in linhas:
            id_fatura = linha.find_element(By.XPATH, SELETORES["coluna_id"]).text.strip()
            due_date = linha.find_element(By.XPATH, SELETORES["coluna_due_date"]).text.strip()
            url_fatura = linha.find_element(By.XPATH, SELETORES["link_download"]).get_attribute("href")
            nome_arquivo = url_fatura.split("/")[-1]


            dados_item = {
                "id_fatura": id_fatura,
                "due_date": due_date,
                "url_fatura": url_fatura,
                "nome_arquivo": nome_arquivo
            }
            lista_faturas_web.append(dados_item)

        return lista_faturas_web
    except Exception as e:
        print(f"ERRO Falha ao raspar os dados da tabela: {e}")
        return []

def baixar_fatura_local(url_fatura, nome_arquivo):

    # Garante que a pasta destino existe
    if not os.path.exists(PASTA_FATURAS):
        os.makedirs(PASTA_FATURAS)
        print(f"Pasta '{PASTA_FATURAS}' criada com sucesso.")

    caminho_completo = os.path.join(PASTA_FATURAS, nome_arquivo)
    print(f" Baixando: {url_fatura}")

    try:
        resposta = requests.get(url_fatura, stream=True, timeout=15)
        if resposta.status_code == 200:
            with open(caminho_completo, 'wb') as arquivo:
                for bloco in resposta.iter_content(chunk_size=1024):
                    arquivo.write(bloco)
            print(f" Salvo em: {caminho_completo}")
            return caminho_completo
        else:
            print(f" Falha no download. Status Code: {resposta.status_code}")
            return None
    except Exception as e:
        print(f"Erro ao conectar para o download: {e}")
        return None



