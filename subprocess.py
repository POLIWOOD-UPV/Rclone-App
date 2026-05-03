import shutil
import subprocess

if shutil.which("rclone") is None:
    print("rclone no está instalado o no está en PATH")

directorios = subprocess.run(["rclone", "listremotes"], capture_output=True, text=True)

cmd = input("Que quieres hacer (copy/move): ")
dir1 = input("dir 1: ")
dir2 = input("dir2: ")
result = subprocess.run(["rclone", f"{cmd}", f"{dir1}", f"{dir2}", "--progress", "--ignore-existing"], capture_output=True, text=True)

print(result.stdout) #Captura de salida
print(result.stderr) #Captura de errores

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