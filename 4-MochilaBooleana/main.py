# Igor Mendes Domingues Miras e Gustavo Santos Gonçalves
import functions as fun


n = int(input("Digite a quantidade de itens: "))
itens = []

for i in range(n):
    print(f"\nItem {i + 1}:")
    numero = i + 1
    peso = int(input("Peso: "))
    valor = int(input("Valor: "))
    itens.append(fun.Item(numero, peso, valor))

capacidade = int(input("\nDigite a capacidade da mochila: "))
fun.mochila_booleana(itens, capacidade)

input('\n\nAperte ENTER para sair')