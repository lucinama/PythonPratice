from math import pi
class Retangulo:

    def __init__(self, ladox, ladoy):
        self.ladox = ladox
        self.ladoy = ladoy

    def areaRet(self):
        return self.ladox * self.ladoy

    def perimRet(self):
        return 2*(self.ladox + self.ladoy)


class Circulo:

    def __init__(self, raio):
        self._self = self
        self.raio = raio

    def areaCirc(self):
        return (self.raio**2) * pi

    def perimCirc(self):
        return self.raio * pi * 2