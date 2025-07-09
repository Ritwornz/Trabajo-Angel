productos={
    "8475HD":["HP",15.6,"8GB","DD","IT","Intel Core i5","Nvidia GTX1050"],
    "2175HD":["lenovo",14,"4GB","SSD","512GB","Inel Core i5","Nvidia GTX1050"],
    "JjfFHD":["Asus",14,"16GB","SSD","256GB","Intel Core i7","Nvidia RTX2080Ti"],
    "fgdxFHD":["HP",15.6,"8GB","DD","IT","Intel Core i3","integrada"],
    "GF75HD":["Asus",15.6,"8GB","DD","IT","Intel Core i7","Nvidia GTX1050"],
    "123FHD":["lenovo",14,"6GB","DD","IT","AMD Ryzen 5","integrada"],
    "342FHD":["lenovo",15.6,"8GB","DD","IT","AMD Ryzen 7","Nvidia GTX1050"],
    "UWU131HD":["Dell",15.6,"8GB","DD","IT","AMD Ryzen 3","Nvidia GTX1050"]
}
stock={
    "8475HD":[387990,10],
    "2175HD":[327990,4],
    "JjfFHD":[424990,1],
    "fgdxFHD":[664990,21],
    "GF75HD":[749990,2],
    "123FHD":[290890,32],
    "342FHD":[444990,7],
    "UWU131HD":[349990,1]
}
def menu():
    op=0
    while(op!=4):
        print("=======MENU-PRINCIPAL=======")
        print("│1.Stock marca.            │")
        print("│2.Busqueda por precio.    │")
        print("│3.Actualizar precio       │")
        print("│4.Salir.                  │")
        print("============================")
        try:
            op=int(input("Ingrese su opción(1-4): "))
            if(op==1):
                marca=input("Ingrese la marca a consultar: ").upper()
                stock_marca(marca)
            elif(op==2):
                try:
                    p_min=input("Ingrese el valor minimo: ")
                    p_max=input("Ingrese el valor maximo: ")
                    búsqueda_precio(p_min, p_max)
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            elif(op==3):
                modelo=input("Ingrese modelo a actualizar: ").upper()
                p=input("Ingrese precio nuevo: ")
                actualizar_precio(modelo, p)
            elif(op==4):
                print("Programa finalizado.")
                break
            else:
                print("Debe seleccionar una opción válida!!")
        except ValueError:
            print("Entrada incorrecta. Ingrese numeros enteros.")

def stock_marca(marca):
    stock_total=0
    yu=0
    marca=marca.lower()
    for id_productos, data in productos.items():
        if marca == data[0].lower():
            stock_total+=stock[id_productos][1]
            yu+=stock_total
    print(f"El stock es: {yu}")

def búsqueda_precio(p_min, p_max):
    for id_productos, data in stock.items():
        if p_min<=data[0]<=p_max and stock[1]>0:
            print(f"{data[0]}--{id_productos},")
            
        
def actualizar_precio(modelo, p):
    for id_modelo in productos:
        if modelo==stock[id_modelo][0]:
            id_modelo[0]=p
    print("precio actualizado!!")
    
menu()    
    
    
