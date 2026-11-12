import Menu
import Gestion_stock
def main():
    Gestion_stock.inicializar()
    opcion= 0
    
    while opcion != 4:
        opcion= Menu.mostrar_menu()
        if opcion== 1:
            Gestion_stock.cargar_stock()
                
        elif opcion== 2:
            Gestion_stock.mostrar_stock()
                
        elif opcion== 3:
            categoria= input("Ingrese la categoria: \n")
            if categoria in Gestion_stock.stock_cantidades:
                Gestion_stock.contar(
                    Gestion_stock.stock_cantidades[categoria]
                        )
            else:
                print("Esta categoría no es válida")
        elif opcion== 4:
            print("Saliendo del sistema...")
        else:
            print("Esta opción no es válida")

if __name__ == "__main__":
    main()