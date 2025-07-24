
from tkinter import *
from app.controllers.produto_controller import cadastrar_produto, buscar_produtos

def abrir_tela_produtos(master):
    win = Toplevel(master)
    win.title("Cadastro de Produtos")
    win.geometry("400x300")

    nome = Entry(win)
    preco = Entry(win)
    estoque = Entry(win)
    nome.pack(); preco.pack(); estoque.pack()

    def salvar():
        cadastrar_produto(nome.get(), float(preco.get()), int(estoque.get()))
        nome.delete(0, END); preco.delete(0, END); estoque.delete(0, END)
    
    Button(win, text="Cadastrar", command=salvar).pack()

    for p in buscar_produtos():
        Label(win, text=f"{p[1]} - R${p[2]} - Estoque: {p[3]}").pack()
