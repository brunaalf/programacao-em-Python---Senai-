
# **ATIVIDADE 2** 

# Crie um formulário em Tkinter, contendo, nome, idade, e-mail, endereço, celular.
# Problema: Sistema de Cadastro de Clientes

# Você é um desenvolvedor de software e foi contratado por uma empresa de serviços para criar um sistema de cadastro de clientes. O sistema deve permitir que os clientes forneçam suas informações pessoais, como nome, idade, e-mail, endereço, celular...

# ***Atividade:***
# Crie um formulário em Tkinter que contenha os seguintes campos:
# Nome
# Idade
# E-mail
# Endereço
# Celular
# Cep
# Cidade
# Cursos
# O formulário deve ter um botão de "Enviar" que, quando clicado, imprima as informações do cliente na console.


import tkinter as tk
from tkinter import messagebox


def enviar():
    nome = n1.get()
    print(nome)
    idade = n2.get()
    print(idade)
    email = n3.get()
    print(email)
    end = n4.get()
    print (end)
    cel = n5.get()
    print(cel)
    cep = n6.get()
    print(cep)
    cidade = n7.get()
    print(cidade)
    curso = n8.get()
    print(curso)


    # resultado1.config(text=nome) 
    # resultado2.config(text=idade) 
    # resultado3.config(text=email) 
    # resultado4.config(text=end)
    # resultado5.config(text=cel) 
    # resultado6.config(text=cep)
    # resultado7.config(text=cidade) 
    # resultado8.config(text=curso)
root = tk.Tk()
root.title ("Sistema de Cadastro de Clientes")
root.geometry('1700x750')

nome_label =  tk.Label(root, text='NOME', font=('Segoe UI',10))
nome_label.grid(pady=10, column=1, row =1 )

n1 =  tk.Entry(root, font=('Segoe UI',12))
n1.grid(row=1, column=2, padx=5)


idade_label =  tk.Label(root, text='IDADE', font=('Segoe UI',10))
idade_label.grid(pady=10, column=1, row =2 )

n2 =  tk.Entry(root, font=('Segoe UI',12))
n2.grid(row=2, column=2, padx=5)


email_label =  tk.Label(root, text='E-MAIL', font=('Segoe UI',10))
email_label.grid(pady=10, column=1, row =3 )

n3 =  tk.Entry(root, font=('Segoe UI',12))
n3.grid(row=3, column=2, padx=5)


end_label =  tk.Label(root, text='ENDEREÇO', font=('Segoe UI',10))
end_label.grid(pady=10, column=1, row =4 )

n4 =  tk.Entry(root, font=('Segoe UI',12))
n4.grid(row=4, column=2, padx=5)


cel_label =  tk.Label(root, text='CELULAR', font=('Segoe UI',10))
cel_label.grid(pady=10, column=1, row =5 )

n5 =  tk.Entry(root, font=('Segoe UI',12))
n5.grid(row=5, column=2, padx=5)


cep_label =  tk.Label(root, text='CEP', font=('Segoe UI',10))
cep_label.grid(pady=10, column=1, row =6 )

n6 =  tk.Entry(root, font=('Segoe UI',12))
n6.grid(row=6, column=2, padx=5)


cidade_label =  tk.Label(root, text='CIDADE', font=('Segoe UI',10))
cidade_label.grid(pady=10, column=1, row =7 )

n7 =  tk.Entry(root, font=('Segoe UI',12))
n7.grid(row=7, column=2, padx=5)


curso_label =  tk.Label(root, text='CURSOS', font=('Segoe UI',10))
curso_label.grid(pady=10, column=1, row =8 )

n8 =  tk.Entry(root, font=('Segoe UI',12))
n8.grid(row=8, column=2, padx=5)

enter =  tk.Button(root, text= 'ENVIAR', font=('Segoe UI',10), command=enviar)
enter.grid(row=9, column= 2, pady=1)


root.mainloop()

# resultado1 =  tk.Label(root, font=('arial',12))
# resultado1.grid(row = 10, column=2)

# resultado2 =  tk.Label(root, font=('arial',12))
# resultado2.grid(row = 11, column=2)

# resultado3 =  tk.Label(root,  font=('arial',12))
# resultado3.grid(row = 12, column=2)

# resultado4 =  tk.Label(root, font=('arial',12))
# resultado4.grid(row = 13, column=2)

# resultado5 =  tk.Label(root,  font=('arial',12))
# resultado5.grid(row = 14, column=2)

# resultado6 =  tk.Label(root, font=('arial',12))
# resultado6.grid(row = 15, column=2)

# resultado7 =  tk.Label(root,  font=('arial',12))
# resultado7.grid(row = 16, column=2)

# resultado8 =  tk.Label(root,  font=('arial',12))
# resultado8.grid(row = 17, column=2)

# enviar()
# root.mainloop()