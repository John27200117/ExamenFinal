class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaTareas:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cantidad_tareas = 0

    def agregar_tarea(self, tarea):
        nodo_nuevo = Nodo(tarea)

        if self.primero is None:
            self.primero = nodo_nuevo
            self.ultimo = nodo_nuevo
        else:
            nodo_nuevo.siguiente = self.primero
            self.primero = nodo_nuevo

        self.cantidad_tareas += 1

    def eliminar_tarea(self):
        if self.primero is None:
            print("No hay tareas pendientes.")
        elif self.primero == self.ultimo:
            tarea_eliminada = self.primero.valor
            self.primero = None
            self.ultimo = None
            self.cantidad_tareas -= 1
            return tarea_eliminada
        else:
            nodo_actual = self.primero
            while nodo_actual.siguiente != self.ultimo:
                nodo_actual = nodo_actual.siguiente

            tarea_eliminada = self.ultimo.valor
            nodo_actual.siguiente = None
            self.ultimo = nodo_actual
            self.cantidad_tareas -= 1
            return tarea_eliminada

    def mostrar_tareas(self):
        if self.primero is None:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            nodo_actual = self.primero
            while nodo_actual is not None:
                print(nodo_actual.valor)
                nodo_actual = nodo_actual.siguiente

    def mostrar_cantidad_tareas(self):
        print(f"Hay {self.cantidad_tareas} tareas pendientes.")

lista_tareas = ListaTareas()

while True:
    print("-------------------------------Menu-------------------------------")
    print("¿Qué quieres hacer?")
    print("1 - Agregar una tarea al inicio de la lista")
    print("2 - Eliminar una tarea del final de la lista")
    print("3 - Mostrar todas las tareas en orden inverso al que se agregaron")
    print("4 - Mostrar la cantidad total de tareas en la lista")
    print("5 - Salir del programa")

    opcion = input("Ingresa el número de la opción que deseas: ")

    if opcion == "1":
        tarea = input("Ingresa la tarea que deseas agregar: ")
        lista_tareas.agregar_tarea(tarea)
        print(f"{tarea} ha sido agregada a la lista de tareas.")
    elif opcion == "2":
        tarea_eliminada = lista_tareas.eliminar_tarea()
        if tarea_eliminada is not None:
            print(f"{tarea_eliminada} ha sido eliminada de la lista de tareas.")
    elif opcion == "3":
        lista_tareas.mostrar_tareas()
    elif opcion == "4":
        lista_tareas.mostrar_cantidad_tareas()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor ingresa un número del 1 al 5.")
