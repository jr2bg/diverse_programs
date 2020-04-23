import matplotlib.pyplot as plt

# paso
h = 0.1

# número de pasos
N = 1000

# número máximo de argumentos para las funciones, y funciones
m = 2

# inicialización del diccionario de argumentos
keys_arg = ["w_{}".format(i) for i in range(1, m + 1)]

# parámetros de Lotka-Volterra
alpha = 1.1
beta = 0.4
gamma = 0.1
delta = 0.4

# funciones de Lotka-Volterra
def f_1(t_j, **kwargs):
    return alpha * kwargs["w_1"] - beta * kwargs["w_1"] * kwargs["w_2"]

def f_2(t_j, **kwargs):
    return delta * kwargs["w_1"] * kwargs["w_2"] - delta * kwargs["w_2"]

# tupla de funciones
t_functions = (f_1, f_2) #f_3,...., f_m

# condiciones iniciales
w_0 = [10.,10.]


def iteration_RK(t_functions, N, h, w_0, keys_arg):
    # array de tiempo
    t = [i * h for i in range(N)]
    # diccionario con los argumentos
    d_arg = {}
    # array con los valores de w_j
    w = [w_0]

    for j in range(N-1):
        k_1 = []
        k_2 = []
        k_3 = []
        k_4 = []

        # k_1
        l = 0
        for k in keys_arg:
            d_arg[k] = w[j][l]
            l += 1
        for i in range(m):
            k_1.append(h * t_functions[i](t[j], **d_arg))

        # k_2
        l = 0
        for k in keys_arg:
            d_arg[k] = w[j][l] + k_1[l] / 2
            l += 1
        for i in range(m):
            k_2.append(h*t_functions[i](t[j] + h/2, **d_arg))

        # k_3
        l = 0
        for k in keys_arg:
            d_arg[k] = w[j][l] +k_2[l] / 2
            l += 1
        for i in range(m):
            k_3.append(h*t_functions[i](t[j] + h/2, **d_arg))

        # k_4
        l = 0
        for k in keys_arg:
            d_arg[k] = w[j][l] +k_3[l]
            l += 1
        for i in range(m):
            k_4.append(h*t_functions[i](t[j] + h, **d_arg))


        w_i = []
        for i in range(m):
            w_i.append(w[j][i] + (k_1[i] + 2 * k_2[i] + 2 * k_3[i] + k_4[i]) / 6)

        w.append(w_i)

    return t, w



t,w = iteration_RK(t_functions, N, h, w_0, keys_arg)
plt.plot(t,[z[0] for z in w])
plt.plot(t,[z[1] for z in w])
plt.show()
