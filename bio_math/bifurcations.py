
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x, x_dot = [], []
line, = plt.plot([], [], 'r-')
ax.grid()

def init_animation():
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 1.5)
    return line,

def update(r):
    x = np.arange(-2.5,2.5,0.1)
    x_dot = domain ** 2 - r
    line.set_data(x, x_dot)
    return line,

def update_hw(r):
    x = np.arange(-10,10,0.1)
    x_dot = r*x + x**3 - x**5
    line.set_data(x, x_dot)
    ax.set_title("r = {}".format(round(r,3)))
    return line,


def F_SOE():
    t = np.arange(-0.75,1.5,0.05)
    x_f_t = np.exp(2*t) + np.exp(-3*t)
    y_f_t = np.exp(2*t) -4 * np.exp(-3*t)
    return x_f_t, y_f_t

if __name__ == "__main__":
    d_to_do = {1: "animation", 2: "First SOE"}
    to_do = 2

    if to_do == 1:

        ani = FuncAnimation(fig, update_hw, frames = np.arange(-1,1,0.05),
                            init_func = init_animation, blit = False)
        # http://louistiao.me/posts/notebooks/save-matplotlib-animations-as-gifs/
        ani.save('animation.gif', writer='imagemagick', fps=5)
        #plt.show()

    elif to_do == 2:
        x_f_t, y_f_t = F_SOE()
        # print(y_f_t)
        plt.plot(x_f_t, y_f_t, "bo")
        plt.show()
