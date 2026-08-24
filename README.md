Estudiante: Karla Luque
Descripción del Sistema
Aplicación desarrollada en Python para la gestión de productos y usuarios de un restaurante. Integra principios de Programación Orientada a Objetos (POO), manejo de excepciones robusto para evitar caídas del programa y persistencia de datos local mediante un archivo en formato JSON.

Estructura del Proyecto
modelos
  __init__.py: Inicializador del paquete de modelos.
  producto.py: Contiene la clase Producto con encapsulamiento mediante @property y @setter para validar precios, y un método de serialización a diccionario.
  usuario.py: Contiene la clase Usuario para representar la información básica de los usuarios.
  servicios
  __init__.py: Inicializador del paquete de servicios.
  archivo_servicio.py: Servicio dedicado exclusivamente a la lectura, escritura y manejo de errores del archivo JSON.
  restaurante.py: Clase central que administra colecciones en memoria (list), obtiene elementos únicos (set), y coordina el guardado y la carga automática con el servicio de archivos.
  datos
  productos.json: Archivo físico donde se almacenan de manera persistente los productos del restaurante.
  main.py: Punto de entrada del programa que gestiona la interacción por consola mediante un menú interactivo, utilizando bucles, entradas de usuario y bloques de control try-except.
  README.md: Documentación oficial del proyecto.

