class Ensamblador:
    def __init__(self):
        pass


    def ensamblar(self, comando):
        resultado = ""
        self.comando = comando.replace(";", " ; ").split()

        assembly = {
            "SUMA": "0001",
            "RESTA": "0010",
            "MULTI": "0011",
            "DIV": "0100",
            "MOD": "0101",
            "LOAD": "0110",
            "STORE": "0111",
            "JUMP": "1000",
        }

        for intrucion in self.comando:
            if intrucion in assembly:
                resultado += assembly[intrucion]
            else:
                if intrucion.isdigit():
                    resultado += bin(int(intrucion))[2:].zfill(4)
                elif intrucion == ";":
                    resultado += "0000"

        return resultado.ljust(32, "0")