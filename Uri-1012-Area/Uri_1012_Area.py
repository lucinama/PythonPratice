class Areas:
    def __init__(self, valor_a, valor_b, valor_c):
        self._self = self
        self.valor_a = valor_a
        self.valor_b = valor_b
        self.valor_c = valor_c
        self.area_TriRet = (a*c/2)
        self.area_Cir = 3.14159*c**2
        self.area_Tra = (a+b)*c/2
        self.area_Qua = b**2
        self.area_Ret = a*b

lista = input().split()
a = float(lista[0])
b = float(lista[1])
c = float(lista[2])
ar = Areas(a,b,c)
print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(ar.area_TriRet, ar.area_Cir, ar.area_Tra, ar.area_Qua, ar.area_Ret))