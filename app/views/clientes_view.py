
from tkinter import *
from app.controllers.cliente_controller import cadastrar_cliente, buscar_clientes

def abrir_tela_clientes(master):
    win = Toplevel(master)
    win.title("Cadastro de Clientes")
    win.geometry("400x300")

    nome = Entry(win)
    telefone = Entry(win)
    nome.pack(); telefone.pack()

    def salvar():
        cadastrar_cliente(nome.get(), telefone.get())
        nome.delete(0, END); telefone.delete(0, END)

    Button(win, text="Cadastrar", command=salvar).pack()

    for c in buscar_clientes():
        Label(win, text=f"{c[1]} - Tel: {c[2]}").pack()
