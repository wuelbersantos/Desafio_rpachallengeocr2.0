from web_scraper import acessar_pagina_desafio
from web_scraper import raspar_dados_tabela
from web_scraper import baixar_fatura_local
from ocr_processor import extrairDadosFaturas
from web_browser import inicializar_navegador, FecharNagevador
from data_handler import salvar_dados_em_csv





if __name__ == "__main__":
    driver=inicializar_navegador()
    acessar_pagina_desafio(driver)
    faturas_encontradas=raspar_dados_tabela(driver)
    print(faturas_encontradas)
    lista_resultados_finais = []

    for fatura in faturas_encontradas:

        caminho_imagem = baixar_fatura_local(fatura["url_fatura"], fatura["nome_arquivo"])

        if caminho_imagem:
            print(f"pronto para executar OCR {caminho_imagem}")
            dados_extraidos = extrairDadosFaturas(caminho_imagem=caminho_imagem,
                                                  id_fatura=fatura["id_fatura"],
                                                  due_date=fatura["due_date"])

            if dados_extraidos:
                lista_resultados_finais.append(dados_extraidos)

    FecharNagevador(driver)

    salvar_dados_em_csv(lista_resultados_finais)



    for i in range(len(lista_resultados_finais)):
       # print(f" item {i} id {dados_extraidos["total_due"]} ")
        print(f"dados: {i+1} {lista_resultados_finais[i]}")
        print(f"*" * 50)
        #dados_extraidosdados_extraidos["total_due"]



    ##print(lista_resultados_finais)






