def consumo(distancia, combustivel):
    return distancia/combustivel

x = int(input())
y = float(input())
cons = consumo(x,y);
print("{:.3f} km/l".format(cons))