
from tkinter import *
from tkinter import ttk, messagebox
from app.controllers.venda_controller import get_clientes, get_produtos, registrar_venda

def abrir_tela_vendas(master):
    win = Toplevel(master)
    win.title("Registrar Venda")
    win.geometry("500x500")

    clientes = get_clientes()
    produtos = get_produtos()
    itens = []

    Label(win, text="Cliente:").pack()
    cb_cliente = ttk.Combobox(win, values=[f"{c[0]} - {c[1]}" for c in clientes])
    cb_cliente.pack()

    Label(win, text="Produto:").pack()
    cb_produto = ttk.Combobox(win, values=[f"{p[0]} - {p[1]} - R${p[2]:.2f}" for p in produtos])
    cb_produto.pack()

    Label(win, text="Quantidade:").pack()
    ent_qtd = Entry(win)
    ent_qtd.pack()

    lst_itens = Listbox(win)
    lst_itens.pack(pady=10, fill=BOTH, expand=True)

    def adicionar_item():
        if not cb_produto.get() or not ent_qtd.get().isdigit():
            return
        index = cb_produto.current()
        produto = produtos[index]
        quantidade = int(ent_qtd.get())
        preco_unitario = produto[2]
        itens.append((produto[0], quantidade, preco_unitario))
        lst_itens.insert(END, f"{produto[1]} x{quantidade} - R${quantidade * preco_unitario:.2f}")
        ent_qtd.delete(0, END)

    def concluir_venda():
        if not cb_cliente.get() or not itens:
            messagebox.showerror("Erro", "Preencha cliente e itens")
            return
        cliente_id = int(cb_cliente.get().split(" - ")[0])
        venda_id = registrar_venda(cliente_id, itens)
        messagebox.showinfo("Sucesso", f"Venda registrada com ID {venda_id}")
        win.destroy()

    Button(win, text="Adicionar Item", command=adicionar_item).pack()
    Button(win, text="Concluir Venda", command=concluir_venda).pack(pady=10)
