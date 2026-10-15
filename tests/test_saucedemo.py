# Test de la pagina web para demos -saucedemo-
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


#informacion para compartir los driver en cada test, comunica el codigo con el navegador
@pytest.fixture(scope="module")
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

#verificar los titulos
def test_02A_verificar_titulo_ventana(driver):

    page_titel= driver.title

    assert page_titel == "Swag Labs" , "ERROR: El titulo de la ventana no es 'Swag Labs'."

def test_02B_verificar_titulo_section(driver):

    section_titel= driver.find_element(By.CLASS_NAME, 'title').text

    assert section_titel == "Products" , "ERROR: El titulo de la secion no es 'Products'."

#comprobar existencia de productos en pagina
def test_03_comprobar_elementos(driver):
    inventario_items = driver.find_elements(By.CLASS_NAME, 'inventory_list') #busca un contenedor padre con varios elementos
    #comprueba si el contenedor tiene elementos.
    assert len(inventario_items) > 0 , "ERROR: no se encontro productos visibles"

#validar elementos importantes en interfas
def test_04_comprobar_interfaz(driver):

    menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    bar_filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')

    assert menu_button.is_displayed , "ERROR: el menu no esta visible"
    assert bar_filtro.is_displayed , "ERROR: el filtro no esta visible"

def test_05_agregar_producto_carrito(driver):

    first_item= driver.find_elements(By.CLASS_NAME, 'inventory_item')[0]

    boton_agregar= first_item.find_element(By.TAG_NAME, 'button')
    boton_agregar.click()

    assert boton_agregar.text.capitalize() == 'Remove' , 'ERROR: el boton no cambio a "Remove"'

 