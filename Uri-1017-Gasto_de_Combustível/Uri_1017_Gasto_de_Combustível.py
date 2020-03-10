def consumo(t, v):
    d = t*v
    l = d/12
    return l

tempo = int(input())
velocidade = int(input())
litros = consumo(tempo, velocidade)
print("{:.3f}".format(litros))
