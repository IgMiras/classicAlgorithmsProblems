# Igor Mendes Domingues Miras e Gustavo Santos Gonçalves
import functions as fun


frase = input('Digite uma frase: ')

frequencia = {}
for c in frase:
    if c in frequencia:
        frequencia[c] += 1
    else:
        frequencia[c] = 1

frequencia = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)

nos = frequencia

while len(nos) > 1:
    (key1, c1) = nos[-1]
    (key2, c2) = nos[-2]
    nos = nos[:-2]
    no = fun.arvore(key1, key2)
    nos.append((no, c1 + c2))

    nos = sorted(nos, key=lambda x: x[1], reverse=True)

huffmanCode = fun.arvore_codigo_huffman(nos[0][0])

print(' Caractere | Codigo de Huffman ')
print('----------------------')
for (caractere, freq) in frequencia:
    print(' %-4r |%12s' % (caractere, huffmanCode[caractere]))
    
input('\n\nAperte ENTER para sair')