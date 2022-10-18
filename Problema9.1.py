"""
Problema número 9.1

Escribir un método, copiarPila(), que copie el contenido de una pila en otra. El
método tendrá dos argumentos de tipo pila, uno para la pila fuente y otro para la pila
destino. Utilizar las operaciones definidas sobre el TAD Pila.

Pág.317, del libro "Estructura de datos" (Luis Joyanes Aguilar, Ignacio Zahonero Martínez, 2008)

"""


# clase donde se hace uso de las operaciones de una pila dinámica
class PilaDinamica:
    def __init__(self):
        self.__listaPila = []

    # Este método inserta un nuevo elemento a la pila
    def insertar(self, elemento):
        self.__listaPila.append(elemento)

    # Este método quita el último elemento agregado a la pila
    def quitar(self):
        if self.pilaVacia():
            return False
        else:
            elemento = self.__listaPila.pop()
            return elemento

    # Este método cuenta la cantidad de elementos de la pila a través de un "len" y si es igual a cero retorna
    # Verdadero y si esta vacía retorna Falso
    def pilaVacia(self):
        if len(self.__listaPila) == 0:
            return True
        else:
            return False

    # Este método cuenta la cantidad de elementos de la pila a través de un "len" e imprime la cantidad
    def tamPila(self):
        print("La pila tiene", len(self.__listaPila), "elementos")

    # Este método usa "clear" para eliminar todos los elementos que existan en la pila
    def limpiarPila(self):
        self.__listaPila.clear()

    # Se debe implementar el método __str__ para retornar un string, asi "listaPila" será mostrado en
    # pantalla de manera legible
    def __str__(self):
        return str(self.__listaPila)


# Este método usa los valores insertados en la clase "PilaDinamica" y también usa a la misma clase para agregar
# elementos a la "pilaDestino", después de quitarlos a la "pilaFuente" mediante un ciclo "While", que
# se ejecuta mientras la "pilaFuente" no este vacia
def copiarInvertida(pilaFuente):
    pilaDestino = PilaDinamica()
    while not pilaFuente.pilaVacia():
        pilaDestino.insertar(pilaFuente.quitar())
    return pilaDestino

# Método copiarPila
# Este método usa los resultados del método "copiarInvertida" y también hace lo mismo por lo que retorna una
# pila en el orden exacto que la "pilaFuente"
def copiarPila(pilaFuente):
    pilaDestino = PilaDinamica()
    while not pilaFuente.pilaVacia():
        pilaDestino.insertar(pilaFuente.quitar())
    return pilaDestino


pi = PilaDinamica()  # instancia
print("-----------------Pila-Fuente-------------------")
# se insertan elementos del 1 al 9
pi.insertar(1)
pi.insertar(2)
pi.insertar(3)
pi.insertar(4)
pi.insertar(5)
pi.insertar(6)
pi.insertar(7)
pi.insertar(8)
pi.insertar(9)

# se imprime
print(pi)

# Método que indica el tamaño
# print("\n-tamaño-")
# pi.tamPila()

# print("\n-método-para-quitar-")
# pi.quitar()
# print(pi)

# print("-método-que-limpia-la-pila-")
# pi.limpiarPila()

#print("\n(-Pila-Copiada-Invertida-)")
#p1 = copiarInvertida(pi)
#print(p1)

# copia de la pila fuente y en el mismo orden
print("\n-----------------Pila-Copiada-en-el-mismo-orden-----------------")
p2 = copiarPila(p1)
print(p2)


