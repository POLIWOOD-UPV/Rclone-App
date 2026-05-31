from guizero import *
from operaciones import *

def cambio_ventana(ventana_abrir,ventana_cerrar):
    ventana_cerrar.hide()
    ventana_abrir.show()

def cierre_programa():
    Aplicacion.after(1500,Aplicacion.destroy)
    
def anadir_repo(nombre_r, url_r):
    if config(nombre_r,url_r):
        info("Exito", "Se ha añadido se repositorio. Compruebe que funciona con rclone config en la consola.")

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


W_Config=Window(Aplicacion,title="Config",visible=False)
T_nombre_repo=Text(W_Config,text="Nombre del repositorio")
Tb_nombre_repo=TextBox(W_Config,width=30)
Text(W_Config,text=" ")
T_url=Text(W_Config,text="Direccion del sharepoint")
Tb_url=TextBox(W_Config,width=30)
Text(W_Config,text=" ")
B_anadir_repo=PushButton(W_Config, text="Añadir repos.", command=lambda:anadir_repo(Tb_nombre_repo.value, Tb_url.value))
B_volvel_config=PushButton(W_Config,text="Inicio",align="bottom",command=lambda: cambio_ventana(Aplicacion,W_Config))

W_Copy_Move=Window(Aplicacion,title="Copy/Move",visible=False)
Text(W_Copy_Move,text=" ")
T_dir1=Text(W_Copy_Move,text="Direccion de donde estan los archivos")
Tb_dir1=TextBox(W_Copy_Move, width=50)
Text(W_Copy_Move,text=" ")
T_dir2=Text(W_Copy_Move,text="Direccion hacia donde copiar/mover")
Tb_dir2=TextBox(W_Copy_Move,width=50)
Text(W_Copy_Move,text=" ")
Bx_cm=Box(W_Copy_Move,layout="grid")
B_copy=PushButton(Bx_cm, text="Copiar",width=15, command=lambda: copy_move("copy", Tb_dir1.value, Tb_dir2.value),grid=[0,0])
Text(Bx_cm,text="   ",grid=[1,0])
B_move=PushButton(Bx_cm, text="Mover",width=15, command=lambda: copy_move("move", Tb_dir1.value, Tb_dir2.value),grid=[2,0])

B_Volver_CM=PushButton(W_Copy_Move,text="Inicio",command=lambda: cambio_ventana(Aplicacion,W_Copy_Move),align="bottom")



Aplicacion.display()