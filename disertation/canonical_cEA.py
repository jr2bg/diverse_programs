# dependencies
import numpy as np

def fitness(cell):
    pass

def fitness_ratio(population_fitness):
    ''' función que calcula el cociente del fitness de toda la población'''
    total = sum(population_fitness)
    l_f_ratio = [x/total for x in population_fitness]
    return l_f_ratio

def a_fit_ratio(l_fit_ratio):
    ''' función que regresa el acumulado de la lista con los valores de fitness'''
    # como en programación dinámica
    accum_fit_ratio = [(0,l_fit_ratio[0])]

    for fit in l_fit_ratio[1:]:
        accum_fit_ratio.append((accum_fit_ratio[-1][1],accum_fit_ratio[-1][1] + fit))

    return accum_fit_ratio

def parents_selection(accum_fit_ratio):
    ''' función que regresa a los progenitores '''
    # se usa la 'ruleta'
    pos_parents = []
    # REEMPLAZO
    # número aleatorio para saber qué padres escoger
    point = random.random()
    if point <= 0.5:
        n_point = point + 0.5
    else:
        n_point = point - 0.5
    for i in range(len(accum_fit_ratio)):
        if  accum_fit_ratio[i][0] <= point <= accum_fit_ratio[i][1]:
            pos_parents.append(i)
        if accum_fit_ratio[i][0] <= n_point <= accum_fit_ratio[i][1]:
            pos_parents.append(i)

    return pos_parents

def crossover(f_parent, s_parent):
    ''' función para el intercambio de cromosomas entre los padres
     toma la mitad de uno y la reemplaza en la otra mitad'''
    l_cut = len(f_parent) // 2
    r_cut = len(f_parent) - l_cut

    f_child = f_parent[:l_cut] + s_parent[l_cut:]
    s_child = s_parent[:l_cut] + f_parent[l_cut:]
    return f_child, s_child

def mutation(child, p_m):
    ''' función de mutación con probabilidad p_m'''
    child = list(child) # cadenas son inmutables, necesario pasar a lista
    for i in range(len(child)):
        if random.random() <= p_m:
            if child[i] == "0":
                child[i] = "1"
            else:
                child[i] = "0"
    child = "".join(child)  # lo regresa un str
    return child


class cea:
    def __init__(self, n_cols, n_rows):
        self.dimensions = (n_rows,n_cols)
        self.grid = np.zeros([n_rows,n_cols])

    def neigh(self,cell_pos):
        ''' método para extraer la vecindad alrededor de una célula del CA'''
        neigh_rows = [cell_pos[0] - 1, cell_pos[0] , cell_pos[0] + 1] % self.dimensions[0]
        neigh_cols = [cell_pos[1] - 1, cell_pos[1] , cell_pos[1] + 1] % self.dimensions[1]

        return self.grid(np.ix_(neigh_rows, neigh_cols))

    def parent_selection(cell_neigh):
        ''' cell_neigh es una vecindad alrededor de una célula'''

    def rules(grid_neigh):

        neighbours =

    def evolution(self):
        ''' regla de evolución, iteración sobre cada elemento del grid'''
        with np.nditer(self.grid, op_flags = ['readwrite']) as it:
            for cell in it:
                cell[...] =

def interest_function(x):
    return x**2

# as it is a cellular evolutionary algorithm, there is a grid
