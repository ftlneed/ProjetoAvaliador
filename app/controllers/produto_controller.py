
from app.models.produto_model import listar_produtos, adicionar_produto

def controller_listar_produtos():
    return listar_produtos()

def controller_adicionar_produto(nome, preco, estoque):
    adicionar_produto(nome, preco, estoque)
