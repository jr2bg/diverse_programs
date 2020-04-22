import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp
# https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html

# funciones de las mallas del Bourden
def fun(t,I):
    dI1dt = -4*I[0] + 3*I[1] +6
    dI2dt = -2.4 * I[0] +1.6*I[1] +3.6
    return [dI1dt, dI2dt]

def fI1(t):
    return -3.375 * np.exp(-2*t) +1.875 * np.exp(-0.4*t) + 1.5

def fI2(t):
    return -2.25 * np.exp(-2*t) + 2.25 * np.exp(-0.4 * t)

y_0 = [0,0]
t_span = [0,0.5]
t_eval = [0,0.1,0.2,0.3,0.4,0.5]

arr_an_sol = np.array([fI1(np.array(t_eval)),fI2(np.array(t_eval))])

sol = solve_ivp(fun, t_span, y_0, t_eval = t_eval)
# print(sol.t)
# print(sol.y)

print(np.absolute(arr_an_sol - sol.y))
# print(sol.sol)
