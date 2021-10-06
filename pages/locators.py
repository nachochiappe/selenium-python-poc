from selenium.webdriver.common.by import By

class BnaMainPageLocators(object):

    BOTON_SOLICITUD_TURNOS = (By.LINK_TEXT, 'Solicitud de Turnos')

class AtencionEnSucursalesPageLocators(object):

    HEADER = (By.XPATH, '//*[@id="titulo"]/h1')
    LINK_TURNOS_PARA_ATENCION = (By.XPATH, '//*[@id="contenidoMicroView"]/div/ul/li[2]/a/div/h2')

class TurnoParaAtencionEnSucursalesPageLocators(object):

    HEADER = (By.XPATH, '//*[@id="titulo"]/h1')
    BOTON_SOLICITAR_TURNO = (By.LINK_TEXT, "Solicitar Turno")
    
class SolicitarTurnosPageLocators(object):

    HEADER = (By.XPATH, '//*[@id="contenidoInternaLayout"]/h1')
    CUIL = (By.ID, 'numeroClaveTributariaId')
    EMAIL = (By.ID, 'idMail')
    PREFIJO = (By.ID, 'Prefijo')
    TELEFONO = (By.ID, 'Telefono')
    BOTON_CONTINUAR = (By.ID, 'buttonValidarCUIL')