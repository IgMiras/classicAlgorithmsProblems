
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

