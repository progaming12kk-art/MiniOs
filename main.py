from colores import Colores
from disco import Disco
from ejecutor import Ejecutor


def main():
    color = Colores()
    disco = Disco()

    print("--- Mini OS v1.0 ---")
    print("Comandos: listar, escribir, leer, borrar, ejecutar, salir\n")

    while True:
        try:
            comando = input(color.verde + "~ " + color.reset + "$ ")
            if comando.strip().lower() == "salir":
                break

            terminal = Ejecutor(comando, disco)
            terminal.ejecutar()

        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo...")
            break


if __name__ == "__main__":
    main()