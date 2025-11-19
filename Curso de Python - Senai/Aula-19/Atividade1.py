import tkinter as tk 
from tkinter import ttk


# capturando um texto do input e mostrando na label embaixo do botão


def display():
    texto  = input_.get()
    texto_3.config(text=texto)



# criando a janela 
janela  = tk.Tk()
janela.geometry('480x768')
janela.configure(bg = 'black')


fr  =  tk.Frame(janela, bg='red')
fr.pack()



arvore =  ttk.Treeview(janela)
arvore.pack()





# inserindo um texto
texto = tk.Label(fr, text = ' Isso é um teste ', font=('arial',16) )
texto.pack()


# inserindo um texto
texto_2 = tk.Label(fr, text = ' Isso é um teste ', font=('arial',16) )
texto_2.pack()


# inserido um input 
input_ = tk.Entry(fr, font=('arial',16))
input_.pack()


# criando um botão
btn  =  tk.Button(janela, text= 'clique aqui', font=('arial',16), command=display)
btn.pack()



texto_3 = tk.Label(janela, text = 'aqui vai aparecer um texto', font=('arial',16) )
texto_3.pack()


# loop da janela
janela.mainloop()