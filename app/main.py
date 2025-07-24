import tkinter as tk
from tkinter import messagebox, ttk

# Dados dos jogos com estoque
games = [
    {"nome": "The Witcher 3", "preco": 120, "estoque": 5},
    {"nome": "Cyberpunk 2077", "preco": 150, "estoque": 3},
    {"nome": "Minecraft", "preco": 80, "estoque": 10},
    {"nome": "FIFA 23", "preco": 200, "estoque": 4},
    {"nome": "God of War", "preco": 180, "estoque": 2},
]

# Lista de clientes cadastrados
clientes = []

# Usuário e senha fixos para exemplo
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Loja de Games")
        self.root.geometry("300x180")
        self.root.configure(bg="#222831")
        self.root.resizable(False, False)

        tk.Label(root, text="Usuário:", bg="#222831", fg="white", font=("Segoe UI", 12)).pack(pady=(20, 5))
        self.entry_usuario = tk.Entry(root, font=("Segoe UI", 12))
        self.entry_usuario.pack()

        tk.Label(root, text="Senha:", bg="#222831", fg="white", font=("Segoe UI", 12)).pack(pady=(10, 5))
        self.entry_senha = tk.Entry(root, font=("Segoe UI", 12), show="*")
        self.entry_senha.pack()

        self.btn_login = tk.Button(root, text="Entrar", bg="#00ADB5", fg="white", font=("Segoe UI", 12), command=self.checar_login)
        self.btn_login.pack(pady=15)

        # Enter tecla para login
        self.root.bind('<Return>', lambda event: self.checar_login())

    def checar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            # Fecha a janela de login e abre a loja
            self.root.destroy()
            abrir_loja()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

