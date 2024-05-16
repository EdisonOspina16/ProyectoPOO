class SistemaExcepcion(Exception):
    """Clase base para excepciones en el sistema."""

    def __init__(self, mensaje="Error en el sistema"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

    def obtener_mensaje(self):
        return self.mensaje


class MeseroExistenteError(SistemaExcepcion):
    """Excepción lanzada cuando se intenta registrar un mesero que ya existe."""

    def __init__(self, mensaje="El mesero ya está registrado"):
        super().__init__(mensaje)


class HorarioInvalidoError(SistemaExcepcion):
    """Excepción lanzada cuando se produce un error en la asignación de horarios."""

    def __init__(self, mensaje="Error en la asignación de horarios"):
        super().__init__(mensaje)


class AgendaNoDisponibleError(SistemaExcepcion):
    """Excepción lanzada cuando la agenda de horarios no está disponible."""

    def __init__(self, mensaje="La agenda de horarios no está disponible"):
        super().__init__(mensaje)


class NotificacionError(SistemaExcepcion):
    """Excepción lanzada cuando se produce un error en el proceso de notificación."""

    def __init__(self, mensaje="Error en la notificación"):
        super().__init__(mensaje)