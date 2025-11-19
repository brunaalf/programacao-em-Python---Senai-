import tkinter as tk


def mostrar_resultado_soma():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma  = n1_ +  n2_
    resultado.config(text=soma) 

def mostrar_resultado_sub():
    n3_ = float(n1.get())
    n4_ = float(n2.get())
    subtração  = n3_ -  n4_
    resultado.config(text=subtração) 

def mostrar_resultado_mult():
    n5_ = float(n1.get())
    n6_ = float(n2.get())
    multiplicacao  = n5_ *  n6_
    resultado.config(text=multiplicacao) 

def mostrar_resultado_div():
    n7_ = float(n1.get())
    n8_ = float(n2.get())
    divisao  = n7_ /  n8_
    resultado.config(text=divisao) 

root = tk.Tk()
root.geometry('250x370')


n1_label =  tk.Label(root, text='N1', font=('arial',12))
n1_label.grid(pady=5, column=1, row =1 )

n1 =  tk.Entry(root, font=('arial',12))
n1.grid(row=1, column=2, padx=5)

n2_label =  tk.Label(root, text='N2', font=('arial',12))
n2_label.grid(pady=5, column=1, row =3 )

n2 =  tk.Entry(root, font=('arial',12))
n2.grid(row=3, column=2, padx=5)

btn_soma =  tk.Button(root, text= '+', font=('arial',50), command=mostrar_resultado_soma)
btn_soma.grid(row=5, column= 1, pady=1)

btn_sub = tk.Button(root, text = '-', font = ('arial', 50), command=mostrar_resultado_sub)
btn_sub.grid(row=5, column= 2, pady=7)

btn_mult = tk.Button(root, text = 'X', font = ('arial', 50), command=mostrar_resultado_mult)
btn_mult.grid(row=6, column= 1, pady=5)

btn_div = tk.Button(root, text = '/', font = ('arial', 50), command=mostrar_resultado_div)
btn_div.grid(row=6, column= 2, pady=5)

resultado =  tk.Label(root, text = '=', font=('arial',12))
resultado.grid(row = 8, column=7)

root.mainloop()
