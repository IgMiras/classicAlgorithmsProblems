def imprimir(matriz, lin, col):
    for i in range(lin):
        for j in range(col):
            print(f"{matriz[i][j]}\t", end="")
        print()

def solucao(matriz_custo, N):
    tarefa = [-1] * N
    custo_total = 0

    # Atribuição de tarefas usando Branch and Bound
    for i in range(N):
        custo_minimo = float('inf')
        pessoa = -1

        for j in range(N):
            if tarefa[j] == -1 and matriz_custo[i][j] < custo_minimo:
                custo_minimo = matriz_custo[i][j]
                pessoa = j

        tarefa[pessoa] = i
        custo_total += custo_minimo

    print("\nAlocação de Tarefas:")
    for i in range(N):
        print(f"Tarefa {tarefa[i] + 1} -> Pessoa {i + 1}")

    print("\nCusto Total:", custo_total)

def main():
    N = int(input("Digite o numero de pessoas/tarefas (N): "))

    matriz_custo = [[0] * N for _ in range(N)]

    print("Digite os custos das tarefas para cada pessoa:")
    for i in range(N):
        for j in range(N):
            matriz_custo[i][j] = int(input(f"Custo para a Pessoa {i + 1} na Tarefa {j + 1}: "))

    solucao(matriz_custo, N)

if __name__ == "__main__":
    main()
