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
    RADIO_CABA = (By.ID, 'capitalFederalRadio')
    RADIO_PROV = (By.ID, 'provinciasRadio')
    DROPDOWN_BARRIO = (By.ID, 'branchTownDropDown')
    DROPDOWN_SUCURSAL = (By.ID, 'branchDropDown')
    DROPDOWN_PLATAFORMA = (By.ID, 'PlataformasID')
    DROPDOWN_SERVICIO = (By.ID, 'ServicioID')
    CALENDARIO = (By.ID, 'divDatePicker')
    MES_PREVIO = (By.CLASS_NAME, 'ui-datepicker-prev ui-corner-all')
    MES_SIGUIENTE = (By.CLASS_NAME, 'ui-datepicker-next ui-corner-all')
    DROPDOWN_MES = (By.CLASS_NAME, 'ui-datepicker-month valid')
    DROPDOWN_ANIO = (By.CLASS_NAME, 'ui-datepicker-year')
    DIA_DISPONIBLE = (By.XPATH, "//td[@title='Disponible']")
    HORARIO_DISPONIBLE = (By.ID, '1-hora')
    CAPTCHA = (By.ID, 'captchaInput')
    BOTON_SOLICITAR_TURNO = (By.ID, 'btn_product_request_submit')
    BOTON_CONFIRMAR_TURNO = (By.XPATH, '//*[@id="modalConfirmacion"]/div/div/div[3]/button[1]')
    BOTON_CANCELAR_TURNO = (By.XPATH, '//*[@id="modalConfirmacion"]/div/div/div[3]/button[2]')

class ConfirmacionTurnoPageLocators(object):

    HEADER_CONFIRMACION = (By.XPATH, '//*[@id="contenidoInternaLayout"]/h1')
    