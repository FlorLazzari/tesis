# voy a comparar los epsilon:
# de la figura 4
# de la ecuacion 19
# de la ecuacion 21

# C_T (case 1) = 0.42
# C_T (case 2 al 5) = 0.8

C_T = [0.42, 0.8]
beta = [0, 0]
epsilon_19 = [0, 0]
epsilon_21 = [0, 0]


for i in range(0,2):
    beta[i] = 0.5 * ((1 + (1 - C_T[i])**0.5)/(1 - C_T[i])**0.5)
    epsilon_19[i] = 0.25 * (beta[i])**0.5
    epsilon_21[i] = 0.2 * (beta[i])**0.5

# comparo con epsilon de la figura 4:
# obtengo epsilon de la ordenada al origen del grafico
epsilon_figura_case_1 = 0.219
epsilon_figura_case_2 = 0.238
epsilon_figura_case_3 = 0.253
epsilon_figura_case_4 = 0.272
epsilon_figura_case_5 = 0.257

print "CASE 1: \n equ 19 = %f \n equ 21 = %f \n figura = %f" % (epsilon_19[0], epsilon_21[1], epsilon_figura_case_1)
print "CASE 2: \n equ 19 = %f \n equ 21 = %f \n figura = %f" % (epsilon_19[1], epsilon_21[1], epsilon_figura_case_2)
print "CASE 3: \n equ 19 = %f \n equ 21 = %f \n figura = %f" % (epsilon_19[1], epsilon_21[1], epsilon_figura_case_3)
print "CASE 4: \n equ 19 = %f \n equ 21 = %f \n figura = %f" % (epsilon_19[1], epsilon_21[1], epsilon_figura_case_4)
print "CASE 5: \n equ 19 = %f \n equ 21 = %f \n figura = %f" % (epsilon_19[1], epsilon_21[1], epsilon_figura_case_5)


#
# print "epsilon_19 (case 2) =", epsilon_19[1], "epsilon__figura (case 1) =", epsilon_figura_case_1
# print "epsilon_21 (case 1) =", epsilon_21[0], "epsilon__figura (case 1) =", epsilon_figura_case_1
# print "epsilon_21 (case 2) =", epsilon_21[1], "epsilon__figura (case 1) =", epsilon_figura_case_1
#
