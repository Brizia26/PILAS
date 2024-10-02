import matplotlib.pyplot as plt

class Pila:
    def __init__(self, max_size):
        self.pila = []
        self.max_size = max_size

    # Método para agregar un elemento a la pila
    def apilar(self, elemento):
        if len(self.pila) < self.max_size:
            self.pila.append(elemento)
            print(f"{elemento} apilado.")
        else:
            print("La pila está llena, no se puede agregar más elementos.")
        self.graficar()

    # Método para eliminar un elemento según la posición dada por el usuario
    def desapilar_por_posicion(self, posicion):
        if not self.esta_vacia():
            if 0 <= posicion < len(self.pila):
                elemento = self.pila.pop(posicion)
                print(f"Elemento en la posición {posicion} ({elemento}) desapilado.")
            else:
                print("Posición inválida.")
        else:
            print("La pila está vacía, no se puede desapilar.")
        self.graficar()

    # Método para verificar si la pila está vacía
    def esta_vacia(self):
        return len(self.pila) == 0

    # Método para verificar si la pila está llena
    def esta_llena(self):
        return len(self.pila) == self.max_size

    # Método para mostrar el contenido de la pila
    def mostrar(self):
        print("Pila actual:", self.pila)

    # Método para graficar la pila
    def graficar(self):
        plt.figure(figsize=(5, 5))
        plt.barh(range(len(self.pila)), self.pila, color='skyblue')
        plt.yticks(range(len(self.pila)), [f"Elemento {i}" for i in range(len(self.pila)-1, -1, -1)])
        plt.xlabel("Valor del elemento")
        plt.ylabel("Posiciones en la pila")
        plt.title("Visualización de la Pila")
        plt.gca().invert_yaxis()  # Invertimos el eje Y para que el último elemento agregado esté arriba
        plt.show()

# Función principal
def main():
    max_size = int(input("Ingrese el tamaño máximo de la pila: "))
    mi_pila = Pila(max_size)

    while True:
        print("\n--- Menú ---")
        print("1. Apilar un elemento")
        print("2. Desapilar un elemento por posición")
        print("3. Mostrar la pila")
        print("4. Verificar si la pila está vacía")
        print("5. Verificar si la pila está llena")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if mi_pila.esta_llena():
                print("La pila está llena, no puedes agregar más elementos.")
            else:
                elemento = int(input("Ingrese el elemento a apilar (número): "))
                mi_pila.apilar(elemento)

        elif opcion == "2":
            if mi_pila.esta_vacia():
                print("La pila está vacía, no puedes desapilar elementos.")
            else:
                posicion = int(input(f"Ingrese la posición del elemento a desapilar (0 a {len(mi_pila.pila) - 1}): "))
                mi_pila.desapilar_por_posicion(posicion)

        elif opcion == "3":
            mi_pila.mostrar()

        elif opcion == "4":
            if mi_pila.esta_vacia():
                print("La pila está vacía.")
            else:
                print("La pila no está vacía.")

        elif opcion == "5":
            if mi_pila.esta_llena():
                print("La pila está llena.")
            else:
                print("La pila no está llena.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
main()
