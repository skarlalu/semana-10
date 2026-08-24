import json
import os

class ArchivoServicio:
    RUTA_ARCHIVO = os.path.join("datos", "productos.json")

    @staticmethod
    def guardar_productos(productos_diccionarios: list) -> None:
        os.makedirs("datos", exist_ok=True)
        try:
            with open(ArchivoServicio.RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                json.dump(productos_diccionarios, archivo, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: No hay permisos para escribir el archivo JSON.")

    @staticmethod
    def cargar_productos() -> list:
        try:
            if not os.path.exists(ArchivoServicio.RUTA_ARCHIVO):
                return []
            with open(ArchivoServicio.RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                if not contenido.strip():
                    return []
                return json.loads(contenido)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        except PermissionError:
            print("Error: Permiso denegado para leer el archivo.")
            return []