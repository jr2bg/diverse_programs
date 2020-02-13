# dependencies
import numpy as np
import random

def fitness(cell):
    # si solo regresa cell, significa que está trabajando sobre una
    # función lineal

    return cell

def fitness_ratio(population_fitness):
    ''' función que calcula el cociente del fitness de toda la población'''
    total = sum(population_fitness)
    l_f_ratio = [x/total for x in population_fitness]
    return l_f_ratio

def a_fit_ratio(l_fit_ratio):
    ''' función que regresa el acumulado de la lista con los valores de fitness'''
    # como en programación dinámica
    accum_fit_ratio = [(0,l_fit_ratio[0])]
    # se toma desde el inicio hasta el final, por eso es que es una tupla
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


class CEA:
    def __init__(self, n_cols, n_rows, mutation_prob = 0.001):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.grid = np.zeros([n_rows,n_cols])
        self.p_m = mutation_prob

    def init_population(self):
        ''' inicializa la teselación con valores enteros entre 0 y 255'''
        with np.nditer(self.grid, op_flags = ['readwrite']) as it:
            for cell in it:
                cell[...] = random.randint(0 , 255)
        print(self.grid)

    def neigh(self,cell_pos):
        ''' método para extraer la vecindad alrededor de una célula del CA'''
        # creación del toroide
        neigh_rows = [(cell_pos[0] - 1) % self.n_rows, cell_pos[0]% self.n_rows,
                    (cell_pos[0] + 1)% self.n_rows]
        neigh_cols = [(cell_pos[1] - 1)% self.n_cols, cell_pos[1]% self.n_cols,
                    (cell_pos[1] + 1)% self.n_cols]

        nbg_np = self.grid[np.ix_(neigh_rows, neigh_cols)]
        ngb_l = list(np.concatenate(nbg_np).flat)
        # lista no anidada
        return ngb_l


    def evolution(self):
        ''' regla de evolución, iteración sobre cada elemento del grid'''
        #print("--- NEIGHBORHOODS---")
        with np.nditer(self.grid, op_flags = ['readwrite']) as it:
            # contador de la iteración sobre el arreglo de numpy
            i = 0
            for cell in it:
                l_fitness = [] # lista con el fitness de la vecindad

                # posición de la celda con respecto al número de iteraciones
                # sobre el arreglo del numpy
                cell_pos = (i// self.n_cols, i%self.n_cols)

                # numpy solo trabaja con floats, necesario pasarlo a int
                int_cell = int(cell)
                # vecindad como un arreglo plano
                ngbhood = self.neigh(cell_pos)

                for habitant in ngbhood:
                    l_fitness.append(fitness(habitant))
                #print(ngbhood)

                # determinación de las probabilidades para seleccionar los padres
                l_fitness = fitness_ratio(l_fitness)
                l_fitness = a_fit_ratio(l_fitness)

                # obtención de la posición de los padres
                pos_parents = parents_selection(l_fitness)

                # identificación de los padres y codeado a binario
                f_parent = bin(int(ngbhood[pos_parents[0]]))
                s_parent = bin(int(ngbhood[pos_parents[1]]))

                # remover el "0b" inicial del str
                f_parent = f_parent[2:]
                s_parent = s_parent[2:]

                #crossover
                f_child, s_child = crossover(f_parent, s_parent)

                #mutation
                f_child = mutation(f_child, self.p_m)
                s_child = mutation(s_child, self.p_m)

                # reconstruction
                f_child = int(f_child, 2)
                s_child = int(s_child, 2)

                # assotiation of the cell with a value
                if fitness(f_child) > fitness(s_child):
                    cell[...] = f_child
                else:
                    cell[...] = s_child

                # print(l_fitness)
                # print(pos_parents)
                # print(f_parent, s_parent)
                # print(cell)
                # print("")

                i +=1


def main():
    '''  función principal a ejecutar
    contiene información acerca de las dimensiones del CA,
    así como de la condición de paro '''
    n_cols = 5
    n_rows = 3
    cea = CEA(n_cols, n_rows, 0.05)
    cea.init_population()
    for i in range(20): # 20 iteraciones
        cea.evolution()
    print(cea.grid)
    print("SUCCESS")



if __name__ == "__main__":
    main()
