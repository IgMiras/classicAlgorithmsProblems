def max(a, b):
    return a if a > b else b

def subsequencia_comum_maxima(sequencia1, sequencia2):
    tamanho1 = len(sequencia1)
    tamanho2 = len(sequencia2)

    matriz = [[0] * (tamanho2 + 1) for _ in range(tamanho1 + 1)]

    for i in range(tamanho1 + 1):
        for j in range(tamanho2 + 1):
            if i == 0 or j == 0:
                matriz[i][j] = 0
            elif sequencia1[i - 1] == sequencia2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1] + 1
            else:
                matriz[i][j] = max(matriz[i - 1][j], matriz[i][j - 1])

    tamanho_maior_subsequencia = matriz[tamanho1][tamanho2]
    maior_subsequencia = [""] * tamanho_maior_subsequencia
    i, j = tamanho1, tamanho2

    while i > 0 and j > 0:
        if sequencia1[i - 1] == sequencia2[j - 1]:
            maior_subsequencia[tamanho_maior_subsequencia - 1] = sequencia1[i - 1]
            i -= 1
            j -= 1
            tamanho_maior_subsequencia -= 1
        elif matriz[i - 1][j] > matriz[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("\nMaior subsequencia comum:", "".join(maior_subsequencia))
    print("Tamanho da maior subsequencia comum:", matriz[tamanho1][tamanho2])
