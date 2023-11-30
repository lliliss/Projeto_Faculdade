from flask import Flask, render_template, request, redirect, url_for, flash
import random, os

app = Flask(__name__)
app.secret_key = "chave_secreta"  # Defina uma chave secreta para o uso do flash

# Defina um filtro personalizado 'instanceof' para verificar a instância de objetos
@app.template_filter('instanceof')
def isinstance_filter(obj, class_name):
    return isinstance(obj, eval(class_name))

# Coletar Itens cadastrados no banco (TXT)
def ler_camisas_txt(nome_arquivo):
    dicionario = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                chave, valor = linha.strip().split('::')
                nome, preco, imagem, tamanho, serie = valor.strip().split(';')
                dicionario.append([nome, float(preco), imagem, tamanho.split(','), int(serie)])
    return dicionario

def ler_canecas_txt(nome_arquivo):
    dicionario = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                chave, valor = linha.strip().split('::')
                nome, preco, imagem, tamanho, serie = valor.strip().split(';')
                dicionario.append([nome, float(preco), imagem, tamanho, int(serie)])
    return dicionario

def ler_quadrinhos_txt(nome_arquivo):
    dicionario = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                chave, valor = linha.strip().split('::')
                nome, preco, imagem, autor, editora, serie = valor.strip().split(';')
                dicionario.append([nome, float(preco), imagem, autor, editora, int(serie)])
    return dicionario

# Salvar Itens cadastrados no banco (TXT)
def salvar_no_arquivo_txt(nome_arquivo, dicionario):
    with open(nome_arquivo, 'w') as arquivo:
        for chave, valor in sorted(dicionario.items()):
            arquivo.write(f"{chave}: {valor}\n")

global n_series
n_series = []

class Produto:
    def __init__(self, nome, preco, imagem):
        self.nome = nome
        self.preco = preco
        self.imagem = imagem

    def gerar_numero_serie(self, base):
        global n_series
        while True:
            num = random.choice(range(base, 100000, base))
            if(num not in n_series):
                self.numero_serie = num
                n_series.append(num)
                break

class Camisa(Produto):
    def __init__(self, valores):
        super().__init__(valores[0], valores[1], valores[2])
        self.tamanho = valores[3]
        if valores[4] == 0:
            self.gerar_numero_serie(5)
        else:
            global n_series
            n_series.append(valores[4])
            self.numero_serie = valores[4]

class Caneca(Produto):
    def __init__(self, valores):
        super().__init__(valores[0], valores[1], valores[2])
        self.capacidade = valores[3]
        if valores[4] == 0:
            self.gerar_numero_serie(3)
        else:
            global n_series
            n_series.append(valores[4])
            self.numero_serie = valores[4]

class Quadrinho(Produto):
    def __init__(self, valores):
        super().__init__(valores[0], valores[1], valores[2])
        self.autor = valores[3]
        self.editora = valores[4]
        if valores[5] == 0:
            self.gerar_numero_serie(7)
        else:
            global n_series
            n_series.append(valores[5])
            self.numero_serie = valores[5]

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        pass  # Implemente a lógica para adicionar o produto ao carrinho

    def finalizar_compra(self):
        pass  # Implemente a lógica para finalizar a compra e gerar a nota fiscal

carrinho = Carrinho()

produtos = []
camisas = []
canecas = []
quadrinhos = []

# Puxar Camisas do banco
auxiliar = ler_camisas_txt(r'data/camisas.txt')
for produto in auxiliar:
    camisas.append(Camisa(produto))
    produtos.append(Camisa(produto))

# Puxar Canecas do banco
auxiliar = ler_canecas_txt(r'data/canecas.txt')
for produto in auxiliar:
    canecas.append(Caneca(produto))
    produtos.append(Caneca(produto))

# Puxar Quadrinhos do banco
auxiliar = ler_quadrinhos_txt(r'data/quadrinhos.txt')
for produto in auxiliar:
    quadrinhos.append(Quadrinho(produto))
    produtos.append(Quadrinho(produto))

@app.route('/')
def index():
    return render_template('index.html', carrinho=carrinho, produtos=produtos)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    # Implemente a lógica para adicionar itens ao carrinho
    pass

@app.route('/finalizar_compra')
def finalizar_compra():
    # Implemente a lógica para finalizar a compra
    pass

if __name__ == "__main__":
    app.run(debug=True)
