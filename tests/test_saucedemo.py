# Test de la pagina web para demos -saucedemo-
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


#informacion para compartir los driver en cada test, comunica el codigo con el navegador
@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    yield driver

    driver.quit()



#Ingresa al login, carga los datos de usuario, hace click y verifica la pagina objetivo
def test_01_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "/inventory.html" in driver.current_url , "ERROR: No se redirigir a la pagina objetivo."