from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def obtener_clima(ciudad):
    """
    Busca el clima de una ciudad utilizando Selenium.
    """
    options = Options()
    options.add_argument("--headless")  # Ejecutar sin abrir el navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Navegar al sitio de búsqueda
    driver.get(f"https://www.google.com/search?q=clima+{ciudad}")

    try:
        # Localizar la información del clima
        temperatura = driver.find_element(By.ID, "wob_tm").text
        condicion = driver.find_element(By.ID, "wob_dc").text
        driver.quit()
        return f"El clima en {ciudad} es de {temperatura}°C con {condicion}."
    except Exception as e:
        driver.quit()
        return f"No se pudo obtener el clima de {ciudad}: {e}"
