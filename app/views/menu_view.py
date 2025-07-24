
from tkinter import *
from app.views.produtos_view import abrir_tela_produtos
from app.views.clientes_view import abrir_tela_clientes
from app.views.vendas_view import abrir_tela_vendas

def abrir_menu(master):
    win = Toplevel(master)
    win.title("Menu Principal")
    win.geometry("300x250")

    Button(win, text="Produtos", command=lambda: abrir_tela_produtos(win)).pack(pady=10)
    Button(win, text="Clientes", command=lambda: abrir_tela_clientes(win)).pack(pady=10)
    Button(win, text="Vendas", command=lambda: abrir_tela_vendas(win)).pack(pady=10)
