#AXEL ARIEL CACH YAM
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class MyLinkedList:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._tamaño = 0
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def tamaño(self):
        return self._tamaño
    
    def agregar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self._tamaño += 1
    
    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self._tamaño += 1
    
    def insertar(self, indice, dato):
        if indice < 0 or indice > self._tamaño:
            raise IndexError(f"Índice {indice} fuera de rango")
        if indice == 0:
            self.agregar_inicio(dato)
        elif indice == self._tamaño:
            self.agregar_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range(indice - 1):
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            self._tamaño += 1
    
    def eliminar(self, dato):
        if self.esta_vacia():
            return False
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is None:
                self.cola = None
            self._tamaño -= 1
            return True
        
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente
        if actual.siguiente and actual.siguiente.dato == dato:
            if actual.siguiente == self.cola:
                self.cola = actual
            actual.siguiente = actual.siguiente.siguiente
            self._tamaño -= 1
            return True
        return False
    
    def eliminar_en(self, indice):
        if indice < 0 or indice >= self._tamaño:
            raise IndexError(f"Índice {indice} fuera de rango")
        
        if indice == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is None:
                self.cola = None
            self._tamaño -= 1
            return dato
        
        actual = self.cabeza
        for _ in range(indice - 1):
            actual = actual.siguiente
        dato = actual.siguiente.dato
        if actual.siguiente == self.cola:
            self.cola = actual
        actual.siguiente = actual.siguiente.siguiente
        self._tamaño -= 1
        return dato
    
    def obtener(self, indice):
        if indice < 0 or indice >= self._tamaño:
            raise IndexError(f"Índice {indice} fuera de rango")
        actual = self.cabeza
        for _ in range(indice):
            actual = actual.siguiente
        return actual.dato
    
    def establecer(self, indice, dato):
        if indice < 0 or indice >= self._tamaño:
            raise IndexError(f"Índice {indice} fuera de rango")
        actual = self.cabeza
        for _ in range(indice):
            actual = actual.siguiente
        actual.dato = dato
        
    def indice_de(self, dato):
        actual = self.cabeza
        indice = 0
        while actual:
            if actual.dato == dato:
                return indice
            actual = actual.siguiente
            indice += 1
        return -1
    
    def contiene(self, dato):
        return self.indice_de(dato) != -1
    
    def limpiar(self):
        self.cabeza = None
        self.cola = None
        self._tamaño = 0
    
    def a_lista(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def invertir(self):
        if self._tamaño <= 1:
            return
        anterior = None
        actual = self.cabeza
        self.cola = self.cabeza
        while actual:
            siguiente_nodo = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente_nodo
        self.cabeza = anterior
    
    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos) + " -> None"
    
    def __len__(self):
        return self._tamaño
    
    def __getitem__(self, indice):
        return self.obtener(indice)
    
    def __setitem__(self, indice, valor):
        self.establecer(indice, valor)
    
    def __contains__(self, dato):
        return self.contiene(dato)
    
    def __iter__(self):
        self._actual = self.cabeza
        return self
    
    def __next__(self):
        if self._actual is None:
            raise StopIteration
        dato = self._actual.dato
        self._actual = self._actual.siguiente
        return dato