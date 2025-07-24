
from app.models.venda_model import inserir_venda, listar_clientes, listar_produtos

def registrar_venda(cliente_id, itens):
    total = sum(qtd * preco for _, qtd, preco in itens)
    venda_id = inserir_venda(cliente_id, itens, total)
    return venda_id

def get_clientes():
    return listar_clientes()

def get_produtos():
    return listar_produtos()
