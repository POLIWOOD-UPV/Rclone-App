import shutil
import subprocess

if shutil.which("rclone") is None:
    print("rclone no está instalado o no está en PATH")

opciones: str = input("¿Qué quieres hacer? (config/copy-move): ")

def copy_move() -> str:
    cmd = input("Que quieres hacer (copy/move): ")
    dir1 = input("dir 1: ")
    dir2 = input("dir2: ")
    result = subprocess.run(["rclone", f"{cmd}", f"{dir1}", f"{dir2}", "--progress", "--ignore-existing"], capture_output=True, text=True)
    return result

def buscar(salida) -> int:
    opciones = {}
    matches = re.findall(r'(\d+)\s+/\s+(.+)', salida)
    for numero, nombre in matches:
        opciones[nombre.strip()] = numero

    for nombre, numero in opciones.items():
        print(f"{nombre} -> {numero}\n")
        
    eleccion = input("Cual quieres: ")
    return opciones[eleccion]

def config():
    nombre = input("Nombre del repositorio: ")
    numero = 42
    url = input("Direccion del sharepoint: ")
    comando = subprocess.Popen(['rclone','config'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)
    salida,errores = comando.communicate(input=f"n\n{nombre}\n{numero}\n\n\n\n\n\n\n3\n{url}\n2\n\n\n")
    #El 2 depende del sharepoint, 1 si es uno normal y 2 si es una personalizado
    
    print(salida)
    
    '''
    comando.stdin.write("n\n")
    comando.stdin.flush()
    
    comando.stdin.write(f"{nombre}\n")
    comando.stdin.flush()
    
    comando.stdin.write(f"{numero}\n\n\n\n\n\n\n")
    comando.stdin.flush()
    
    comando.stdin.write(f"3\n")
    comando.stdin.flush()

    https://upvedues.sharepoint.com/sites/HastaAcabarEstoCopias
    '''

if opciones == "config":
    config()
elif opciones == "copy-move":
    result = copy_move()
    print(result.stout)

else:
    print("La opción no es correcta")


'''print(result.stdout) #Captura de salida
print(result.stderr) #Captura de errores'''

'''
if result.returncode == 0: #Si no da error
if result.returncode != 0: #Si da error
'''

'''
1. Direcciones manuales -> Mayo-Junio
rclone config / rclone copy-move
config -> Manual
Variables: Nombre, Dirección

Copy/Move -> Pide directorios
Variables: cmd(copy/move), Dir1, Dir2
'''