import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter


# ----------------------
#  BANCO DE DADOS
# ----------------------
def conectar():
    return sqlite3.connect('banco.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS cliente(
            cpf TEXT PRIMARY KEY,
            nome TEXT,
            email TEXT,
            perfil TEXT

    )
    ''')
    conn.commit()
    conn.close()

# ----------------------
#  CRUD
# ----------------------
def inserir_cliente():
    cpf = CPF_entry.get()
    nome = nome_entry.get()
    email = email_entry.get()
    perfil = perfil_var.get()

    if cpf and nome and email and perfil:
        conn = conectar()
        c = conn.cursor()
        c.execute("INSERT INTO cliente VALUES (?,?,?,?)", (cpf, nome, email, perfil))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Dados inseridos!')
        mostrar_cliente()
    else:
        messagebox.showwarning('Erro', 'Preencha todos os campos!')


perfil_nomes = {
    "A": "Conservador",
    "B": "Moderado",
    "C": "Agressivo",
    "D": "Não sei"
}


def mostrar_cliente():
    tree.delete(*tree.get_children())

    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM cliente")
    cliente = c.fetchall()
    conn.close()

    for cpf, nome, email, perfil_codigo in cliente:
        perfil_legivel = perfil_nomes.get(perfil_codigo, "Indefinido")
        tree.insert("", "end", values=(cpf, nome, email, perfil_legivel))

def atualizar():
    selecao = tree.selection()
    if not selecao:
        messagebox.showwarning("Erro", "Selecione um registro!")
        return

    cpf_original = tree.item(selecao)["values"][0]
    novo_cpf = CPF_entry.get()
    novo_nome = nome_entry.get()
    novo_email = email_entry.get()
    novo_perfil = perfil_var.get()

    if novo_cpf and novo_nome and novo_email and novo_perfil:
        conn = conectar()
        c = conn.cursor()
        c.execute("""
            UPDATE cliente
            SET cpf=?, nome=?, email=?, perfil=?
            WHERE cpf=?
        """, (novo_cpf, novo_nome, novo_email, novo_perfil, cpf_original))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Registro atualizado!")
        mostrar_cliente()
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")

def delete_cliente():
    selecao = tree.selection()
    if not selecao:
        messagebox.showwarning("Erro", "Selecione um registro!")
        return

    cpf_del = tree.item(selecao)['values'][0]

    conn = conectar()
    c = conn.cursor()
    c.execute("DELETE FROM cliente WHERE cpf=?", (cpf_del,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Registro deletado!")
    mostrar_cliente()


# ----------------------
#  INTERFACE
# ----------------------
janela = tk.Tk()
janela.title("CRUD - Investimentos")
janela.geometry("900x700")
janela.configure(bg="white")


# TÍTULO
tk.Label(janela, text="Recomendação de Investimentos",
         font=("Arial", 20, "bold"), bg="white").pack(pady=20)


# FORMULÁRIO
form_frame = tk.Frame(janela, bg="white")
form_frame.pack(pady=10)

# CPF
tk.Label(form_frame, text="CPF", font=("Arial", 14), bg="white")\
    .grid(row=0, column=0, padx=10, pady=5, sticky="e")

CPF_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
CPF_entry.grid(row=0, column=1, padx=10, pady=5)

# Nome
tk.Label(form_frame, text="Nome", font=("Arial", 14), bg="white")\
    .grid(row=1, column=0, padx=10, pady=5, sticky="e")

nome_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
nome_entry.grid(row=1, column=1, padx=10, pady=5)

# Email
tk.Label(form_frame, text="E-mail", font=("Arial", 14), bg="white")\
    .grid(row=2, column=0, padx=10, pady=5, sticky="e")

email_entry = tk.Entry(form_frame, font=("Arial", 14), width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)


btn_frame = tk.Frame(janela, bg="white")
btn_frame.pack(pady=15)

customtkinter.CTkButton(btn_frame, text='SALVAR', fg_color="#483D8B",
                        width=140, command=inserir_cliente)\
    .grid(row=0, column=0, padx=10)

customtkinter.CTkButton(btn_frame, text='ATUALIZAR', fg_color="#483D8B",
                        width=140, command=atualizar)\
    .grid(row=0, column=1, padx=10)

customtkinter.CTkButton(btn_frame, text='DELETAR', fg_color="#483D8B",
                        width=140, command=delete_cliente)\
    .grid(row=0, column=2, padx=10)


# ----------------------
# SEÇÃO MEU PERFIL
# ----------------------
perfil_label = tk.Label(form_frame, text='Meu Perfil',
                        font=('Arial', 14, "bold"), bg="white")
perfil_label.grid(row=3, column=0, sticky="ne", padx=10, pady=20)

perfil_frame = tk.Frame(form_frame, bg="white")
perfil_frame.grid(row=3, column=1, sticky="w")

perfil_var = tk.StringVar(value="A")

opcoes = [
    ("Conservador", "A"),
    ("Moderado", "B"),
    ("Agressivo", "C"),
    ("Não sei", "D")
]

for texto, valor in opcoes:
    tk.Radiobutton(perfil_frame, text=texto, value=valor,
                   variable=perfil_var, bg="white",
                   font=("Arial", 12)).pack(anchor="w")


# BOTÃO RECOMENDAÇÃO
def verificar_perfil():
    perfil = perfil_var.get()
    resultados = {
        "A": "Perfil Conservador selecionado. Recomanda-se investir em tesouro Direto, ou ativos de curto prazo como LCA,LCI e CDB de boas instituições financeiras",
        "B": "Perfil Moderado selecionado.Recomenda-se investir em Fundos de Renda Fixa, CDB de médio prazo",
        "C": "Perfil Agressivo selecionado. Recomenda-se ter uma parcela diversificada em boas ações, ou fundos de investimentos Multimercado ou de Ações",
        "D": "Recomendamos fazer um teste de perfil, https://brasilqueinveste.b3.com.br/quiz"
    }
    messagebox.showinfo("Recomendação", resultados[perfil])

tk.Button(janela, text="Gerar Recomendação",
          command=verificar_perfil).pack(pady=10)

recomendacoes = {
    "A": "Perfil Conservador: recomenda-se investimentos de baixo risco, como poupança ou tesouro direto.",
    "B": "Perfil Moderado: recomenda-se uma combinação de renda fixa e variável, com risco controlado.",
    "C": "Perfil Agressivo: pode investir em ações, fundos de investimento e ativos de maior risco.",
    "D": "Não sei: faça um teste de perfil para descobrir o melhor investimento para você."
}


def gerar_recomendacao():
    perfil = perfil_var.get()  # pega o valor selecionado no Radiobutton
    texto = recomendacoes.get(perfil, "Perfil não identificado")
    
    # Mostra em messagebox
    messagebox.showinfo("Recomendação", blablablablabalba)

# ----------------------
# TABELA
# ----------------------
colunas = ('CPF', 'NOME', 'EMAIL', 'PERFIL')
table_frame = tk.Frame(janela, bg="white")
table_frame.pack(pady=20)

tree = ttk.Treeview(table_frame, columns=colunas, show="headings", height=12)
tree.grid(row=0, column=0)

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, width=180)

scroll = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scroll.set)
scroll.grid(row=0, column=1, sticky="ns")


# Iniciar
criar_tabela()
mostrar_cliente()
janela.mainloop()
