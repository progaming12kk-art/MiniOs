class Colores:
    def __init__(self):
        self.EXTENCION = "\033["
        self.gris = self.EXTENCION + "90m"
        self.rojo = self.EXTENCION + "91m"
        self.verde = self.EXTENCION + "92m"
        self.amarillo = self.EXTENCION + "93m"
        self.azul = self.EXTENCION + "94m"
        self.rosa = self.EXTENCION + "95m"
        self.cian = self.EXTENCION + "96m"
        self.gruesa = self.EXTENCION + "1m"
        self.reset = self.EXTENCION + "0m"
        self.subrallado = self.EXTENCION + "7m"