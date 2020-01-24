# dependencies
import numpy as np

class cea:
    def __init__(self, n_cols, n_rows):
        self.dimensions = (n_rows,n_cols)
        self.grid = np.zeros([n_rows,n_cols])

    def neigh(neighbourhood):
        ''' método para asignar una vecindad como la usar'''
        self.neighbourhood = neighbourhood

    def rules(cell):
        neighbours = 

    def evolution():
        ''' regla de evolución, iteración sobre cada elemento del grid'''
        with np.nditer(self.grid, op_flags = ['readwrite']) as it:
            for cell in it:
                awfgvc

def interest_function(x):
    return x**2

# as it is a cellular evolutionary algorithm, there is a grid
