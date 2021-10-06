"""Test de solicitud de Turnos Web en testbna.bna.com.ar"""

from pages.page import BnaMainPage, AtencionEnSucursalesPage, TurnoParaAtencionEnSucursalesPage, SolicitarTurnosPage, ConfirmacionTurnoPage

def test_solicitud_turno_web(browser):
    bna_main_page = BnaMainPage(browser)
    atencion_en_sucursales_page = AtencionEnSucursalesPage(browser)
    turno_para_atencion_en_sucursales_page = TurnoParaAtencionEnSucursalesPage(browser)
    solicitar_turnos_page = SolicitarTurnosPage(browser)
    confirmacion_turno_page = ConfirmacionTurnoPage(browser)

    bna_main_page.load()
    bna_main_page.ir_a_solicitud_de_turno()

    # Cargo el link correcto porque apunta a Producción
    # Esto debe sacarse una vez corregido el desarrollo

    atencion_en_sucursales_page.cargar_link_correcto()
    atencion_en_sucursales_page.ir_a_link_turnos()

    turno_para_atencion_en_sucursales_page.ir_a_boton_solicitar_turno()

    solicitar_turnos_page.completar_campos('23345217819', 'banconacion.adlc@gmail.com', '011', '44445555')
    solicitar_turnos_page.continuar_solicitud()
    solicitar_turnos_page.seleccionar_sucursal('Mataderos', 'NUEVA CHICAGO')
    solicitar_turnos_page.seleccionar_plataforma_servicio('Operaciones de Caja', 'DEPOSITO/EXTRACCION MON.EXTRANJERA')
    solicitar_turnos_page.seleccionar_fecha_hora()
    # Wait until user enter Captcha
    input("Press ENTER after filling CAPTCHA")
    solicitar_turnos_page.solicitar_turno()
    solicitar_turnos_page.confirmar_turno()
    header_confirmacion = confirmacion_turno_page.get_header()
    assert header_confirmacion == '¡Ya tenés tu turno web!'