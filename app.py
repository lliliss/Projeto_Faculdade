import tkinter as tk
from tkinter import messagebox
import random

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.numero_serie = None

    def gerar_numero_serie(self):
        pass  # Implemente a geração de número de série para cada tipo de produto

class Camisa(Produto):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def gerar_numero_serie(self):
        return random.choice(range(5, 100, 5))

class Caneca(Produto):
    def __init__(self, nome, preco, capacidade):
        super().__init__(nome, preco)
        self.capacidade = capacidade

    def gerar_numero_serie(self):
        return random.choice(range(3, 100, 3))

class Quadrinho(Produto):
    def __init__(self, nome, preco, autor, editora):
        super().__init__(nome, preco)
        self.autor = autor
        self.editora = editora

    def gerar_numero_serie(self):
        return random.choice(range(7, 100, 7))

class LojaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Loja Nerd/Geek")
        self.root.geometry("200x200+250+200")

        self.carrinho = []

        # Adicione widgets, botões e campos de entrada conforme necessário
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.pack()

        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_preco = tk.Label(root, text="Preço:")
        self.label_preco.pack()

        self.entry_preco = tk.Entry(root)
        self.entry_preco.pack()

        self.label_quantidade = tk.Label(root, text="Quantidade:")
        self.label_quantidade.pack()

        self.entry_quantidade = tk.Entry(root)
        self.entry_quantidade.pack()

        self.botao_adicionar = tk.Button(root, text="Adicionar ao Carrinho", command=self.adicionar_ao_carrinho)
        self.botao_adicionar.pack()

        self.botao_finalizar_compra = tk.Button(root, text="Finalizar Compra", command=self.finalizar_compra)
        self.botao_finalizar_compra.pack()

    def adicionar_ao_carrinho(self):
        # Implemente a lógica para adicionar o produto ao carrinho
        pass

    def finalizar_compra(self):
        # Implemente a lógica para finalizar a compra e imprimir a nota fiscal
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = LojaApp(root)
    root.mainloop()