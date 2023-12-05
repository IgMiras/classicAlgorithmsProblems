
class Item:
    def __init__(self, numero, peso, valor):
        self.numero = numero
        self.peso = peso
        self.valor = valor

def mochila_booleana(itens, capacidade):
    n = len(itens)
    valor_maximo = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if itens[i - 1].peso <= w:
                valor_maximo[i][w] = max(itens[i - 1].valor + valor_maximo[i - 1][w - itens[i - 1].peso],
                                         valor_maximo[i - 1][w])
            else:
                valor_maximo[i][w] = valor_maximo[i - 1][w]

    capacidade_atual = capacidade
    itens_selecionados = [0] * n
    valor_total = valor_maximo[n][capacidade]

    for i in range(n, 0, -1):
        if valor_total != valor_maximo[i - 1][capacidade_atual]:
            itens_selecionados[i - 1] = 1
            valor_total -= itens[i - 1].valor
            capacidade_atual -= itens[i - 1].peso

    print("\nItens selecionados:")
    for i, item in enumerate(itens):
        if itens_selecionados[i]:
            print(f"Item {item.numero}")

    print(f"\nValor total acumulado na mochila: {valor_maximo[n][capacidade]}")
