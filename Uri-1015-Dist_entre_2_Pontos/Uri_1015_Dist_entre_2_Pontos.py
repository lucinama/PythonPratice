import math
def dist2P(ponto1,ponto2):
    num = pow((ponto2[0]-ponto1[0]),2) + pow((ponto2[1]-ponto1[1]),2)
    return math.sqrt(num)

lista = input().split()
p1 = [float(lista[0]),float(lista[1])]
lista = input().split()
p2 = [float(lista[0]),float(lista[1])]
distancia = dist2P(p1,p2)
print("{:.4f}".format(distancia))