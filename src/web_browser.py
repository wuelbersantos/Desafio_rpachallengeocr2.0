from selenium import webdriver #importar selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def inicializar_navegador():

    chrome_opions= Options()

    chrome_opions.add_argument("--start-maximized")#iniciar com tela maximizada
    chrome_opions.add_argument("--disable-blink-features=AutomationControlled")#evitar bloqueios
    chrome_opions.add_experimental_option("excludeSwitches", ["enable-automation"])#remover cabeçalhos para nao identifcar que é um robo
    chrome_opions.add_experimental_option('useAutomationExtension', False) #nao executar exntesao

    driver = webdriver.Chrome(chrome_opions)

    return driver

def FecharNagevador(driver):
    if driver:
        try:
            driver.quit()
            print(f"Navegador encerrado com sucesso")
        except Exception as e:
            print(f" Falha ao fechar navegador")