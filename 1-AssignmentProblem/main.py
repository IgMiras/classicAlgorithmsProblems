# Igor Mendes Domingues Miras e Gustavo Santos Gonçalves
import functions as fun


N = int(input("Digite o numero de pessoas/tarefas (N): "))

matriz_custo = [[0] * N for _ in range(N)]

print("Digite os custos das tarefas para cada pessoa:")

for i in range(N):
    for j in range(N):
        matriz_custo[i][j] = int(
            input(f"Custo para a Pessoa {i + 1} na Tarefa {j + 1}: ")
        )

fun.solucao(matriz_custo, N)

input("\n\nAperte ENTER para sair")
