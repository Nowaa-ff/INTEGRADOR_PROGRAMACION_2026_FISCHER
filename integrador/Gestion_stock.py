stock_productos= {
    'enlatados': [],
    'frutas': [],
    'congelados': [],
    'panaderia': []
}
stock_cantidades= {
    'enlatados': [],
    'frutas': [],
    'congelados': [],
    'panaderia': []
}


def inicializar():
    for categoria in stock_productos:
        stock_productos[categoria]= []
    for categoria in stock_cantidades:
        stock_cantidades[categoria]= []

def cargar_stock():
    categoria= input("Ingrese la catgoria (enlatados/frutas/congelados/panaderia): \n")
    if categoria in stock_productos:
        producto= input("Ingrese elproducto: \n")
        cantidad= int(input("Ingrese la cantidad: \n"))
        stock_productos[categoria].append(producto)
        stock_cantidades[categoria].append(cantidad)
    else:
        print("Esa categoría no es existe...")
 

def mostrar_stock():
    for categoria in stock_productos:
        print("— Categoría: ", categoria)
        print("— Productos: ", stock_productos[categoria])
        print("— Cantidades:  ", stock_cantidades[categoria])
    
def contar(lista_productos):
    cont= 0
    total= 0
    for cant in lista_productos:
        cont= cont  +1
        total= total + cant
    print("—— Cantidad de productos en esta categoría: ", cont)
    print("—— Cantidad total de productos: ", total)
           