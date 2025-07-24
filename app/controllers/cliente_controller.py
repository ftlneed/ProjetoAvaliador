
from app.models.cliente_model import inserir_cliente, listar_clientes

def cadastrar_cliente(nome, telefone):
    inserir_cliente(nome, telefone)

def buscar_clientes():
    return listar_clientes()
