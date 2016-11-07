# figura 3 del paper:

# estaría bueno que no solo quedara restringida al script de la gaussiana, sino que pueda hacer este gráfico para cualquier modelo

for i in range(0,len(x_n)):
	y[i] = gaussiana[x_n[i],fin]
	

fig = plt.figure(1)
plt.ylim([0,1])	
plt.xlim([0,1])	
plt.xlabel('r')
plt.ylabel(r'$\Delta U / \Delta U_{max} $')
plt.plot(r,y[0])
plt.plot(r,y[1])
plt.plot(r,y[2])
plt.plot(r,y[3])
plt.plot(r,y[4])
plt.plot(r,y[5])
plt.plot(r,y[6])
plt.plot(r,y[7])
plt.plot(r,y[8])
plt.plot(r,y[9])
plt.show()
fig.savefig('figura_3_gaussiana.png')


# faltaría ponerle leyenda para que se entienda la variación en x

