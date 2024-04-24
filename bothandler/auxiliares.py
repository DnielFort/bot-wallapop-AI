import os

def link_valido(link):
    # Comprueba que el link existe y comienza con la cadena de texto especificada
    if link != '/nuevo_aviso':
        return True
    else:
        return False

# Obtiene ruta al directorio actual
parent_dir = os.getcwd()

# Construye la ruta al directorio 'usuarios'
usuarios_dir = os.path.join(parent_dir, 'usuarios')

# Crea una carpeta en Usuarios con el nombre del id_usuario
def crear_carpeta(id_usuario):
    usuario_dir = os.path.join(usuarios_dir, str(id_usuario))
    # Crea el directorio si no existe
    os.makedirs(usuario_dir, exist_ok=True)
    # Crea un fichero llamado links.txt si no existe
    with open(os.path.join(usuario_dir, 'links.txt'), 'a') as f:
        pass


def añadir_producto(id_usuario, link):
    # Se crea la carpeta del usuario si hace falta
    crear_carpeta(id_usuario)
    # Se abre el archivo links.txt en modo append
    with open(os.path.join(usuarios_dir, str(id_usuario), 'links.txt'), 'a') as f:
        # Se escribe el link en el archivo
        f.write(link[13:] + '\n')
    

def obtener_nombres_carpetas_usuarios():
    ruta_directorio_usuarios = './usuarios'  # Ajusta esto a la ruta correcta si es necesario
    todos_los_archivos_y_directorios = os.listdir(ruta_directorio_usuarios)
    solo_directorios = [nombre for nombre in todos_los_archivos_y_directorios if os.path.isdir(os.path.join(ruta_directorio_usuarios, nombre))]
    return solo_directorios