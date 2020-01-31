# dependencies
import numpy as np

class cea:
    def __init__(self, n_cols, n_rows):
        self.dimensions = (n_rows,n_cols)
        self.grid = np.zeros([n_rows,n_cols])

    def neigh(self,cell_pos):
        ''' método para extraer el grid con los estados del CA'''
        neigh_rows = [cell_pos[0] - 1, cell_pos[0] , cell_pos[0] + 1] % self.dimensions[0]
        neigh_cols = [cell_pos[1] - 1, cell_pos[1] , cell_pos[1] + 1] % self.dimensions[1]

        return self.grid(np.ix_(neigh_rows, neigh_cols))

    def rules(grid_neigh):
        
        neighbours =

    def evolution():
        ''' regla de evolución, iteración sobre cada elemento del grid'''
        with np.nditer(self.grid, op_flags = ['readwrite']) as it:
            for cell in it:
                awfgvc

def interest_function(x):
    return x**2

# as it is a cellular evolutionary algorithm, there is a grid
