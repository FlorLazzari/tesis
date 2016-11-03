#figura 4 del paper:

# sigma_n en fc de x_n:

len(sigma_n)
len(x_n)


fig = plt.figure(3)
#plt.ylim([0,1])	
plt.xlabel(r'$ x / d_{0} $')
plt.ylabel(r'$\sigma / d_{0} $')
plt.plot(x_n,sigma_n, 'x')
plt.show()
fig.savefig('figura_4_gaussiana.png')


