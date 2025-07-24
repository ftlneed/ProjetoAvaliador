
from tkinter import *
from app.controllers.produto_controller import controller_listar_produtos, controller_adicionar_produto

class ProdutoView(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastro de Produtos")
        self.geometry("500x400")
        self.criar_widgets()
        self.listar()

    def criar_widgets(self):
        Label(self, text="Nome").pack()
        self.nome = Entry(self)
        self.nome.pack()

        Label(self, text="Preço").pack()
        self.preco = Entry(self)
        self.preco.pack()

        Label(self, text="Estoque").pack()
        self.estoque = Entry(self)
        self.estoque.pack()

        Button(self, text="Salvar", command=self.salvar_produto).pack(pady=10)
        self.lista = Text(self, height=10)
        self.lista.pack(fill=BOTH, expand=True)

    def salvar_produto(self):
        controller_adicionar_produto(
            self.nome.get(),
            float(self.preco.get()),
            int(self.estoque.get())
        )
        self.nome.delete(0, END)
        self.preco.delete(0, END)
        self.estoque.delete(0, END)
        self.listar()

    def listar(self):
        self.lista.delete("1.0", END)
        produtos = controller_listar_produtos()
        for p in produtos:
            self.lista.insert(END, f"{p[0]} - {p[1]} | R${p[2]:.2f} | Estoque: {p[3]}")
