class U(object):
    def __init__(self):
        self.coord = None

estas dos cosas estan muy a lo bestia, ni siquiera estan probadas, hay que terminar esto:

    def merge_estela(self, estela, cantidad_adentro_disco, cantidad_turbinas_izquierda_de_selec):
        estela_en_coord_rand_mergeada = np.zeros(cantidad_adentro_disco)
        for i in range(cantidad_adentro_disco):
            for j in range(cantidad_turbinas_izquierda_de_selec):
                estela_en_coord_rand_mergeada[i] += estela[i+cantidad_adentro_disco*j]
        return estela_en_coord_rand_mergeada


    def restar_deficit():
        u_coord = u_coord * (1 - deficit_normalizado_en_coord)

# prueba:
# turbina = Turbina(0,0)
# estela = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
# cant_adentro = 7
# cant_turbinas = 2
# estela_mergeada = turbina.merge_estela(estela, cant_adentro, cant_turbinas)
# print estela_mergeada