class CadastroClientes(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Cadastro de Clientes")
        self.geometry("400x300")
        self.configure(bg="#222831")

        tk.Label(self, text="Nome:", bg="#222831", fg="white", font=("Segoe UI", 12)).pack(pady=(20, 5))
        self.entry_nome = tk.Entry(self, font=("Segoe UI", 12))
        self.entry_nome.pack(padx=20)

        tk.Label(self, text="Email:", bg="#222831", fg="white", font=("Segoe UI", 12)).pack(pady=(15, 5))
        self.entry_email = tk.Entry(self, font=("Segoe UI", 12))
        self.entry_email.pack(padx=20)

        tk.Label(self, text="Telefone:", bg="#222831", fg="white", font=("Segoe UI", 12)).pack(pady=(15, 5))
        self.entry_telefone = tk.Entry(self, font=("Segoe UI", 12))
        self.entry_telefone.pack(padx=20)

        self.btn_cadastrar = tk.Button(self, text="Cadastrar", bg="#00ADB5", fg="white", font=("Segoe UI", 12), command=self.cadastrar_cliente)
        self.btn_cadastrar.pack(pady=20)

    def cadastrar_cliente(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        telefone = self.entry_telefone.get().strip()

        if not nome or not email or not telefone:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return
        
        clientes.append({"nome": nome, "email": email, "telefone": telefone})
        messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado com sucesso!")
        self.destroy()

class LojaGames:
    def __init__(self, root):
        self.root = root
        self.root.title("Loja de Games")
        self.root.geometry("800x450")
        self.root.configure(bg="#222831")

        self.carrinho = []

        # Style ttk
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview",
                        background="#393E46",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#393E46",
                        font=("Segoe UI", 10))
        style.map('Treeview', background=[('selected', '#00ADB5')])

        style.configure("TButton",
                        font=("Segoe UI", 10),
                        background="#00ADB5",
                        foreground="white")
        style.map("TButton",
                  background=[('active', '#007f87')])

        style.configure("TLabel",
                        background="#222831",
                        foreground="white",
                        font=("Segoe UI", 12))

        # Frame topo - botões cadastro cliente e logout
        frame_top = tk.Frame(root, bg="#222831")
        frame_top.pack(fill=tk.X, padx=20, pady=5)

        btn_cadastro = ttk.Button(frame_top, text="Cadastro de Clientes", command=self.abrir_cadastro)
        btn_cadastro.pack(side=tk.LEFT)

        btn_logout = ttk.Button(frame_top, text="Logout", command=self.fazer_logout)
        btn_logout.pack(side=tk.RIGHT)

        # Frame de busca
        self.frame_busca = tk.Frame(root, bg="#222831")
        self.frame_busca.pack(pady=10, fill=tk.X, padx=20)

        tk.Label(self.frame_busca, text="Buscar jogo:", font=("Segoe UI", 12), bg="#222831", fg="white").pack(side=tk.LEFT, padx=(0, 10))
        self.entry_busca = tk.Entry(self.frame_busca, font=("Segoe UI", 12), width=30)
        self.entry_busca.pack(side=tk.LEFT, padx=(0, 10))
        self.entry_busca.bind("<KeyRelease>", self.atualizar_lista_jogos)

        # Frame principal
        self.frame_main = tk.Frame(root, bg="#222831")
        self.frame_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Frame dos jogos
        self.frame_games = tk.LabelFrame(self.frame_main, text="Jogos Disponíveis", bg="#222831", fg="white", font=("Segoe UI", 14, "bold"))
        self.frame_games.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        self.tree_games = ttk.Treeview(self.frame_games, columns=("Título", "Preço", "Estoque"), show="headings", selectmode="browse")
        self.tree_games.heading("Título", text="Título")
        self.tree_games.heading("Preço", text="Preço (R$)")
        self.tree_games.heading("Estoque", text="Estoque")
        self.tree_games.column("Título", width=200, anchor=tk.W)
        self.tree_games.column("Preço", width=80, anchor=tk.CENTER)
        self.tree_games.column("Estoque", width=80, anchor=tk.CENTER)
        self.tree_games.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.btn_add = ttk.Button(self.frame_games, text="Adicionar ao Carrinho", command=self.adicionar_carrinho)
        self.btn_add.pack(pady=5)

        # Frame do carrinho
        self.frame_carrinho = tk.LabelFrame(self.frame_main, text="Carrinho", bg="#222831", fg="white", font=("Segoe UI", 14, "bold"))
        self.frame_carrinho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.tree_carrinho = ttk.Treeview(self.frame_carrinho, columns=("Preço"), show="headings", selectmode="browse")
        self.tree_carrinho.heading("Preço", text="Preço (R$)")
        self.tree_carrinho.column("Preço", width=80, anchor=tk.CENTER)
        self.tree_carrinho.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.btn_remover = ttk.Button(self.frame_carrinho, text="Remover do Carrinho", command=self.remover_carrinho)
        self.btn_remover.pack(pady=(0,10))

        self.label_total = ttk.Label(self.frame_carrinho, text="Total: R$ 0", font=("Segoe UI", 14, "bold"))
        self.label_total.pack(pady=5)

        self.btn_finalizar = ttk.Button(self.frame_carrinho, text="Finalizar Compra", command=self.finalizar_compra)
        self.btn_finalizar.pack(pady=5)

        self.atualizar_lista_jogos()

    def abrir_cadastro(self):
        CadastroClientes(self.root)

    def fazer_logout(self):
        self.root.destroy()
        main()

    def atualizar_lista_jogos(self, event=None):
        busca = self.entry_busca.get().lower()
        self.tree_games.delete(*self.tree_games.get_children())
        for game in games:
            if busca in game["nome"].lower():
                preco_str = f"{game['preco']:.2f}"
                self.tree_games.insert("", tk.END, iid=game["nome"],
                                       values=(game["nome"], preco_str, game["estoque"]))

    def adicionar_carrinho(self):
        selecionado = self.tree_games.selection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um jogo para adicionar ao carrinho.")
            return
        nome = selecionado[0]
        game = next(g for g in games if g["nome"] == nome)

        if game["estoque"] <= 0:
            messagebox.showerror("Sem estoque", f"O jogo '{game['nome']}' está sem estoque.")
            return

        # Adiciona ao carrinho e decrementa estoque temporariamente
        self.carrinho.append(game)
        game["estoque"] -= 1
        self.atualizar_carrinho()
        self.atualizar_lista_jogos()
        self.atualizar_total()

    def remover_carrinho(self):
        selecionado = self.tree_carrinho.selection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um jogo para remover do carrinho.")
            return
        nome = selecionado[0]

        # Remove o primeiro jogo encontrado com esse nome no carrinho
        for i, game in enumerate(self.carrinho):
            if game["nome"] == nome:
                self.carrinho.pop(i)
                # Retorna estoque
                for g in games:
                    if g["nome"] == nome:
                        g["estoque"] += 1
                        break
                break
        self.atualizar_carrinho()
        self.atualizar_lista_jogos()
        self.atualizar_total()

    def atualizar_carrinho(self):
        self.tree_carrinho.delete(*self.tree_carrinho.get_children())
        for game in self.carrinho:
            preco_str = f"{game['preco']:.2f}"
            self.tree_carrinho.insert("", tk.END, iid=game["nome"], values=(preco_str,))

    def atualizar_total(self):
        total = sum(item['preco'] for item in self.carrinho)
        self.label_total.config(text=f"Total: R$ {total:.2f}")

    def finalizar_compra(self):
        if not self.carrinho:
            messagebox.showinfo("Carrinho vazio", "Adicione jogos ao carrinho antes de finalizar a compra.")
            return
        total = sum(item['preco'] for item in self.carrinho)
        messagebox.showinfo("Compra Finalizada", f"Compra realizada com sucesso!\nTotal: R$ {total:.2f}")

        # Carrinho limpado e estoque já atualizado, só limpar lista
        self.carrinho.clear()
        self.atualizar_carrinho()
        self.atualizar_total()
        self.atualizar_lista_jogos()

def abrir_loja():
    root = tk.Tk()
    loja = LojaGames(root)
    root.mainloop()

def main():
    root_login = tk.Tk()
    login = LoginWindow(root_login)
    root_login.mainloop()

if __name__ == "__main__":
    main()
