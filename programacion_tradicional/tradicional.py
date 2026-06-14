# tradicional.py
# Programa de gestión de mascotas con Programación Tradicional
# No se utilizan clases ni objetos, solo funciones y variables.

def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")
    return nombre, especie, edad

def mostrar_mascota(nombre, especie, edad):
    print("\n--- Información de la Mascota ---")
    print(f"Nombre : {nombre}")
    print(f"Especie: {especie}")
    print(f"Edad   : {edad} años")

# Programa principal
if __name__ == "__main__":
    nombre, especie, edad = registrar_mascota()
    mostrar_mascota(nombre, especie, edad)
