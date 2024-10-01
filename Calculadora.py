
def calcular_total_a_pagar(cantidad_kg, precio_por_kilo):
    """Calcula el total a pagar basado en la cantidad y el precio por kilo."""
    return cantidad_kg * precio_por_kilo

def calcular_vuelto(total_a_pagar, monto_pagado):
    """Calcula el vuelto basado en el total a pagar y el monto pagado."""
    return monto_pagado - total_a_pagar

def obtener_nombre_completo(nombre, apellido):
    """Obtiene el nombre completo combinando nombre y apellido."""
    return f"{nombre} {apellido}"





def mostrar_menu():
    "Muestra el menú de frutas y verduras en consola."
    print("Menú de Frutas y Verduras")
    print("========================")
    
    # Listas de frutas y verduras
    frutas = ["Manzana", "Plátano", "Naranja"]
    verduras = ["Zanahoria", "Brócoli"]
    
    # Mostrar frutas
    print("Frutas:")
    for i, fruta in enumerate(frutas, start=1):
        print(f"{i}. {fruta}")

    # Mostrar verduras
    print("\nVerduras:")
    for i, verdura in enumerate(verduras, start=4):
        print(f"{i}. {verdura}")





if __name__ == "__main__":

    "Función principal que ejecuta el menú."
    mostrar_menu()
    print("")
    fruta = input("Ingrese la fruta que va a comprar el cliente: ")
    cantidad_kg = float(input("Ingrese la cantidad que va a comprar el cliente (en KG): "))
    
    precio_por_kilo = float(input("Ingrese el precio de la fruta o verdura (en pesos chilenos, por kilo): "))
    monto_pagado = float(input("Ingrese con cuánto pagó el cliente: "))

    total_a_pagar = calcular_total_a_pagar(cantidad_kg, precio_por_kilo)
    vuelto = calcular_vuelto(total_a_pagar, monto_pagado)

    """Registra una venta y calcula los detalles asociados."""
    nombre_vendedor = input("Ingrese el nombre del vendedor: ")
    apellido_vendedor = input("Ingrese el apellido del vendedor: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    apellido_cliente = input("Ingrese el apellido del cliente: ")

    nombre_completo_vendedor = obtener_nombre_completo(nombre_vendedor, apellido_vendedor)
    nombre_completo_cliente = obtener_nombre_completo(nombre_cliente, apellido_cliente)
    


    print("\nDetalles de la venta:")
    print(f"Vendedor: {nombre_completo_vendedor}")
    print(f"Cliente: {nombre_completo_cliente}")
    print(f"Fruta/verdura: {fruta}")
    print(f"Cantidad comprada (KG): {cantidad_kg}")
    print(f"Precio por kilo: {precio_por_kilo} CLP")
    print(f"Total a pagar: {total_a_pagar} CLP")
    print(f"Vuelto: {vuelto} CLP")

def main():
    num_ventas = int(input("Ingrese la cantidad de ventas a realizar: "))
    
    for i in range(num_ventas):
        print(f"\n--- Venta {i+1} ---")
        registrar_venta()

if __name__ == "__main__":
    main()
