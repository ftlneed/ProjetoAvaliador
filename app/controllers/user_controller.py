
from app.models.user_model import validar_login

def autenticar_usuario(email, senha):
    return validar_login(email, senha)
