from guizero import *
from operaciones import *

def cambio_ventana(ventana_abrir,ventana_cerrar):
    ventana_cerrar.hide()
    ventana_abrir.show()

def cierre_programa():
    Aplicacion.after(1500,Aplicacion.destroy)

Aplicacion= App(title="Rclone visual",layout="grid",width=400,height=500)
Aplicacion.tk.columnconfigure(0, weight=1)
Aplicacion.tk.columnconfigure(1, weight=2)
Aplicacion.tk.columnconfigure(2, weight=1)
T_titulo=Text(Aplicacion,text="Rclone visual",size=20,grid=[1,0])
T_titulo.tk.configure(pady=70)
B_Config=PushButton(Aplicacion,text="Config",command=lambda:cambio_ventana(W_Config,Aplicacion),width=15,grid=[1,1])
Box(Aplicacion,height=15,grid=[1,2])
B_Copy_Move=PushButton(Aplicacion,text="Copy/Move",command=lambda:cambio_ventana(W_Copy_Move,Aplicacion),width=15,grid=[1,3])
Box(Aplicacion,height=30,grid=[1,4])
B_cierre=PushButton(Aplicacion,text="Cerrar programa",command=cierre_programa,grid=[1,5])


W_Config=Window(Aplicacion,title="Config",visible=False,width=700)
Bx_Config=Box(W_Config,layout="grid")
Bx_Config.tk.columnconfigure(0, weight=1)
Bx_Config.tk.columnconfigure(1, weight=0, minsize=200)
Bx_Config.tk.columnconfigure(2, weight=1)
Config_box_izq=Box(Bx_Config,layout="grid", grid=[0,0])
Config_box_der=Box(Bx_Config,layout="grid", grid=[2,0])
T_nombre_repo=Text(Config_box_izq,text="Nombre del repositorio",grid=[0,0],align="left")
Tb_nombre_repo=TextBox(Config_box_izq,grid=[1,0],align="left",width=30)
T_url=Text(Config_box_izq,text="Direccion del sharepoint",grid=[0,1],align="left")
Tb_url=TextBox(Config_box_izq,grid=[1,1],align="left",width=30)
B_anadir_repo=PushButton(Bx_Config, text="Añadir repos.", command=lambda:config(Tb_nombre_repo.value, Tb_url.value))
T_prueba=Text(Config_box_der,text="Texto de prueba",grid=[1,2],align="left")
B_volvel_config=PushButton(W_Config,text="Inicio",align="bottom",command=lambda: cambio_ventana(Aplicacion,W_Config))

W_Copy_Move=Window(Aplicacion,title="Copy/Move",visible=False,layout="grid")
B_Volver_CM=PushButton(W_Copy_Move,text="Inicio",command=lambda: cambio_ventana(Aplicacion,W_Copy_Move),align="bottom",grid=[0,2])



Aplicacion.display()