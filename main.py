from task_manager import TaskManager

def  print_menu():
    print("\n---Gestor de Tareas inteligente---\n")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir\n")


def main():
    
    manager = TaskManager()

    while True:
        print_menu()

        choice = input("Seleccione una opción (1-5): ")
        match choice:
            case "1":
                description = input("Ingrese la descripción de la tarea: ")
                manager.add_task(description)
            case "2":
                manager.list_tasks()
            case "3":
                id = int(input("Ingrese el ID de la tarea a completar: "))
                manager.complete_task(id)
            case "4":
                id = int(input("Ingrese el ID de la tarea a eliminar: "))
                manager.delete_task(id)
            case "5":
                print("Saliendo del gestor de tareas. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()