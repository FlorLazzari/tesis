# de donde sale este valor para Fandsen: C_T = 0.42	

def frandsen(x_n,r,C_T):
	if r>d_0:
		k_wake = 0.1	
		A_0 = pi * (d_0/2)**2
		A_w = np.zeros(len(x_n)+1)
		n = (1 - C_T)**0.5
		beta = 0.5 * ((1+n)/n)
		A_a = beta * A_0
		alpha = 10 * k_wake		
		d_w = ((beta + alpha * x_n)**0.5) * d_0
		A_w = pi * (d_w/2)**2
		frac = A_0 / A_w
		deficit_dividido_U_inf = 0.5 * (1 - (1 - 2*C_T*frac )**0.5)
	else :
		deficit_dividido_U_inf = 0
	return deficit_dividido_U_inf

# esto está mal, falta pensarlo un poco
