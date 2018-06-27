from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
# coding=utf-8


from Turbina import Turbina
from scipy import interpolate

class Turbina_BlindTest_2_TSR4(Turbina):

    def __init__(self, coord):
        d_0 = 0.894
        super(Turbina_BlindTest_2_TSR4, self).__init__(d_0, coord)

    def c_T_tabulado(self, U):

        U_tabulado = np.array([3.56135115899, 3.56547783208 , 3.66054806312 , 3.69998206373 , 4.00854765204 , 4.09521993031 , 4.4241382668 , 4.55770878947 , 4.98071967506 , 5.08498044583 , 5.32944909023 , 5.42535198145 , 5.69228752348 , 5.80755443632 , 6.13763130303 , 6.23859775363 , 6.60572156018 , 6.77061317059 , 6.77543074148 , 7.23796532963 , 7.33258499463 , 8.06752026333 , 8.15174412018 , 8.88833511837 , 8.8956552691 , 8.93562677517 , 9.90256792528 , 10.0925054085 , 13.0052054885 , 13.6327952832 , 18.6553937623 , 25.4092060249 , 26.1534663976 , 26.1969867627 , 26.2179894845 , 26.3258260425 , 43.5172340061 , 43.7376865951])
        c_T_tabulado = np.array([1.1165769166, 1.10234113227, 1.104641417, 1.09209267192, 1.07543862479, 1.06868057083, 1.06862544338, 1.04330601836, 1.02273510393, 1.00467465793, 0.990941599229, 0.973980338424, 0.958124139533, 0.941486356226, 0.919590797054, 0.905870026831, 0.882708383358, 0.861592864254, 0.863359370066, 0.824484594668, 0.815656436082, 0.771978992581, 0.764469311128, 0.741513143654, 0.737218903195, 0.737422358271, 0.668222782961, 0.651538568644, 0.397861884221, 0.381706732783, 0.300882883854, 0.239947674624, 0.237579050069, 0.232946082889, 0.236635820069, 0.235402739615, 0.181321292469, 0.181321292469])
        tck = interpolate.splrep(U_tabulado, c_T_tabulado, s=0)
        c_Tnew = interpolate.splev(U, tck, der=0)
        return c_Tnew

    def P_tabulado(self, U):
        Pnew = 0 ###??????
        return Pnew

    def c_P_tabulado(self, U):
        c_Pnew = 0 ###??????
        return c_Pnew
