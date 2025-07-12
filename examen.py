import os
os.system("cls")
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
    }

def ver_modelos():
    print("\nModelos disponibles")

    for modelo in sorted(productos.keys()):
        marca = modelo.append
        print(marca)
    



def ver_marca():#primero
    marcas = set()

    for prod in productos.values():
        marcas.add(prod[0])
    for marca in sorted(marcas):
        print(f"{marca}")

def stock_marca(marca):#primero
    for marca in sorted(stock)[1]:
        print(f"{marca}")



def busqueda_por_precio(p_min,p_max):
    stock = []
    pass


def Actualizar_precio(modelo, p):
   pass


def Selecc_opcion(max):
    try:
        opcion = int(input("Ingresa una opcion: "))
        if opcion < 1 or opcion > max:
            input("Ingresa un valor entre 1 y 4")
        else:
            return opcion
    except ValueError:
        input("Ingresa un valor valido, Presiona entrer para volver a intentar")


    

def menu():
    while True:

        print("===Tienda Online Pybooks===")
        print("1.- Stock Marca.")
        print("2.- Busqueda por precio.")
        print("3.- Actualizar precio.")
        print("4.- Salir.")

        opcion = Selecc_opcion(4)


        if opcion == 1:
            os.system("cls")
            ver_marca()
            marca = input("Ingresa la marca para ver el stock disponible: ").lower()
            stock_marca(marca)
            input()
        
        elif opcion == 2:
            os.system("cls")
            p_min = int(input("Ingresa el precio minimo: "))
            p_max = int(input("Ingresa el precio maximo: "))
            busqueda_por_precio(p_min,p_max)
            input()
        
        elif opcion == 3:
            os.system("cls")
            ver_modelos()
            modelo = input("Ingrese el modelo: ")
            Actualizar_precio()
            input()
        
        elif opcion  == 4:
            os.system("cls")
            print("Programa terminado")
            break

        else:
            print("Valor no valido.")
        

menu()