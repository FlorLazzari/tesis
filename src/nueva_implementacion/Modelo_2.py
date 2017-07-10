class Modelo(object):

    def __init__(self):
        pass
    def evalDeficitNorm(self, coord, c_T):
        pass

    # def play_cart(self, coordenadas, c_T):
    #     if isinstance(coordenadas, Coordenadas):
    #         self.x = coordenadas.x
    #         self.y = coordenadas.y
    #         self.z = coordenadas.z
    #         coordenadas.normalizar_hub(self.case)
    #         self.x_n = coordenadas.x_n
    #         self.y_n = coordenadas.y_n
    #         self.z_n = coordenadas.z_n
    #     elif isinstance(coordenadas, Coordenadas_Norm):
    #         self.x_n = coordenadas.x_n
    #         self.y_n = coordenadas.y_n
    #         self.z_n = coordenadas.z_n
    #         coordenadas.desnormalizar_hub(self.case)
    #         self.x = coordenadas.x
    #         self.y = coordenadas.y
    #         self.z = coordenadas.z
    #     self.c_T = c_T
    #     self.deficit_dividido_U_inf = np.zeros((len(self.x_n),len(self.y_n),len(self.z_n)))
    #     for i in range (0,len(self.x_n)):
    #         for j in range (0,len(self.y_n)):
    #             for k in range (0,len(self.z_n)):
    #                 self.deficit_dividido_U_inf[i,j,k] = self.evalDeficitNormevalDeficitNorm((self.x_n[i], self.y_n[j], self.z_n[k]))












    # def play_lcart(self, coordenadas, c_T):
    #     # coordenadas es una lista de tuplas de 3 componentes
    #
    #     self.c_T = c_T
    #
    #     self.deficit_dividido_U_inf = list()
    #     for coord in coordenadas:
    #         self.deficit_dividido_U_inf.append() = self.evalDeficitNormevalDeficitNorm((coord[0], coord[1], coord[2]))





    # def play_pol_2d(self, coordenadas, c_T):
    #     if isinstance(coordenadas, Coordenadas):
    #         self.x = coordenadas.x
    #         self.y = coordenadas.y
    #         self.z = coordenadas.z
    #         coordenadas.normalizar(self.case)
    #         self.x_n = coordenadas.x_n
    #         self.y_n = coordenadas.y_n
    #         self.z_n = coordenadas.z_n
    #     elif isinstance(coordenadas, Coordenadas_Norm):
    #         self.x_n = coordenadas.x_n
    #         self.y_n = coordenadas.y_n
    #         self.z_n = coordenadas.z_n
    #         coordenadas.desnormalizar(self.case)
    #         self.x = coordenadas.x
    #         self.y = coordenadas.y
    #         self.z = coordenadas.z
    #     self.c_T = c_T
    #     self.r, self.phi = cart2pol(self.y_n, self.z_n)
    #     sigma_n = self.k_estrella * self.x_n + self.epsilon
    #     sigma_n_cuadrado = (sigma_n)**2
    #     r_cuadrado = self.r**2
    #     c = 1 - (1-(self.c_T/(8*sigma_n_cuadrado)))**(0.5)
    #     exponente = np.zeros((len(self.x_n),len(self.r)))
    #     self.gauss = np.zeros((len(self.x_n),len(self.r)))
    #     self.deficit_dividido_U_inf = np.zeros((len(self.x_n),len(self.r)))
    #     for i in range (0,len(self.x_n)):
    #         for j in range (0,len(self.r)):
    #             exponente[i,j] = -r_cuadrado[j] / (2 * sigma_n_cuadrado[i])
    #             self.gauss[i,j] = exp(exponente[i,j])
    #             self.deficit_dividido_U_inf[i,j] = c[i] * self.gauss[i,j]
    #
    # def play_pol(self, coordenadas, c_T):
    #     if isinstance(coordenadas, Coordenadas):
    #         self.x = coordenadas.x
    #         self.y = coordenadas.y
    #         self.z = coordenadas.z
    #         coordenadas.normalizar(self.case)
    #         self.x_n = coordenadas.x_n
    #         self.y_n = coordenadas.y_n
    #         self.z_n = coordenadas.z_n
    #     elif isinstance(coordenadas, Coordenadas_Norm):
    #         self.x_n = coordenadas.x_n
    #         self.y_n = coordenadas.y_n
    #         self.z_n = coordenadas.z_n
    #         coordenadas.desnormalizar(self.case)
    #         self.x = coordenadas.x
    #         self.y = coordenadas.y
    #         self.z = coordenadas.z
    #     self.c_T = c_T
    #     self.sigma_n = self.k_estrella * self.x_n + self.epsilon
    #     sigma_n_cuadrado = (self.sigma_n)**2
    #     #r_cuadrado = self.y_n**2 + self.z_n**2
    #     c = 1 - (1-(self.c_T/(8*sigma_n_cuadrado)))**(0.5)
    #     r_cuadrado = np.zeros((len(self.y_n),len(self.z_n)))
    #     exponente = np.zeros((len(self.x_n),len(self.y_n),len(self.z_n)))
    #     self.gauss = np.zeros((len(self.x_n),len(self.y_n),len(self.z_n)))
    #     self.deficit_dividido_U_inf = np.zeros((len(self.x_n),len(self.y_n),len(self.z_n)))
    #     for i in range (0,len(self.x_n)):
    #         for j in range (0,len(self.y_n)):
    #             for k in range (0,len(self.z_n)):
    #                 r_cuadrado[j,k] = (self.y_n[j])**2 + (self.z_n[k])**2
    #                 exponente[i,j,k] = -r_cuadrado[j,k] / (2 * sigma_n_cuadrado[i])
    #                 self.gauss[i,j,k] = exp(exponente[i,j,k])
    #                 self.deficit_dividido_U_inf[i,j,k] = c[i] * self.gauss[i,j,k]
