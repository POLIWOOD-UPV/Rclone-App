from guizero import *

def abrir_config():
    Aplicacion.hide()
    Config_w.show()

Aplicacion= App(title="Rclone visual")
Config_btt=PushButton(Aplicacion,command=abrir_config)

Config_w=Window(Aplicacion,visible=False)

