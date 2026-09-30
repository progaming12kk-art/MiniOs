class CPU:
    def __init__(self, programa):
        self.programa = [programa[i:i+32] for i in range(0, len(programa), 32)]
        self.memoria = [0] * 64
        self.pc = 0
        self.muerto = False


    def actualizar(self):
        instruccion = self.programa[self.pc]

        self.opcode = instruccion[0:4]
        self.argumento1 = int(instruccion[4:8], 2)
        self.argumento2 = int(instruccion[8:12], 2)
        self.argumento3 = int(instruccion[12:16], 2)


    def suma(self):
        self.actualizar()
        self.memoria[self.argumento3] = self.memoria[self.argumento1] + self.memoria[self.argumento2]


    def resta(self):
        self.actualizar()
        self.memoria[self.argumento3] = self.memoria[self.argumento1] - self.memoria[self.argumento2]


    def mult(self):
        self.actualizar()
        self.memoria[self.argumento3] = self.memoria[self.argumento1] * self.memoria[self.argumento2]


    def div(self):
        self.actualizar()
        if self.memoria[self.argumento2] != 0:
            self.memoria[self.argumento3] = self.memoria[self.argumento1] // self.memoria[self.argumento2]


    def mod(self):
        self.actualizar()
        if self.memoria[self.argumento2] != 0:
            self.memoria[self.argumento3] = self.memoria[self.argumento1] % self.memoria[self.argumento2]


    def load(self):
        self.actualizar()
        self.memoria[self.argumento1] = self.argumento2


    def store(self):
        self.actualizar()
        self.memoria[self.argumento2] = self.memoria[self.argumento1]


    def jump(self):
        self.actualizar()
        self.pc = self.argumento1
        self.saltar = True


    def halt(self):
        self.muerto = True


    def ejecutar(self):
        while not self.muerto and self.pc < len(self.programa):
            opcodes = {
                "0001": self.suma,
                "0010": self.resta,
                "0011": self.mult,
                "0100": self.div,
                "0101": self.mod,
                "0110": self.load,
                "0111": self.store,
                "1000": self.jump,
            }

            instruccion_actual = self.programa[self.pc]
            self.opcode = instruccion_actual[0:4]
            self.saltar = False

            if self.opcode in opcodes:
                opcodes[self.opcode]()
            elif self.opcode == "0000":
                self.halt()

            if not self.saltar:
                self.pc += 1
            print(self.memoria)