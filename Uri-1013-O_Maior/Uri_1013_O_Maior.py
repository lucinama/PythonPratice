def MaiorAB(x,y):
    return int((x + y + abs(x-y))/2)

lista = input().split()
maior1 = MaiorAB(int(lista[0]),int(lista[1]))
maior = MaiorAB(maior1,int(lista[2]))
print("{} eh o maior".format(maior))