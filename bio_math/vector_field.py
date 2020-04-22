import matplotlib.pyplot as plt
import numpy as np

# https://x-engineer.org/undergraduate-engineering/advanced-mathematics/differential-equations/drawing-vector-field-plots-easy/

a = 0.1
k = 100
c = 0.01
delta_t = 0.01
x_int = [1,2]
t_steps = 15

#t_0 = np.array([x*0.1 for x in range(20)])
t_0 = np.array([[y/10  for x in range(0,31)] for y in range(t_steps)])
t_1 = t_0 + delta_t
X_0 = np.array([[x * 5 for x in range(-10,21)] for y in range(t_steps) ])

# slope: diff equation
m = a * X_0 * (1- X_0 / k) - c * X_0
#m = X_0 * (1-X_0) * (2-X_0)
X_1 = m *(t_1 - t_0)

# print(t_1-t_0)
# print(t_1)
# print(X_0)
# print(X_1)
print(m)
plt.quiver(t_0 , X_0, delta_t, X_1)
plt.show()
