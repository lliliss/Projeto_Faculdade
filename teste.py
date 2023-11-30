import os

def ler_arquivo_txt(nome_arquivo):
    dicionario = {}
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                chave, valor = linha.strip().split('::')
                dicionario[chave.strip()] = valor.strip()
    return dicionario

def adicionar_elemento(dicionario, chave, valor):
    dicionario[chave] = valor

def salvar_no_arquivo_txt(nome_arquivo, dicionario):
    with open(nome_arquivo, 'w') as arquivo:
        for chave, valor in sorted(dicionario.items()):
            arquivo.write(f"{chave}: {valor}\n")

# Nome do arquivo
nome_do_arquivo = "data\/camisas.txt"

print("abrindo arquivo...")

# Lê o conteúdo do arquivo para um dicionário
meu_dicionario = ler_arquivo_txt(nome_do_arquivo)
print("arquivo aberto!")
print(meu_dicionario)

# Adiciona um novo elemento ao dicionário
a = input("pressione enter para adicionar um novo valor ao dicionario!")
adicionar_elemento(meu_dicionario, "NovaChave", "NovoValor")
a = input("Valor adicionado! Pressione enter para encerrar o código e verificar o arquivo")

# Salva o dicionário de volta no arquivo
salvar_no_arquivo_txt(nome_do_arquivo, meu_dicionario)
