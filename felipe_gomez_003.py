productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']},
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}


def stock_marca(marca:str):
    """Selecciona una marca"""
    marca= "HP, lenovo, Asus, Dell".lower()
    for i in productos:
        for j in marca:
            if i == j:
                return True



def valida_texto(mensaje_input):
    while True:
        texto=input(mensaje_input)
        if len(texto.strip())==0:
            continue


def valida_opcion(mensaje_input:int):
    while True:
        texto=input(mensaje_input)
        if valida_opcion > 5 and valida_opcion <= 0:
            print("Debe seleccionar una opcion válida!!")


def marca_precio(busqueda_precio:int):
    busqueda_precio== 0
    for i in stock:
        for j in busqueda_precio:
            if i ==j:
                return True


            
#letras en codigo
def codigo_stock(stock:str):
    letras="ABCDEFGHIJKLMNÑOPQRSTUVXYZ".lower()
    for i in codigo_stock:
        for j in letras:
            if i == j:
                return True

#numeros en codigo
def codigo_stock(stock:int):
    letras="1234567890"
    for i in codigo_stock:
        for j in letras:
            if i == j:
                return True
    
    

def Actualizar_precio(marca:str,marca_precio:int,codigo_stock:int):
        stock={
            '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
            'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
            'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
        }
        stock[0].append()
        


#lenovo:249990
#asus:749990
def menu():
    
    while True:
        print("***MENÚ PRINCIPAL***")
        print("[1] - Stock marca")
        print("[2] - Búsqueda por precio")
        print("[3] - Actualizar precio")
        print("[4] - Salir")
        opcion= valida_opcion("Ingres una opción:")

        if opcion == 1:
            stock_marca= valida_texto("Ingrese una marca que desee buscar:")
            if stock_marca != productos:
                print("La marca ingresada no se encuentra dentro de nuestros productos")
            elif stock_marca == productos:
                print(productos)
        elif opcion ==2:
            busqueda_precio_minimo= marca_precio("Primero ingrese el mínimo de precio que desea:")
            busqueda_precio_maximo= marca_precio("Ahora ingrese el máximo de precio que desea:")
            if busqueda_precio_minimo < 249990:
                print("No hay notebooks en ese rango de precios.")
            else:
                print("Tenemos stock de los siguientes productos:"[productos])
        elif opcion== 3:
            precio_actualizado= Actualizar_precio("Ingrese el modelo que desea actualizar:")
            print("Pecio actualizado!!")
            print(input("¿Desea actualizar algún otro precio?"))
        elif opcion==4:
            print("Programa finalizado")

        






        

