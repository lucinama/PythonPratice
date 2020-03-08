class Produto:
    def __init__(self, codigo, unidades, preco):
        self._self = self
        self.codigo = codigo
        self.unidades = unidades
        self.preco = preco

lista1 = input().split()
prod1 = Produto(int(lista1[0]), int(lista1[1]), float(lista1[2]))
lista2 = input().split()
prod2 = Produto(int(lista2[0]), int(lista2[1]), float(lista2[2]))
valor = prod1.preco*prod1.unidades + prod2.preco*prod2.unidades
print("VALOR A PAGAR: R$ {:.2f}".format(valor))