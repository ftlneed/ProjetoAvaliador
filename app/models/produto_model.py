
from app.models.user_model import conectar

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def adicionar_produto(nome, preco, estoque):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)", (nome, preco, estoque))
    conn.commit()
    conn.close()
