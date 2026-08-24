from typing import List, Optional, Set
from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self) -> None:
        self.productos: List[Producto] = []
        self.usuarios: List[Usuario] = []
        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self) -> None:
        datos_json = ArchivoServicio.cargar_productos()
        for dato in datos_json:
            try:
                prod = Producto(
                    codigo=dato["codigo"],
                    nombre=dato["nombre"],
                    categoria=dato["categoria"],
                    precio=float(dato["precio"])
                )
                self.productos.append(prod)
            except (KeyError, ValueError):
                pass

    def guardar_coleccion(self) -> None:
        datos = [p.a_diccionario() for p in self.productos]
        ArchivoServicio.guardar_productos(datos)

    def registrar_producto(self, producto: Producto) -> None:
        if self.buscar_producto(producto.codigo):
            raise ValueError("Ya existe un producto con este código.")
        self.productos.append(producto)
        self.guardar_coleccion()

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nuevo_precio: float) -> None:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("No se encontró un producto con ese código.")
        producto.precio = nuevo_precio
        self.guardar_coleccion()

    def eliminar_producto(self, codigo: str) -> None:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("No se encontró un producto con ese código.")
        self.productos.remove(producto)
        self.guardar_coleccion()

    def listar_productos(self) -> List[Producto]:
        return self.productos

    def registrar_usuario(self, usuario: Usuario) -> None:
        for u in self.usuarios:
            if u.identificacion == usuario.identificacion:
                raise ValueError("La identificación ya está registrada.")
        self.usuarios.append(usuario)

    def listar_usuarios(self) -> List[Usuario]:
        return self.usuarios

    def obtener_categorias_unicas(self) -> Set[str]:
        categorias = set()
        for producto in self.productos:
            categorias.add(producto.categoria)
        return categorias