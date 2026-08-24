from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n--- MENÚ DEL RESTAURANTE ---")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar precio de producto")
    print("5. Eliminar producto")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("8. Ver categorías únicas")
    print("9. Salir")

def main():
    restaurante = Restaurante()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            try:
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: "))
                
                nuevo_prod = Producto(codigo, nombre, categoria, precio)
                restaurante.registrar_producto(nuevo_prod)
                print("¡Producto registrado y guardado con éxito!")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif opcion == '2':
            productos = restaurante.listar_productos()
            if not productos:
                print("No hay productos registrados.")
            else:
                print("\n--- LISTA DE PRODUCTOS ---")
                for p in productos:
                    print(f"[{p.codigo}] {p.nombre} - {p.categoria} - ${p.precio:.2f}")
                    
        elif opcion == '3':
            codigo = input("Ingrese el código a buscar: ")
            p = restaurante.buscar_producto(codigo)
            if p:
                print(f"Encontrado: [{p.codigo}] {p.nombre} - {p.categoria} - ${p.precio:.2f}")
            else:
                print("Producto no encontrado.")
                
        elif opcion == '4':
            try:
                codigo = input("Código del producto a actualizar: ")
                nuevo_precio = float(input("Nuevo precio: "))
                restaurante.actualizar_producto(codigo, nuevo_precio)
                print("¡Precio actualizado correctamente!")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif opcion == '5':
            try:
                codigo = input("Código del producto a eliminar: ")
                restaurante.eliminar_producto(codigo)
                print("¡Producto eliminado correctamente!")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif opcion == '6':
            try:
                ide = input("Identificación: ")
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                nuevo_usu = Usuario(ide, nombre, correo)
                restaurante.registrar_usuario(nuevo_usu)
                print("¡Usuario registrado con éxito!")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif opcion == '7':
            usuarios = restaurante.listar_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                print("\n--- LISTA DE USUARIOS ---")
                for u in usuarios:
                    print(f"[{u.identificacion}] {u.nombre} - {u.correo}")
                    
        elif opcion == '8':
            categorias = restaurante.obtener_categorias_unicas()
            if not categorias:
                print("No hay categorías registradas.")
            else:
                print(f"Categorías únicas: {list(categorias)}")
                
        elif opcion == '9':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()