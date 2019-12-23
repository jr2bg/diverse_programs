import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 0 -> nada (blanco)
# 1 -> bosque (verde)
# 2 -> fuego (rojo)
# 3 -> ceniza (negro)
class Universe:
    def __init__(self):
        self.n_rows = 40
        self.n_cols = 60
        self.lattice = np.zeros((self.n_rows, self.n_cols))

    def forest_areas(self, forest_points):
        #self.lattice = [[0 for x in range(n_rows)] for y in range(n_cols)]
        for point in forest_points:
            # zonas verdes
            self.lattice[point[0]][point[1]] = 1

    def fire_areas(self, fire_points):
        for point in fire_points:
            self.lattice[point[0]][point[1]] = 2

    def rules(self):
        for row in range(len(self.lattice)):
            for i in range(len(row)):
                if self.lattice[row][i] == 1:
                    dfdf
                elif el == 2:
                    el = 3

    def plot_forest(self):
        df = pd.DataFrame(self.lattice)
        sns.heatmap(df, cmap= ["white", "green", "red", "black"], vmax = 3,
                    linewidths=.5)#"YlGnBu")
        plt.show()

if __name__ == "__main__":
    forest = Universe()
    forest.forest_areas([(20,55),(10,20),(31,41)])
    forest.fire_areas([(1,2),(6,8)])
    forest.plot_forest()
