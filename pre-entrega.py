print("\n" + "_" * 65)
print("\n        BIENVENIDO A SCP (Sistema de Carga de Productos)")
print("_" * 65)

print("\n" + "\t" * 2 + "Elija la opcion que desea y oprima ENTER" "\n")
print("\t" * 1 + "1 - Alta de prducto")
print("\t" * 1 + "2 - Modificar datos de un producto")
print("\t" * 1 + "3 - Eliminar un producto" "\n")

seleccion_de_opcion = int(input())

if seleccion_de_opcion == 1:
    print("\n" + "Indique los datos del nuevo producto")
    print("Nombre: ")
    input()
    print("Categoria: ")
    input()
    print("Precio: ")
    input()