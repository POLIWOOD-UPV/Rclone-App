from guizero import *

def cambio_ventana(ventana_abrir,ventana_cerrar):
    ventana_cerrar.hide()
    ventana_abrir.show()

def cierre_programa():
    Aplicacion.after(1500,Aplicacion.destroy)

Aplicacion= App(title="Rclone visual")
B_Config=PushButton(Aplicacion,text="Config",command=lambda:cambio_ventana(W_Config,Aplicacion),width=15)
B_Copy_Move=PushButton(Aplicacion,text="Copy/Move",command=lambda:cambio_ventana(W_Copy_Move,Aplicacion),width=15)
B_cierre=PushButton(Aplicacion,text="Cerrar programa",align="bottom",command=cierre_programa)


W_Config=Window(Aplicacion,visible=False)
B_Volver_cnf=PushButton(W_Config,text="Inicio", command=lambda: cambio_ventana(Aplicacion,W_Config),align="bottom")

W_Copy_Move=Window(Aplicacion,title="Copy/Move",visible=False)
B_Volver_CM=PushButton(W_Copy_Move,text="Inicio",command=lambda: cambio_ventana(Aplicacion,W_Copy_Move),align="bottom")



Aplicacion.display()