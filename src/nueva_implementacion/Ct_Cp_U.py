from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
# coding=utf-8

from Turbina import Turbina
from scipy import interpolate

U_tabulado = np.array([  3.97553683,   4.9669611 ,   5.95972269,   6.95196727,
7.95116277,   8.93613964,   9.93634081,  10.92857237,
11.9171516 ,  12.9245659 ,  13.91116425,  14.90904084,
15.9053444 ,  16.88414983,  17.88072698,  18.87876044,
19.87055544,  20.84568607,  21.87016143,  22.8544895 ,
23.847984  ,  24.83090363])

c_T_tabulado = np.array([0.824, 0.791, 0.791, 0.791, 0.732, 0.606, 0.510, 0.433, 0.319, 0.247, 0.196, 0.159, 0.134, 0.115, 0.100, 0.086, 0.074, 0.064, 0.057, 0.050, 0.045, 0.040])
# tck = interpolate.splrep(U_tabulado, c_T_tabulado, s=0)
# c_Tnew = interpolate.splev(U, tck, der=0)

c_P_tabulado = np.array([0.3528756612, 0.4188313302, 0.4407975431, 0.4504238495, 0.4410945765, 0.4037893836, 0.3605747665, 0.3129388419, 0.2567853612, 0.2057066378, 0.1659160941, 0.1358084161, 0.1124665859, 0.093973068, 0.0792089026, 0.0673489313, 0.05774329, 0.049880825, 0.0433833884, 0.0379671505, 0.0334162558, 0.0295645645])
# tck = interpolate.splrep(U_tabulado, c_P_tabulado, s=0)
# c_Pnew = interpolate.splev(U, tck, der=0)

plt.figure(figsize=(10,10))
plt.plot(U_tabulado, c_T_tabulado, 'ob--',label=r'$C_T$', markersize= 10)
plt.plot(U_tabulado, c_P_tabulado, 'or--',label=r'$C_P$', markersize= 10)
plt.legend(fontsize=20, loc= 'upper right')
plt.grid()
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel(r'$u_{hub}$[m/s]', fontsize=25)
plt.ylabel(r'coeficientes', fontsize=25)
plt.savefig('Ct_Cp_U.pdf')
plt.show()
