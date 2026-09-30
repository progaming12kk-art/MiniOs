from colores import Colores
from ensamblador import Ensamblador
from cpu import CPU


class Ejecutor:
    def __init__(self, comando, disco):
        self.color = Colores()
        self.disco = disco
        self.partes = comando.strip().split()


    def unir(self, desde):
        resultado = ""
        dentro = False

        for palabra in self.partes[desde:]:
            if palabra == "{":
                dentro = True
                continue
            if palabra == "}":
                break
            if dentro:
                resultado += palabra + " "

        return resultado.strip()


    def ejecutar(self):
        if not self.partes:
            return
        cmd = self.partes[0].lower()

        if cmd == "ls":
            self.disco.listar()

        elif cmd == "write":
            nombre = self.partes[1]
            datos = self.unir(2).encode()
            self.disco.crear(nombre, datos)

        elif cmd == "remove":
            self.disco.borrar(self.partes[1])

        elif cmd == "cat":
            nombre = self.partes[1]
            datos = self.disco.leer(nombre)
            if datos:
                print(datos.decode())

        elif cmd == "execute":
            nombre = self.partes[1]
            datos = self.disco.leer(nombre)
            if not datos:
                print(self.color.rojo + "Archivo no encontrado")
                return
            binario_total = ""
            for dato in datos.decode().split("_"):
            	ensamblador = Ensamblador()
            	binario_total += ensamblador.ensamblar(dato.strip())
            cpu = CPU(binario_total)
            cpu.ejecutar()
