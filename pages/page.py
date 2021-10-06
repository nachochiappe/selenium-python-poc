from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
        self.driver.maximize_window()

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
    
    def seleccionar_sucursal(self, barrio, sucursal):
        self.find_element(*SolicitarTurnosPageLocators.RADIO_CABA).click()
        drpBarrio = Select(self.find_element(*SolicitarTurnosPageLocators.DROPDOWN_BARRIO))
        drpBarrio.select_by_visible_text(barrio)
        drpSucursal = Select(self.find_element(*SolicitarTurnosPageLocators.DROPDOWN_SUCURSAL))
        drpSucursal.select_by_visible_text(sucursal)

    def seleccionar_plataforma_servicio(self, plataforma, servicio):
        drpPlataforma = Select(self.find_element(*SolicitarTurnosPageLocators.DROPDOWN_PLATAFORMA))
        drpPlataforma.select_by_visible_text(plataforma)
        drpServicio = Select(self.find_element(*SolicitarTurnosPageLocators.DROPDOWN_SERVICIO))
        drpServicio.select_by_visible_text(servicio)

    def seleccionar_fecha_hora(self):
        self.find_element(*SolicitarTurnosPageLocators.DIA_DISPONIBLE).click()
        self.find_element(*SolicitarTurnosPageLocators.HORARIO_DISPONIBLE).click()
        
    def solicitar_turno(self):
        self.find_element(*SolicitarTurnosPageLocators.BOTON_SOLICITAR_TURNO).click()
    
    def confirmar_turno(self):
        self.find_element(*SolicitarTurnosPageLocators.BOTON_CONFIRMAR_TURNO).click()

class ConfirmacionTurnoPage(BasePage):

    def get_header(self):
        return self.find_element(*ConfirmacionTurnoPageLocators.HEADER_CONFIRMACION).text