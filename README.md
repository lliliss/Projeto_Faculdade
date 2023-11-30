# A LOLja Nerd

## Integrantes
- Alice Ferreira
- Irving Samuel
- Isabel Melo
- Thayná Carnaúba
- Vlamir Gama

## Descrição do Projeto

A LOLja Nerd é uma loja online especializada na venda de produtos nerds, como camisas, canecas e quadrinhos. Para gerenciar o estoque e as transações, foi desenvolvido um programa em Python que utiliza classes para representar os diferentes tipos de produtos disponíveis.

### Estrutura do Projeto

O programa possui uma classe genérica para representar produtos, com três subclasses específicas:
1. Camisas: Além dos atributos comuns (nome e preço), as camisas possuem a característica de tamanho (P, M, G).
2. Canecas: Além dos atributos comuns, as canecas possuem o campo de capacidade, medido em litros.
3. Quadrinhos: Além dos atributos comuns, os quadrinhos têm informações relativas a autor e editora.

O usuário interage com o programa através de comandos de input para adicionar ou remover produtos da lista e finalizar a compra. O programa realiza tratamento de exceções para lidar com entradas inesperadas.

### Promoções Especiais

O gerente implementou duas promoções especiais:
- A cada 4 camisas compradas, o cliente ganha uma caneca de brinde.
- A cada 5 quadrinhos comprados, o quadrinho de menor valor sai de graça.

Ao imprimir a nota fiscal, o programa informa quais produtos do carrinho do cliente entraram na promoção.

### Números de Série

Cada produto comprado gera um número de série aleatório, seguindo as seguintes regras:
- Camisas: Múltiplos de 5
- Canecas: Múltiplos de 3
- Quadrinhos: Múltiplos de 7

Cada produto, mesmo aqueles que fazem parte da promoção, possui seu próprio número de série.

## Implementação

O backend do projeto foi desenvolvido em Python, utilizando Flask como framework web. O frontend foi construído com Jinja2. A seguir, algumas imagens do projeto em produção:

![Imagem 1]
Legenda da imagem 1

![Imagem 2]
Legenda da imagem 2
