from models.usuario_model import UsuarioModel

class LoginController:
    def __init__(self, app, view):
        self.app = app
        self.view = view

    def autenticar(self, email, senha):
        usuario = UsuarioModel.autenticar(email, senha)
        if usuario:
            self.app.show_dashboard()
        else:
            self.view.mostrar_erro("Login ou senha incorretos.")