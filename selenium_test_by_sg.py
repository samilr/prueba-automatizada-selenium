from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar WebDriver (Asegúrate de tener el driver adecuado para tu navegador)
driver = webdriver.Chrome()

def test_wikipedia_search():
    try:
        # 1. Abrir Wikipedia
        driver.get("https://www.wikipedia.org")
        driver.maximize_window()
        time.sleep(2)
        
        # 2. Encontrar el cuadro de búsqueda y escribir "Python (programming language)"
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("Python (programming language)")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # 3. Verificar que la página de resultados cargó correctamente
        title = driver.find_element(By.ID, "firstHeading").text
        assert title == "Python (programming language)", f"Título esperado no encontrado: {title}"
        print("Prueba exitosa: La página de Wikipedia cargó correctamente con el término buscado.")
    
    except Exception as e:
        print(f"Prueba fallida: {e}")
    
    finally:
        # 4. Cerrar el navegador
        driver.quit()

# Ejecutar la prueba
test_wikipedia_search()


<h1 id="firstHeading" class="firstHeading mw-first-heading"><span class="mw-page-title-main">Python (programming language)</span></h1>