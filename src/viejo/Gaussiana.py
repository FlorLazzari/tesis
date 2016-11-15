#from Modelo import Modelo


# super() lets you avoid referring to the base class explicitly, which can be nice.
# But the main advantage comes with multiple inheritance, where all sorts of fun
# stuff can happen.


class Gaussiana(object):

    def __init__(self,coordenadas,c_T,case,k_estrella,epsilon):
        super(Gaussiana, self).__init__(self.coordenadas,self.c_T,self.case)
        # self.coordenadas = coordenadas
        # self.c_T = c_T
        self.case = case
        self.k_estrella = k_estrella
        self.epsilon = epsilon

    def play(self):
        self.coordenadas.normalizar(self.case)
        x_n = self.coordenadas.x_n
        y_n = self.coordenadas.y_n
        z_n = self.coordenadas.z_n
        self.coordenadas.cart2pol()
        r = self.coordenadas.r
        phi = self.coordenadas.phi
        sigma_n = self.k_estrella * x_n + self.epsilon
        print(sigma_n)


		# sigma_n_cuadrado = (sigma_n)**2
		# r_cuadrado = r**2
		# c = 1 - (1-(c_T/(8*sigma_n_cuadrado)))**(1/2)
		#
		# exponente = np.zeros((len(x_n),len(r_cuadrado)))
		# gaussiana = np.zeros((len(x_n),len(r_cuadrado)))
		# deficit_dividido_U_inf = np.zeros((len(x_n),len(r_cuadrado)))
		#
		# for i in range (0,len(x_n)):
		# 	for j in range (0,len(r_cuadrado)):
		# 		exponente[i,j] = -r_cuadrado[j] / (2 * sigma_n_cuadrado[i])
		# 		gaussiana[i,j] = exp(exponente[i,j])
		# 		deficit_dividido_U_inf[i,j] = c[i] * gaussiana[i,j]
