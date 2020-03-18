# 4th order Runge Kutta Method

f_k1 = lambda h, f, y_n, t_n : h * f(y_n,t_n)
f_k2 = lambda h, f, y_n, t_n, k1: h * f(y_n + k1/2, t_n + h/2)
f_k3 = lambda h, f, y_n, t_n, k2: h * f(y_n + k2/2, t_n + h/2)
f_k4 = lambda h, f, y_n, t_n, k3: h * f(y_n + k3, t_n + h)

f_yn1 = lambda y_n, k1, k2, k3, k4: y_n + (k1 + 2*k2 + 2*k3 + k4) / 6

# system ODE
# kn -> k_{n}
# k_n -> k_{-n}
S_ode = lambda k_1, c, k1, e, s : k_1*c - k1*e*s
C_ode = lambda k1, e, sk_1, c, k2: k1*e*s - k_1*c - k2*c
P_ode = lambda k2, c: k2*c
E_ode = lambda k1, e, s, k_1, c, k2 : -k1*e*s + k_1*c + k2*c

sys_ODE_MMk = { 0: S_ode,
                1: C_ode,
                2: P_ode,
                3: E_ode}


def main():
    # valores iniciales
    # l_s = [10]
    # l_e = [2]
    # l_c = [0]
    # l_p = [0]
    # l_t = [0]
    l_values = [[10],[2],[0],[0], [0]]

    # paso
    h = 0.1


    # iteración
    for i in range(1000):
        for j in range(4):

            f = sys_ODE_MMk[0]
            y_n = l_values[j][-1]
            t_n = l_values[-1][-1]

            k1 = f_k1(h, f, y_n, t_n)
            k2 = f_k2(h, f, y_n, t_n, k1)
            k3 = f_k3(h, f, y_n, t_n, k2)
            k4 = f_k4(h, f, y_n, t_n, k3)

            y_n1  = f_yn1(y_n, k1, k2, k3, k4 )

            l_values.append(y_n1)
