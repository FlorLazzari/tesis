# la clase padre puede tener distintos atributos que la clase hijo
# en este caso, modelo no tiene las ctes

class Modelo(object):

    def __init__(self, case):
        self.case = case

    def evalDeficitNorm(self, coord):
        pass

    def play_pol_2d(self, coordenadas, c_T):
        pass

    def play_pol(self, coordenadas, c_T):
        pass

    def play_cart(self, coordenadas, c_T):
        pass
