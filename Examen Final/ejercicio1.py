class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
        self.ant = None

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.cola = None
    #metodo para agregar al final de la Lista
    def agregarFinal(self, dato):
        nodo = Nodo(dato)
        if len(self) == 0:
            self.primero = self.cola = nodo
        else:
            aux = self.cola
            self.cola = aux.sig = nodo
            self.cola.ant = aux
    #metodo para Eliminar al inicio de la Lista
    def eliminarInicio(self):
        if len(self) == 0:
            pass
        elif self.primero.sig == None:
            self.primero = self.cola = None
        else:
            self.primero = self.primero.sig
            self.primero.ant = None

    def buscarNodo(self, dato):
        existe = False
        aux = self.primero
        while aux != None:
            if aux.dato == dato:
                existe = True
                break
            aux = aux.sig
        return existe
    
    def reemplazarNodo(self, anterior, nuevoDato):
        if self.buscarNodo(anterior):
            aux = self.primero
            while aux != None:
                if aux.dato == anterior:
                    aux.dato = nuevoDato
                    break
                aux = aux.sig

    def __len__(self):
        aux = self.primero
        count = 0
        while aux != None:
            count += 1
            aux = aux.sig
        return count
    
    def recorrerInicio(self):
        aux = self.primero

        while aux != None:
            print(aux.dato)
            aux = aux.sig
    
    def recorrerFinal(self):
        aux = self.cola
        while aux != None:
            print(aux.dato)
            aux = aux.ant
    
    def __str__(self) -> str:
        aux = self.primero
        datos = "----------------Lista de Compras---------------- \n "
        while aux != None:
            datos += str(aux.dato) + " \n "
            aux = aux.sig
        datos += "----------------Fin de la lista de compras----------------"
        return datos
    
    def __getitem__(self, indice):
        if indice >= 0 and indice < len(self):
            actual = self.primero
            for i in range(indice):
                actual = actual.sig

            return actual.dato
        elif indice <= -1 and indice >= -len(self):
            actual = self.cola

            for i in range(indice*(-1)-1):
                actual = actual.ant
            return actual.dato
        else:
            raise IndexError ("Indice fuera de rango")

def lista_Opciones(lista):
    valor = True
    while valor :
        print("""
        Opciones para lista ::::
        1: Agregar producto final
        2: Eliminar producto inicio
        3: Verificar si esta lista de productos vacia
        4: Ver lista
        5: Salir
        """)

        opcion = int(input("- Seleccione una opcion : "))
        if opcion == 1:
            dato = str(input("Ingrese un producto : "))
            lista.agregarFinal(dato)
        elif opcion == 2:
            lista.eliminarInicio() #elimina el primer nodo
        elif opcion==3:
            if(len(lista))==0:
                print("Esta vacia")
            else:
                print("No esta vacia ")
        elif opcion==4:
            print(" Esta es la lista de datos que se estan guardando")
            print(lista)
        elif opcion ==5:
            print("Hemos salido ;-;  ")
            valor = False
        else:
            print("Esa ocion no esta permitida")

ls = ListaDoble() #instanciando
lista_Opciones(ls)
