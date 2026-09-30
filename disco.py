class Disco:
    def __init__(self):
        self.memoria = []
        self.archivos = {}


    def hash_nombre(self, nombre):
        total = 0
        for i, letra in enumerate(nombre):
            total += ord(letra) * (256 ** i)
        return total


    def detectar_tipo(self, nombre):
        if nombre.endswith(".txt"):
            return 505
        elif nombre.endswith(".png"):
            return 606
        elif nombre.endswith(".py"):
            return 707
        elif nombre.endswith(".asm"):
            return 808
        else:
            return 404


    def crear(self, nombre, datos):
        tipo = self.detectar_tipo(nombre)
        hash_nombre = self.hash_nombre(nombre)
        longitud = len(datos)

        if hash_nombre in self.archivos:
            self.borrar(nombre)

        inicio = len(self.memoria)

        self.memoria.append(tipo)
        self.memoria.append(longitud)
        self.memoria.append(hash_nombre)
        self.memoria.extend(datos)

        self.archivos[hash_nombre] = {
            "nombre": nombre,
            "inicio": inicio,
            "longitud": longitud,
        }


    def leer(self, nombre):
        hash_nombre = self.hash_nombre(nombre)

        if hash_nombre not in self.archivos:
            return None

        info = self.archivos[hash_nombre]
        inicio = info["inicio"] + 3
        longitud = info["longitud"]

        return bytes(self.memoria[inicio:inicio + longitud])


    def borrar(self, nombre):
        if self.hash_nombre(nombre) in self.archivos:
            archivo = self.archivos[self.hash_nombre(nombre)]
            longitud = archivo["longitud"]
            inicio = archivo["inicio"]
            bloque = longitud + 3

            del self.memoria[inicio:inicio + bloque]

            for info in self.archivos.values():
                if info["inicio"] > inicio:
                    info["inicio"] -= bloque

            del self.archivos[self.hash_nombre(nombre)]


    def listar(self):
        for info in self.archivos.values():
            print(info["nombre"])