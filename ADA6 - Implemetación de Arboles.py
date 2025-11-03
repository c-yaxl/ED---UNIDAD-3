#Axel Ariel Cach Yam
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import os
import platform

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, datos=None):
        """Constructor del árbol binario"""
        self.raiz = None
        if datos:
            self.crear_desde_lista(datos)
    
    def crear_desde_lista(self, datos):
        """Crea un árbol desde una lista de datos"""
        if isinstance(datos, str):
            try:
                # Intentar convertir string a lista de números
                datos = [int(x.strip()) for x in datos.split(',')]
            except ValueError:
                return False, "Error: Los datos deben ser números separados por comas"
        
        for valor in datos:
            self.insertar_sin_mensaje(valor)
        return True, f"Árbol creado con {len(datos)} elementos"
    
    def crear_vacio(self):
        """Crea un árbol vacío"""
        self.raiz = None
        return True, "Árbol vacío creado"
    
    def insertar_sin_mensaje(self, valor):
        """Inserta sin retornar mensaje (para uso interno)"""
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo_sin_mensaje(self.raiz, valor)
    
    def _insertar_recursivo_sin_mensaje(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo_sin_mensaje(nodo_actual.izquierda, valor)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo_sin_mensaje(nodo_actual.derecha, valor)
    
    # [1] Insertar elemento
    def insertar(self, valor):
        """Inserta un elemento en el árbol"""
        try:
            valor = int(valor)
        except ValueError:
            return False, "Error: El valor debe ser un número entero"
        
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return True, f"Valor {valor} insertado como raíz"
        else:
            return self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
                return True, f"Valor {valor} insertado a la izquierda de {nodo_actual.valor}"
            else:
                return self._insertar_recursivo(nodo_actual.izquierda, valor)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
                return True, f"Valor {valor} insertado a la derecha de {nodo_actual.valor}"
            else:
                return self._insertar_recursivo(nodo_actual.derecha, valor)
    
    # [2] Mostrar árbol completo acostado
    def mostrar_arbol(self):
        """Muestra el árbol completo con la raíz a la izquierda"""
        if self.raiz:
            print("\n" + "="*50)
            print("REPRESENTACIÓN TEXTUAL DEL ÁRBOL")
            print("="*50)
            self._mostrar_recursivo(self.raiz, 0)
            print("="*50)
        else:
            print("El árbol está vacío")
    
    def _mostrar_recursivo(self, nodo, nivel):
        if nodo is not None:
            self._mostrar_recursivo(nodo.derecha, nivel + 1)
            print("    " * nivel + "-> " + str(nodo.valor))
            self._mostrar_recursivo(nodo.izquierda, nivel + 1)
    
    # [3] Graficar árbol completo
    def graficar_arbol(self, mostrar=True):
        """Grafica el árbol usando networkx y matplotlib"""
        if not self.raiz:
            if mostrar:
                print("El árbol está vacío - No hay nada que graficar")
            return False
        
        try:
            G = nx.DiGraph()
            posiciones = {}
            
            def agregar_nodos(nodo, x=0, y=0, nivel=0, espaciado=2):
                if nodo:
                    posiciones[nodo.valor] = (x, y)
                    G.add_node(nodo.valor)
                    
                    if nodo.izquierda:
                        G.add_edge(nodo.valor, nodo.izquierda.valor)
                        agregar_nodos(nodo.izquierda, x - espaciado/(nivel+1), 
                                     y - 1, nivel + 1, espaciado/1.5)
                    
                    if nodo.derecha:
                        G.add_edge(nodo.valor, nodo.derecha.valor)
                        agregar_nodos(nodo.derecha, x + espaciado/(nivel+1), 
                                     y - 1, nivel + 1, espaciado/1.5)
            
            agregar_nodos(self.raiz)
            
            plt.figure(figsize=(12, 8))
            nx.draw(G, posiciones, with_labels=True, node_size=2000, node_color='lightblue', 
                    font_size=10, font_weight='bold', arrows=False, edge_color='gray')
            plt.title("REPRESENTACIÓN GRÁFICA DEL ÁRBOL BINARIO", fontsize=14, fontweight='bold')
            plt.axis('off')
            if mostrar:
                plt.show()
            else:
                plt.close()
            return True
        except ImportError:
            if mostrar:
                print("Error: Para graficar necesita instalar matplotlib y networkx")
                print("Ejecute: pip install matplotlib networkx")
            return False
    
    # [4] Buscar un elemento en el árbol
    def buscar(self, valor):
        """Busca un elemento en el árbol"""
        try:
            valor = int(valor)
        except ValueError:
            return False, "Error: El valor debe ser un número entero"
        
        encontrado = self._buscar_recursivo(self.raiz, valor)
        if encontrado:
            return True, f"Valor {valor} encontrado en el árbol"
        else:
            return False, f"Valor {valor} no encontrado en el árbol"
    
    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)
    
    # [5] Recorrer el árbol en PreOrden
    def preorden(self):
        """Recorrido PreOrden: Raíz - Izquierda - Derecha"""
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _preorden_recursivo(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierda, resultado)
            self._preorden_recursivo(nodo.derecha, resultado)
    
    # [6] Recorrer el árbol en InOrden
    def inorden(self):
        """Recorrido InOrden: Izquierda - Raíz - Derecha"""
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecha, resultado)
    
    # [7] Recorrer el árbol en PostOrden
    def postorden(self):
        """Recorrido PostOrden: Izquierda - Derecha - Raíz"""
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _postorden_recursivo(self, nodo, resultado):
        if nodo:
            self._postorden_recursivo(nodo.izquierda, resultado)
            self._postorden_recursivo(nodo.derecha, resultado)
            resultado.append(nodo.valor)
    
    # [8] Eliminar un nodo del árbol PREDECESOR
    def eliminar_predecesor(self, valor):
        """Elimina un nodo usando el predecesor inorden"""
        try:
            valor = int(valor)
        except ValueError:
            return False, "Error: El valor debe ser un número entero"
        
        if not self._buscar_recursivo(self.raiz, valor):
            return False, f"Valor {valor} no existe en el árbol"
        
        self.raiz = self._eliminar_predecesor_recursivo(self.raiz, valor)
        return True, f"Valor {valor} eliminado usando predecesor"
    
    def _eliminar_predecesor_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_predecesor_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_predecesor_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            
            predecesor = self._encontrar_maximo(nodo.izquierda)
            nodo.valor = predecesor.valor
            nodo.izquierda = self._eliminar_predecesor_recursivo(nodo.izquierda, predecesor.valor)
        
        return nodo
    
    def _encontrar_maximo(self, nodo):
        while nodo.derecha:
            nodo = nodo.derecha
        return nodo
    
    # [9] Eliminar un nodo del árbol SUCESOR
    def eliminar_sucesor(self, valor):
        """Elimina un nodo usando el sucesor inorden"""
        try:
            valor = int(valor)
        except ValueError:
            return False, "Error: El valor debe ser un número entero"
        
        if not self._buscar_recursivo(self.raiz, valor):
            return False, f"Valor {valor} no existe en el árbol"
        
        self.raiz = self._eliminar_sucesor_recursivo(self.raiz, valor)
        return True, f"Valor {valor} eliminado usando sucesor"
    
    def _eliminar_sucesor_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_sucesor_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_sucesor_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            
            sucesor = self._encontrar_minimo(nodo.derecha)
            nodo.valor = sucesor.valor
            nodo.derecha = self._eliminar_sucesor_recursivo(nodo.derecha, sucesor.valor)
        
        return nodo
    
    def _encontrar_minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo
    
    # [10] Recorrer el árbol por niveles (Amplitud)
    def recorrido_por_niveles(self):
        """Recorrido por niveles (BFS)"""
        if not self.raiz:
            return []
        
        resultado = []
        cola = deque([self.raiz])
        
        while cola:
            nodo_actual = cola.popleft()
            resultado.append(nodo_actual.valor)
            
            if nodo_actual.izquierda:
                cola.append(nodo_actual.izquierda)
            if nodo_actual.derecha:
                cola.append(nodo_actual.derecha)
        
        return resultado
    
    # [11] Altura del árbol
    def altura(self):
        """Retorna la altura del árbol"""
        return self._altura_recursivo(self.raiz)
    
    def _altura_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura_recursivo(nodo.izquierda), 
                      self._altura_recursivo(nodo.derecha))
    
    # [12] Cantidad de hojas del árbol
    def contar_hojas(self):
        """Cuenta la cantidad de nodos hoja en el árbol"""
        return self._contar_hojas_recursivo(self.raiz)
    
    def _contar_hojas_recursivo(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        return (self._contar_hojas_recursivo(nodo.izquierda) + 
                self._contar_hojas_recursivo(nodo.derecha))
    
    # [13] Cantidad de nodos del árbol
    def contar_nodos(self):
        """Cuenta la cantidad total de nodos en el árbol"""
        return self._contar_nodos_recursivo(self.raiz)
    
    def _contar_nodos_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + (self._contar_nodos_recursivo(nodo.izquierda) + 
                   self._contar_nodos_recursivo(nodo.derecha))
    
    # [15] Revisa si es un árbol binario completo
    def es_completo(self):
        """Verifica si el árbol es completo"""
        if not self.raiz:
            return True
        
        cola = deque([self.raiz])
        nivel_incompleto = False
        
        while cola:
            nodo_actual = cola.popleft()
            
            if nodo_actual.izquierda:
                if nivel_incompleto:
                    return False
                cola.append(nodo_actual.izquierda)
            else:
                nivel_incompleto = True
            
            if nodo_actual.derecha:
                if nivel_incompleto:
                    return False
                cola.append(nodo_actual.derecha)
            else:
                nivel_incompleto = True
        
        return True
    
    # [16] Revisa si es un árbol binario lleno
    def es_lleno(self):
        """Verifica si el árbol es lleno"""
        return self._es_lleno_recursivo(self.raiz)
    
    def _es_lleno_recursivo(self, nodo):
        if nodo is None:
            return True
        
        if nodo.izquierda is None and nodo.derecha is None:
            return True
        
        if nodo.izquierda is not None and nodo.derecha is not None:
            return (self._es_lleno_recursivo(nodo.izquierda) and 
                   self._es_lleno_recursivo(nodo.derecha))
        
        return False
    
    # [17] Eliminar el árbol
    def eliminar_arbol(self):
        """Elimina todo el árbol"""
        self.raiz = None
        return True, "Árbol eliminado completamente"
    
    def estado_arbol(self):
        """Muestra el estado actual del árbol"""
        if self.raiz is None:
            return "Árbol: VACÍO"
        else:
            return f"Árbol: {self.contar_nodos()} nodos, Altura: {self.altura()}, Hojas: {self.contar_hojas()}"

def limpiar_consola():
    """Limpia la consola según el sistema operativo"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu(arbol):
    """Muestra el menú de opciones"""
    print("\n" + "="*60)
    print("          SISTEMA INTERACTIVO DE ÁRBOL BINARIO")
    print("="*60)
    print(f"ESTADO ACTUAL: {arbol.estado_arbol()}")
    print("="*60)
    print("[1]  Insertar elemento")
    print("[2]  Mostrar árbol completo (texto)")
    print("[3]  Graficar árbol completo")
    print("[4]  Buscar un elemento")
    print("[5]  Recorrer en PreOrden")
    print("[6]  Recorrer en InOrden")
    print("[7]  Recorrer en PostOrden")
    print("[8]  Eliminar nodo (Predecesor)")
    print("[9]  Eliminar nodo (Sucesor)")
    print("[10] Recorrer por niveles")
    print("[11] Altura del árbol")
    print("[12] Cantidad de hojas")
    print("[13] Cantidad de nodos")
    print("[15] Verificar si es completo")
    print("[16] Verificar si es lleno")
    print("[17] Eliminar árbol completo")
    print("[18] Crear árbol desde datos (separados por coma)")
    print("[19] Crear árbol vacío")
    print("[0]  Salir")
    print("="*60)

def mostrar_cambio_arbol(arbol, mensaje):
    """Muestra el cambio en el árbol después de una operación"""
    limpiar_consola()
    print(f"✓ {mensaje}")
    print("\n" + "="*40)
    print("ESTADO ACTUAL DEL ÁRBOL")
    print("="*40)
    arbol.mostrar_arbol()
    
    # Mostrar gráfico automáticamente después de cambios
    if arbol.contar_nodos() > 0:
        print("\nGenerando representación gráfica...")
        arbol.graficar_arbol()

def main():
    """Función principal interactiva"""
    arbol = ArbolBinario()
    
    while True:
        limpiar_consola()
        mostrar_menu(arbol)
        
        try:
            opcion = input("\nSeleccione una opción: ").strip()
            
            if opcion == "0":
                print("¡Hasta luego!")
                break
            
            elif opcion == "1":
                limpiar_consola()
                print("INSERTAR ELEMENTO")
                print("-" * 30)
                valor = input("Ingrese el valor a insertar: ").strip()
                resultado, mensaje = arbol.insertar(valor)
                mostrar_cambio_arbol(arbol, mensaje)
                input("\nPresione Enter para continuar...")
            
            elif opcion == "2":
                limpiar_consola()
                arbol.mostrar_arbol()
                input("\nPresione Enter para continuar...")
            
            elif opcion == "3":
                limpiar_consola()
                print("GENERANDO REPRESENTACIÓN GRÁFICA...")
                arbol.graficar_arbol()
                input("\nPresione Enter para continuar...")
            
            elif opcion == "4":
                limpiar_consola()
                print("BUSCAR ELEMENTO")
                print("-" * 30)
                valor = input("Ingrese el valor a buscar: ").strip()
                resultado, mensaje = arbol.buscar(valor)
                print(f"\n✓ {mensaje}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "5":
                limpiar_consola()
                resultado = arbol.preorden()
                print(f"RECORRIDO PREORDEN: {resultado}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "6":
                limpiar_consola()
                resultado = arbol.inorden()
                print(f"RECORRIDO INORDEN: {resultado}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "7":
                limpiar_consola()
                resultado = arbol.postorden()
                print(f"RECORRIDO POSTORDEN: {resultado}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "8":
                limpiar_consola()
                print("ELIMINAR NODO (PREDECESOR)")
                print("-" * 30)
                valor = input("Ingrese el valor a eliminar: ").strip()
                resultado, mensaje = arbol.eliminar_predecesor(valor)
                if resultado:
                    mostrar_cambio_arbol(arbol, mensaje)
                else:
                    print(f"✗ {mensaje}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "9":
                limpiar_consola()
                print("ELIMINAR NODO (SUCESOR)")
                print("-" * 30)
                valor = input("Ingrese el valor a eliminar: ").strip()
                resultado, mensaje = arbol.eliminar_sucesor(valor)
                if resultado:
                    mostrar_cambio_arbol(arbol, mensaje)
                else:
                    print(f"✗ {mensaje}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "10":
                limpiar_consola()
                resultado = arbol.recorrido_por_niveles()
                print(f"RECORRIDO POR NIVELES: {resultado}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "11":
                limpiar_consola()
                altura = arbol.altura()
                print(f"ALTURA DEL ÁRBOL: {altura}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "12":
                limpiar_consola()
                hojas = arbol.contar_hojas()
                print(f"CANTIDAD DE HOJAS: {hojas}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "13":
                limpiar_consola()
                nodos = arbol.contar_nodos()
                print(f"CANTIDAD TOTAL DE NODOS: {nodos}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "15":
                limpiar_consola()
                completo = arbol.es_completo()
                estado = "SÍ" if completo else "NO"
                print(f"¿EL ÁRBOL ES COMPLETO? {estado}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "16":
                limpiar_consola()
                lleno = arbol.es_lleno()
                estado = "SÍ" if lleno else "NO"
                print(f"¿EL ÁRBOL ES LLENO? {estado}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "17":
                resultado, mensaje = arbol.eliminar_arbol()
                limpiar_consola()
                print(f"✓ {mensaje}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "18":
                limpiar_consola()
                print("CREAR ÁRBOL DESDE DATOS")
                print("-" * 40)
                print("Ejemplo: 50,30,70,20,40,60,80,10,25")
                datos = input("\nIngrese los datos separados por coma: ").strip()
                resultado, mensaje = arbol.crear_desde_lista(datos)
                if resultado:
                    mostrar_cambio_arbol(arbol, mensaje)
                else:
                    print(f"✗ {mensaje}")
                input("\nPresione Enter para continuar...")
            
            elif opcion == "19":
                resultado, mensaje = arbol.crear_vacio()
                limpiar_consola()
                print(f"✓ {mensaje}")
                input("\nPresione Enter para continuar...")
            
            else:
                print("❌ Opción no válida. Intente nuevamente.")
                input("\nPresione Enter para continuar...")
        
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            input("\nPresione Enter para continuar...")

# Para usar como módulo
if __name__ == "__main__":
    main()