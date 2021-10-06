from selenium.webdriver.common.by import By
from pages.locators import *

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

class BnaMainPage(BasePage):
    
    URL = 'https://testbna.bna.com.ar/'

    def load(self):
        self.driver.get(self.URL)

    def ir_a_solicitud_de_turno(self):
        boton_solicitud_turnos = self.find_element(*BnaMainPageLocators.BOTON_SOLICITUD_TURNOS)
        boton_solicitud_turnos.click()

class AtencionEnSucursalesPage(BasePage):

    URL_CORRECTA = 'https://testbna.bna.com.ar/Home/AtencionEnSucursales'
    
    def cargar_link_correcto(self):
        self.driver.get(self.URL_CORRECTA)

    def ir_a_link_turnos(self):
        self.find_element(*AtencionEnSucursalesPageLocators.LINK_TURNOS_PARA_ATENCION).click()

class TurnoParaAtencionEnSucursalesPage(BasePage):

    def ir_a_boton_solicitar_turno(self):
        self.find_element(*TurnoParaAtencionEnSucursalesPageLocators.BOTON_SOLICITAR_TURNO).click()

class SolicitarTurnosPage(BasePage):

    def completar_campos(self, cuil, email, prefijo, telefono):
        self.find_element(*SolicitarTurnosPageLocators.CUIL).send_keys(cuil)
        self.find_element(*SolicitarTurnosPageLocators.EMAIL).send_keys(email)
        self.find_element(*SolicitarTurnosPageLocators.PREFIJO).send_keys(prefijo)
        self.find_element(*SolicitarTurnosPageLocators.TELEFONO).send_keys(telefono)
        
    def continuar_solicitud(self):
        self.find_element(*SolicitarTurnosPageLocators.BOTON_CONTINUAR).click()