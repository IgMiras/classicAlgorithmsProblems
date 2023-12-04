# Codigo de Huffman
# Igor Mendes Domingues Miras e Gustavo Santos Gonçalves

frase = input('Digite uma frase: ')

class arvore(object):

    def __init__(self, esquerda=None, direita=None):
        self.esquerda = esquerda
        self.direita = direita

    def filho(self):
        return (self.esquerda, self.direita)

    def nos(self):
        return (self.esquerda, self.direita)

    def __str__(self):
        return '%s_%s' % (self.esquerda, self.direita)


def arvore_codigo_huffman(no, esquerda=True, stringBinaria=''):
    if type(no) is str:
        return {no: stringBinaria}
    (esq, dir) = no.filho()
    dicionario = dict()
    dicionario.update(arvore_codigo_huffman(esq, True, stringBinaria + '0'))
    dicionario.update(arvore_codigo_huffman(dir, False, stringBinaria + '1'))
    return dicionario


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
    no = arvore(key1, key2)
    nos.append((no, c1 + c2))

    nos = sorted(nos, key=lambda x: x[1], reverse=True)

huffmanCode = arvore_codigo_huffman(nos[0][0])

print(' Caractere | Codigo de Huffman ')
print('----------------------')
for (caractere, freq) in frequencia:
    print(' %-4r |%12s' % (caractere, huffmanCode[caractere]))
    
input('\n\nAperte ENTER para sair')