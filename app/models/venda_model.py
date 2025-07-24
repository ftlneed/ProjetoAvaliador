from utils.db import conectar

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM clientes")
    dados = cursor.fetchall()
    conn.close()
    return dados

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, preco FROM produtos")
    dados = cursor.fetchall()
    conn.close()
    return dados

def inserir_venda(cliente_id, itens, total):
    conn = conectar()
    cursor = conn.cursor()

    # Inserir a venda
    cursor.execute("INSERT INTO vendas (cliente_id, total) VALUES (%s, %s)", (cliente_id, total))
    venda_id = cursor.lastrowid

    # Inserir os itens da venda
    for produto_id, quantidade, preco_unitario in itens:
        cursor.execute("""
            INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario)
            VALUES (%s, %s, %s, %s)
        """, (venda_id, produto_id, quantidade, preco_unitario))

    conn.commit()
    conn.close()
    return venda_id
