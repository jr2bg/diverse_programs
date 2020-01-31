# https://www.analyticsvidhya.com/blog/2017/07/introduction-to-genetic-algorithm/

# genetic algorithm to solve the knapsack problem

import random


def chromosome_start(n_genes):
    ''' función que llena el cromosoma de longitud n_genes con 0 XOR 1'''
    chromosome = ''
    for i in range(n_genes):
        chromosome += str(random.randint(0,1))
    return chromosome


def f_population(n_pop, n_genes):
    '''función que regresa a una poblacion de n_pop con n_genes'''
    population = [chromosome_start(n_genes) for x in range(n_pop)]
    return population

def crossover(f_parent, s_parent):
    ''' función para el intercambio de cromosomas entre los padres'''
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

def initialize_knapsack(n_items):
    ''' función que regresa un array 2D con el peso y la utilidad por objeto'''
    knapsack = []
    for i in range(n_items):
        print("introduzca el peso y el valor del objeto, separados por espacio (INT)")
        inpt = input()
        knapsack.append([int(y) for y in inpt.split()])

    #knapsack = [[1,5], [2,5], [6,9], [2,4], [8,11], [9,13], [4,7], [1,1]]
    return knapsack

def fitness(chromosome, knapsack, capacity):
    ''' función que calcula el fitness de un cromosoma'''
    weight = 0
    value = 0
    for i in range(len(chromosome)):
        if chromosome[i] == "1":
            weight += knapsack[i][0]
            value += knapsack[i][1]
    # consideramos el caso en que el peso sea menor o mayor que la capacidad
    if weight <= capacity:
        return value
    else:
        return value - weight

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


if __name__ == "__main__":
    n_genes = 5
    n_pop = 50
    n_items = n_genes  # deben ser el mismo
    capacity = 10
    p_m = 0.001


    knapsack = initialize_knapsack(n_items)
    population = f_population(n_pop, n_genes)


    # halt criteria, iteration's number
    n_iter = 20
    for i in range(n_iter):
        population_fitness = [fitness(chromo, knapsack, capacity) for chromo in population]
        l_fit_ratio = fitness_ratio(population_fitness)
        accum_fit_ratio = a_fit_ratio(l_fit_ratio)
        new_pop = []
        for j in range(n_pop):
            pos_parents = parents_selection(accum_fit_ratio)
            parents = [population[pos_parents[0]],population[pos_parents[1]]]
            f_child, s_child = crossover(parents[0], parents[1])
            f_child = mutation(f_child, p_m)
            s_child = mutation(s_child, p_m)

            if fitness(f_child, knapsack, capacity) >= fitness(s_child, knapsack, capacity):
                new_pop.append(f_child)
            else:
                new_pop.append(s_child)

        population = new_pop


    print(population)
