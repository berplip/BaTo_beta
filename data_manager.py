# data_manager.py

import hashlib

# --- Almacenamiento de Usuarios (directamente en el código) ---

    # Puedes agregar más usuarios aquí si es necesario, generando sus hashes

_usuarios_registrados = {
    "usuario1": {"contrasena_hash": hashlib.sha256("pass123".encode()).hexdigest(), "rol": "usuario"},
    "admin": {"contrasena_hash": hashlib.sha256("adminpass".encode()).hexdigest(), "rol": "administrador"}
}

# --- Estado del Usuario Actual (global a este módulo) ---

usuario_actual = {"nombre": None, "rol": None}
hora_inicio_sesion_actual = None

# --- Diccionario de productos (directamente en el código) ---

_productos = {
    "LP7516": {
        "serie": "666",
        "manual": "lp7516manual.pdf",
        "calibracion": "https://www.youtube.com/watch?v=WJbHmguujdc&ab_channel=ONECOIN",
        "bateria": "4V4AH/20HR",
        "info": "Conector de 5 pines y RS232.",
        "imagen": "LP7516sec01.png",
        "stock": 10
    },
    "TCS-IND.": {
        "serie": "67890ABC",
        "manual": "TCS-IND_manual.pdf",
        "calibracion": "https://www.youtube.com/watch?v=example_cal_video",
        "bateria": "Níquel",
        "info": "Indicador industrial versátil.",
        "imagen": "TCS-IND.png",
        "stock": 5
    },
    "XK": {
        "serie": "123 ",
        "manual": "",
        "calibracion": "",
        "bateria": "6V4AH",
        "info": "Indicador básico y económico.",
        "imagen": "XK.png",
        "stock": 25
    },
    "TRASPALETA": {
        "serie": "XYZ789",
        "manual": "TRASPALETA_manual.pdf",
        "calibracion": "",
        "bateria": "Batería recargable específica.",
        "info": "Balanza integrada en transpaleta manual.",
        "imagen": "TRASPALETA.png",
        "stock": 3
    }
}

# --- Funciones Públicas para Acceder y Modificar Datos ---

def get_productos_data():
    """Retorna una copia del diccionario de productos."""
    return _productos.copy()

def get_producto_data(nombre_producto):
    """Retorna los datos de un producto específico (como una copia), o None."""
    producto = _productos.get(nombre_producto)
    return producto.copy() if producto else None

def get_usuarios_registrados_data():
    """Retorna una copia del diccionario de usuarios."""
    return _usuarios_registrados.copy()

def actualizar_producto_data(nombre_producto, datos_actualizados):
    """Actualiza un producto existente en el diccionario en memoria."""
    if nombre_producto in _productos:
        _productos[nombre_producto].update(datos_actualizados)
        print(f"INFO (data_manager): Producto '{nombre_producto}' actualizado en memoria.")
        return True
    print(f"ERROR (data_manager): Intento de actualizar producto no existente '{nombre_producto}'.")
    return False

def eliminar_producto_data(nombre_producto):
    """Elimina un producto del diccionario en memoria."""
    if nombre_producto in _productos:
        del _productos[nombre_producto]
        print(f"INFO (data_manager): Producto '{nombre_producto}' eliminado de memoria.")
        return True
    print(f"ERROR (data_manager): Intento de eliminar producto no existente '{nombre_producto}'.")
    return False

def registrar_producto_data(nombre_producto, datos_producto):
    """Registra un nuevo producto en el diccionario en memoria."""
    if nombre_producto not in _productos:
        _productos[nombre_producto] = datos_producto
        print(f"INFO (data_manager): Producto '{nombre_producto}' registrado en memoria.")
        return True
    print(f"ERROR (data_manager): Intento de registrar producto ya existente '{nombre_producto}'.")
    return False