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
        custo_minimo = float("inf")
        pessoa = -1

        for j in range(N):
            if tarefa[j] == -1 and matriz_custo[i][j] < custo_minimo:
                custo_minimo = matriz_custo[i][j]
                pessoa = j

        tarefa[pessoa] = i
        custo_total += custo_minimo

    print("\nAlocação de Tarefas:")
    for i in range(N):
        print(f"Tarefa {i + 1} -> Pessoa {tarefa[i] + 1}")

    print("\nCusto Total:", custo_total)
