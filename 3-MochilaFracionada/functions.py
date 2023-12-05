
class Item:
    def __init__(self, numero, peso, valor):
        self.numero = numero
        self.peso = peso
        self.valor = valor

def comparar_itens(item):
    return item.valor / item.peso

def mochila_fracionaria(itens, capacidade):
    itens.sort(key=comparar_itens, reverse=True)

    quantidades = [0.0] * len(itens)
    valor_total = 0.0

    for i, item in enumerate(itens):
        if item.peso <= capacidade:
            quantidades[i] = 1.0
            capacidade -= item.peso
            valor_total += item.valor
        else:
            quantidades[i] = capacidade / item.peso
            valor_total += quantidades[i] * item.valor
            break

    print("\nItens selecionados:")
    for i, item in enumerate(itens):
        print(f"Item {item.numero} - Porcentagem: {quantidades[i] * 100:.2f}%")

    print(f"\nValor total acumulado na mochila: {valor_total:.2f}")
