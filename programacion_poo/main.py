# main.py
# Programa principal que utiliza la clase Mascota

from mascota import Mascota

if __name__ == "__main__":
    # Crear dos objetos de la clase Mascota
    mascota1 = Mascota("Firulais", "Perro", 5)
    mascota2 = Mascota("Mishi", "Gato", 3)

    # Mostrar información y ejecutar métodos
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()

    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()

