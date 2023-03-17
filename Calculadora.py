from tkinter import *  #Importamos la libreria con todos sus modulos
import keyboard

caracteres_validos = ['0','1','2','3','4','5','6','7','8','9','+','**','*','-','/','*','%','(',')','.']
caracteres_invalidos = [(12,13),(15,27),(29,41),(43,52),(55,151)] #Rango de los valores de los caracteres invalidas
i=0

#----------------------- Bloqueo los caracteres invalidos -----------------------

#Recorremos para bloquear todas las input_key que esten en dichos rangos.

keyboard.block_key(0) 
keyboard.block_key(1)

for index in range(len(caracteres_invalidos)):
    for c in range(int(caracteres_invalidos[index][0]),int(caracteres_invalidos[index][1])):
        keyboard.block_key(c)
        
#----------------------- Declaramos funciones -----------------------

def obtener_valor(caracter): #Para insertar los valores
    global i 
    resultado.insert(i,caracter)
    i+=1
    
def operar(): #Realizamos las operaciones 
    valor = resultado.get()
    try:
        expresion =  compile(valor, 'Resultado', 'eval') 
        resultado_aux = eval(expresion)
        resultado.delete(0,END)
        resultado.insert(0,resultado_aux)
    except:
        resultado.delete(0,END)
        resultado.insert(0,"Error")
        
def verificar_input(): #Eliminamos algun caracter no permitido si lo ingresa
    global i 
    resultado_aux = resultado.get()
    for n in resultado_aux:  
        if n not in caracteres_validos:
            resultado.delete(len(resultado_aux)-1,END) 
    i+=1
 
#----------------------- Creamos la pantalla -----------------------

window = Tk() #Creamos ventana
window.title("Calc")
window.geometry("207x305") 
window.resizable(width=False, height=False)   

#Creamos el textbox  
resultado = Entry(window,font="Arial",border="3")
resultado.grid(row=1,columnspan=4,sticky=EW) 
resultado.bind('<KeyRelease>', lambda e:verificar_input())   

#Botones - Numeros

btn_0  = Button(window,text='0',width=6,height=3,command=lambda:obtener_valor(0)).grid(row=5,column=1)
btn_1  = Button(window,text='1',width=6,height=3,command=lambda:obtener_valor(1)).grid(row=4,column=0)
btn_2  = Button(window,text='2',width=6,height=3,command=lambda:obtener_valor(2)).grid(row=4,column=1)
btn_3  = Button(window,text='3',width=6,height=3,command=lambda:obtener_valor(3)).grid(row=4,column=2)
btn_4  = Button(window,text='4',width=6,height=3,command=lambda:obtener_valor(4)).grid(row=3,column=0)
btn_5  = Button(window,text='5',width=6,height=3,command=lambda:obtener_valor(5)).grid(row=3,column=1)
btn_6  = Button(window,text='6',width=6,height=3,command=lambda:obtener_valor(6)).grid(row=3,column=2)
btn_7  = Button(window,text='7',width=6,height=3,command=lambda:obtener_valor(7)).grid(row=2,column=0)
btn_8  = Button(window,text='8',width=6,height=3,command=lambda:obtener_valor(8)).grid(row=2,column=1)
btn_9  = Button(window,text='9',width=6,height=3,command=lambda:obtener_valor(9)).grid(row=2,column=2)

#Botones - Operadores

btn_AC = Button(window,text='AC',width=6,height=3,command=lambda:resultado.delete(0,END)).grid(row=5,column=0)
btn_exp = Button(window,text='EXP',width=6,height=3,command=lambda:obtener_valor('**')).grid(row=5,column=2)
btn_r  = Button(window,text='-',width=6,height=3,command=lambda:obtener_valor('-')).grid(row=5,column=3)
btn_s  = Button(window,text='+',width=6,height=3,command=lambda:obtener_valor('+')).grid(row=4,column=3)
btn_m  = Button(window,text='*',width=6,height=3,command=lambda:obtener_valor('*')).grid(row=3,column=3)
btn_d  = Button(window,text='/',width=6,height=3,command=lambda:obtener_valor('/')).grid(row=2,column=3)
btn_pc = Button(window,text='%',width=6,height=3,command=lambda:obtener_valor('%')).grid(row=6,column=3)
btn_i  = Button(window,text='=',width=6,height=3,command=lambda:operar()).grid(row=6,columnspan=3,sticky=EW)

keyboard.add_hotkey('enter',lambda:operar()) #Habilito el enter para operar

window.mainloop()


    