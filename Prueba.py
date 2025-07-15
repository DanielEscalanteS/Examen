

#Funcion para validar errores al ingresar enteros
def error(x):
    while True:
        try:
            y=int(input(x))
            return y
        except ValueError:
            print ("Debe Ingresar valores enteros!!")

#Diccionarios
productos={"8475HD":["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GtX1050"],
            "217HD":["Acer", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"]}
stock={"8475HD":[387990,10],
       "217HD": [327990,5]}
# Opcion 1
def Stock_marca(marca):
    Contador=0
    for y in productos.items():
        if ((y[1])[0]).upper() == marca:
            Contador+=1
            
    print(f"El stock es: {Contador}")
#Opcion 2
def busqueda_precio(p_min, p_max):
    lista=[]
    for y in stock.items():
        if p_min<(y[1])[0] and (y[1])[0]<p_max and (y[1])[1]!=0:
            lista.append(f"{productos[y[0]][0]}-{y[0]}")
    if lista:
        lista.sort()
        print(lista)
    else:
        print("No hay notebooks en ese rango de precios")
#Opcion 3
def elliminar_producto(modelo):
    if modelo in stock:
        del stock[modelo]
        del productos[modelo]
        return True
    else:
        return False

while True:
    Opcion=error("""***MENU PRINCIPAL***
1. Stock marca.
2. Búsqueda por precio.
3.Eliminar producto
4. Salir
Ingrese su opción: """)
    if Opcion==1:
        seleccion= input("Ingrese marca a consultar: ").upper()
        Stock_marca(seleccion)
    elif Opcion==2:
        p_m=error("Ingrese precio mínimo: ")
        p_M=error("Ingrese precio máximo: ")
        busqueda_precio(p_m, p_M)
    elif Opcion==3:
        while True:
            elemento=input("Ingrese modelo a actualizar: ")
            if elliminar_producto(elemento):
                print("Producto eliminado!!")
            else:
                print("EL modelo no existe!!")
            otro=input("Desea eliminar otro producto (si/no)?").upper()
            if otro == "NO":
                break
    elif Opcion == 4:
        print("Programa finalizado")
        break
    else:
        print("Debe seleccionar una opción válida!!")
        

