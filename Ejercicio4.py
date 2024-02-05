#ejercicio 4
tareas = []

def agregar_tarea():
    descripcion = input("Ingrese la descripción de la tarea: ")
    tarea = {"descripcion": descripcion, "estado": "pendiente"}
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

def eliminar_tarea():
    descripcion = input("Ingrese la descripción de la tarea que desea eliminar: ")
    for tarea in tareas:
        if tarea["descripcion"] == descripcion:
            tareas.remove(tarea)
            print("Tarea eliminada con éxito.")
            return
    print("No se encontró la tarea especificada.")

def mostrar_tareas():
    for tarea in tareas:
        print(f"Descripción: {tarea['descripcion']}, Estado: {tarea['estado']}")

def marcar_completada():
    descripcion = input("Ingrese la descripción de la tarea que desea marcar como completada: ")
    for tarea in tareas:
        if tarea["descripcion"] == descripcion:
            tarea["estado"] = "completada"
            print("Tarea marcada como completada con éxito.")
            return
    print("No se encontró la tarea especificada.")

while True:
    print("¿Qué acción desea realizar?")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar todas las tareas")
    print("4. Marcar tarea como completada")
    print("5. Salir")
    opcion = input("Ingrese el número de la opción que desea: ")
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        eliminar_tarea()
    elif opcion == "3":
        mostrar_tareas()
    elif opcion == "4":
        marcar_completada()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Intente de nuevo.")
