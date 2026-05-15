from guizero import *

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
B_cierre=PushButton(Aplicacion,text="Cerrar programa",align="bottom",command=cierre_programa,grid=[1,5])


W_Config=Window(Aplicacion,visible=False)
B_Volver_cnf=PushButton(W_Config,text="Inicio", command=lambda: cambio_ventana(Aplicacion,W_Config),align="bottom")

W_Copy_Move=Window(Aplicacion,title="Copy/Move",visible=False)
B_Volver_CM=PushButton(W_Copy_Move,text="Inicio",command=lambda: cambio_ventana(Aplicacion,W_Copy_Move),align="bottom")



Aplicacion.display()