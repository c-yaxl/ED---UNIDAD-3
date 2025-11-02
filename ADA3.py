#Axel Ariel Cach Yam
class POSTRES:
    def __init__(self):
        self.postres = []
    
    def buscar_postre(self, nombre_postre):
        for i, (nombre, ingredientes) in enumerate(self.postres):
            if nombre.lower() == nombre_postre.lower():
                return i, nombre, ingredientes
        return -1, None, None
    
    def ingredientes(self):
        
        nombre_postre = input("Ingrese el nombre del postre: ").strip()
        
        if not nombre_postre:
            print("Error: Debe ingresar un nombre de postre.")
            return
        
        id, nombre, ingredientes = self.buscar_postre(nombre_postre)
        if id == -1:
            print(f"Error: El postre '{nombre_postre}' no existe en la estructura.")
            return
        print(f"\n--- Ingredientes de '{nombre}' ---")
        if not ingredientes:
            print("No tiene ingredientes registrados.")
        else:
            for i, ingrediente in enumerate(ingredientes, 1):
                print(f"  {i}. {ingrediente}")
        print("--------------------------------")
    
    def agregar_ingrediente(self):
        nombre_postre = input("Ingrese el nombre del postre: ").strip()
        
        if not nombre_postre:
            print("Error: Debe ingresar un nombre de postre.")
            return
        
        id, nombre, ingredientes = self.buscar_postre(nombre_postre)
        if id == -1:
            print(f"Error: El postre '{nombre_postre}' no existe.")
            return
        
        print(f"\nPostre encontrado: '{nombre}'")
        print("Ingredientes actuales:", ", ".join(ingredientes) 
              if ingredientes 
              else "Ninguno")
        
        nuevos_ingredientes = input("\nIngrese los nuevos ingredientes (separados por coma): ").strip()
        if not nuevos_ingredientes:
            print("Error: No se proporcionaron ingredientes.")
            return
        nuevos_ingredientes = [ing.strip() for ing in nuevos_ingredientes.split(",") if ing.strip()]
        if not nuevos_ingredientes:
            print("Error: No se proporcionaron ingredientes válidos.")
            return
        ingredientes_agregados = 0
        for ingrediente in nuevos_ingredientes:
            if ingrediente not in ingredientes:
                ingredientes.append(ingrediente)
                ingredientes_agregados += 1
        
        if ingredientes_agregados > 0:
            print(f"\n✓ Se agregaron {ingredientes_agregados} ingredientes nuevos a '{nombre}'.")
            print("Ingredientes actualizados:", ", ".join(ingredientes))
        else:
            print("\nTodos los ingredientes ya existían en el postre.")
    
    def eliminar_ingrediente(self):
        nombre_postre = input("Ingrese el nombre del postre: ").strip()
        
        if not nombre_postre:
            print("Error: Debe ingresar un nombre de postre.")
            return
        
        id, nombre, ingredientes = self.buscar_postre(nombre_postre)
        if id == -1:
            print(f"Error: El postre '{nombre_postre}' no existe.")
            return
        if not ingredientes:
            print(f"Error: El postre '{nombre}' no tiene ingredientes.")
            return
        
        print(f"\nPostre: '{nombre}'")
        print("Ingredientes actuales:")
        for i, ingrediente in enumerate(ingredientes, 1):
            print(f"  {i}. {ingrediente}")
            
        ingrediente_eliminar = input("\nIngrese el nombre del ingrediente a eliminar: ").strip()
        if not ingrediente_eliminar:
            print("Error: Debe ingresar un ingrediente.")
            return
        if ingrediente_eliminar not in ingredientes:
            print(f"Error: El ingrediente '{ingrediente_eliminar}' no existe en '{nombre}'.")
            return
        
        ingredientes.remove(ingrediente_eliminar)
        print(f"\n✓ Ingrediente '{ingrediente_eliminar}' eliminado de '{nombre}'.")
        print("Ingredientes actualizados:", ", ".join(ingredientes) if ingredientes else "Ninguno")
    
    def nuevo_postre(self):
        nombre_postre = input("Ingrese el nombre del nuevo postre: ").strip()
        if not nombre_postre:
            print("Error: El nombre del postre no puede estar vacío.")
            return
        
        id, nombre_existente, _ = self.buscar_postre(nombre_postre)
        if id != -1:
            print(f"Error: El postre '{nombre_postre}' ya existe.")
            return
        
        ingredientes_input = input("Ingrese los ingredientes (separados por coma) o Enter para ninguno: ").strip()
        if ingredientes_input:
            ingredientes = [ing.strip() for ing in ingredientes_input.split(",") if ing.strip()]
        else:
            ingredientes = []
        
        nuevo_postre = (nombre_postre, ingredientes)
        
        # Encontrar posición para mantener orden alfabético
        posicion = 0
        for i, (nombre, _) in enumerate(self.postres):
            if nombre.lower() < nombre_postre.lower():
                posicion = i + 1
            else:
                break
        
        self.postres.insert(posicion, nuevo_postre)
        
        print(f"\n✓ Postre '{nombre_postre}' agregado exitosamente.")
        if ingredientes:
            print(f"Ingredientes: {', '.join(ingredientes)}")
    
    def eliminar_postre(self):
        
        nombre_postre = input("Ingrese el nombre del postre a eliminar: ").strip()
        if not nombre_postre:
            print("Error: Debe ingresar un nombre de postre.")
            return
        
        id, nombre, ingredientes = self.buscar_postre(nombre_postre)
        if id == -1:
            print(f"Error: El postre '{nombre_postre}' no existe.")
            return
        self.postres.pop(id)
        print(f"\n✓ Postre '{nombre}' eliminado exitosamente.")

    
    def eliminar_repetidos(self):
        postres_unicos = []
        nombres_vistos = set()
        postres_eliminados = 0
        
        for nombre, ingredientes in self.postres:
            if nombre not in nombres_vistos:
                nombres_vistos.add(nombre)
                postres_unicos.append((nombre, ingredientes))
            else:
                postres_eliminados += 1
                print(f"Eliminando postre duplicado: '{nombre}'")
        
        self.postres = postres_unicos
        
        if postres_eliminados > 0:
            print(f"\n✓ Se eliminaron {postres_eliminados} postres duplicados.")
        else:
            print("\n No se encontraron postres duplicados.")
    
    def mostrar_todos(self):
        """Muestra todos los postres en la estructura"""
        print("\n" + "="*50)
        print("           ESTRUCTURA COMPLETA POSTRES")
        print("="*50)
        
        if not self.postres:
            print("La estructura está vacía.")
        else:
            for i, (nombre, ingredientes) in enumerate(self.postres, 1):
                print(f"\n{i}. {nombre}")
                if ingredientes:
                    print("   Ingredientes:", ", ".join(ingredientes))
                else:
                    print("   Ingredientes: Ninguno")
        print("\n" + "="*50)


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("           SISTEMA DE GESTIÓN DE POSTRES")
    print("="*50)
    print("a. Ver ingredientes de un postre")
    print("b. Agregar ingredientes a un postre")
    print("c. Eliminar ingrediente de un postre")
    print("d. Agregar un postre")
    print("e. Eliminar un postre")
    print("1. Mostrar todos los postres")
    print("2. Eliminar postres repetidos")
    print("0. Salir")
    print("="*50)


def main():
    postres = POSTRES()
    print("¡Bienvenido al Sistema de Gestión de Postres!")
    
    while True:
        
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip().lower()
        if opcion == '0':
            print("\n¡Gracias por usar el Sistema de Gestión de Postres!")
            break
        elif opcion == 'a':
            postres.ingredientes()
        elif opcion == 'b':
            postres.agregar_ingrediente()
        elif opcion == 'c':
            postres.eliminar_ingrediente()
        elif opcion == 'd':
            postres.nuevo_postre()
        elif opcion == 'e':
            postres.eliminar_postre()
        elif opcion == '1':
            postres.mostrar_todos()
        elif opcion == '2':
            postres.eliminar_repetidos()
        else:
            print("\n Opción no válida. Por favor, seleccione una opción del menú.")
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()