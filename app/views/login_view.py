import tkinter as tk
from tkinter import messagebox
from controllers.login_controller import LoginController

class LoginView(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.controller = LoginController(app, self)

        tk.Label(self, text="Login de Usuário", font=("Arial", 18)).pack(pady=20)

        tk.Label(self, text="Email:").pack()
        self.email_entry = tk.Entry(self, width=30)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Senha:").pack()
        self.senha_entry = tk.Entry(self, show="*", width=30)
        self.senha_entry.pack(pady=5)

        tk.Button(self, text="Entrar", command=self.login).pack(pady=20)

    def login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        self.controller.autenticar(email, senha)

    def mostrar_erro(self, mensagem):
        messagebox.showerror("Erro de Login", mensagem)
