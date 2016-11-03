# filled contour plot

X,R = np.meshgrid(x_n,r)

a = deficit_dividido_U_inf.transpose()

fig = plt.figure()  
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel('r')
plt.title('Gaussian Filled Contour Plot')      
cp = plt.contourf(x_n,r,a)
plt.colorbar(cp)
plt.show()
plt.figure()
fig.savefig('figura_6_gaussiana.png')


# faltaría hacerlo en función de z_n. ¿Cómo?

# pero esto no es exactamente lo que aparece en la figura 6, esto es el deficit, yo quiero tener el viento. Veamos cómo se define el deficit y en fc. de eso otenemos el viento

