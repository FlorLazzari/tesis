k_wake = 0.1						# proposed by Jensen
#k_wake_on_shore = 0.075			#suggested in the literature
#k_wake_off_shore = 0.04 and 0.05	#suggested in the literature


def Jensen():
	n = (1 - C_T)**0.5
	a = 1 - n
	denom = (1 + 2*k_wake*x_n)**2
	deficit_dividido_U_inf = a / denom
	return deficit_dividido_U_inf
