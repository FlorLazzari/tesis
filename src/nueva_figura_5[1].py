# figura (no está en el paper): deficit_dividido_U_inf en funcion de x para distintos r



fin_2 = np.arange(0,len(x_n))

y_2 = np.zeros((4,len(x_n)))



r_0 = max(r)
r_1 = max(r) / 2
r_2 = max(r) / 3
r_3 = max(r) * 0.75


y_2[0] = deficit_dividido_U_inf[fin_2,r_0]		
y_2[1] = deficit_dividido_U_inf[fin_2,r_1]
y_2[2] = deficit_dividido_U_inf[fin_2,r_2]
y_2[3] = deficit_dividido_U_inf[fin_2,r_3]

# vemos como la relación es casi idéntica para distintos valores de r (esto está bien?)

fig = plt.figure(2)
plt.ylim([0,0.5])	
plt.xlim([0,6])
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\Delta U / U_{\infty} $')
plt.plot(x_n,y_2[0], 'x')
plt.plot(x_n,y_2[1], 'x')
plt.plot(x_n,y_2[2], 'x')
plt.plot(x_n,y_2[3], 'x')
plt.show()
fig.savefig('figura_5_gaussiana.png')


