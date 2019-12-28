# Example provided by the book Artificial Intelligence, A Guide to Intelligent Systems
# Part 7: Evolutionary algorithms
from random import randint, random

def chromo_st(len_code):
    chromo = ""
    for i in range(len_code):
        chromo += str(randint(0,1))
    return chromo

def decoded_chromo(chromo):
    dec_chromo = 0
    for i in range(len(chromo)):
        dec_chromo += int(chromo[-i-1]) * 2 ** i
    return dec_chromo

def start_population(n_pop, len_code):
    population = []
    for i in range(n_pop):
        population.append(chromo_st(len_code))
    return population

def fitness_func(x):
    return 15*x - x**2

def chromo_fitness(population):
    l_fitness = []
    # para cada elemento de la población
    for being in population:
        # obtenemos su valor de fitness con respecto al número que representa
        # su cromosoma
        l_fitness.append(fitness_func(decoded_chromo(being)))
    return l_fitness


def fitness_ratio(l_fitness):
    l_fit_ratio = []
    sum_fit = 0
    for fitness in l_fitness:
        sum_fit += fitness

    for fitness in l_fitness:
        l_fit_ratio.append(fitness / sum_fit)

    return l_fit_ratio

# probabilidad acumulada
def accum_fit_ratio(l_fit_ratio):
    l_a_fit_ratio = []
    for i in range(len(l_fit_ratio)):
        if i == 0:
            l_a_fit_ratio.append(l_fit_ratio[i])
        else:
            l_a_fit_ratio.append(l_fit_ratio[i] + l_a_fit_ratio[i-1])
    return l_a_fit_ratio

# función de selección de los padres
def roulette_wheel_selection(l_fit_ratio):
    l_a_fit_ratio = accum_fit_ratio(l_fit_ratio)
    # different parents
    f_trial = random()
    s_trial = random()
    f_parent = 0
    s_parent = 0
    s_list = l_fit_ratio.copy() # copia para el segundo padre

    for i in range(len(l_a_fit_ratio)):
        # probabilidad acumulada es mayor al número encontrado
        if l_a_fit_ratio[i] >= f_trial:
            f_parent = i
            prob_i = s_list.pop(i)
            #print("probabilidad de primer padre", prob_i)
            break
    l_a_fit_ratio = accum_fit_ratio(s_list)
    # ciclo que encuentra otro padre diferente al primero pseudo aleatoriamente
    for i in range(len(l_a_fit_ratio)):
        if l_a_fit_ratio[i] >= (s_trial)/(1 - prob_i):
            s_parent = i
            break

    return f_parent, s_parent

# función de crossover
def crossover_operator(s_parents, len_code, crossover_prob = 0.7):
    # NO intercambio de cromosomas
    if random() > crossover_prob:
        return s_parents[0], s_parents[1]
    # intercambio de cromosomas
    else:
        # posición a cortar, aleatoria
        cut_pos = randint(1, len_code - 1)
        # intercambio de genes
        f_children = s_parents[0][:cut_pos] + s_parents[1][cut_pos:]
        s_children = s_parents[1][:cut_pos] + s_parents[0][cut_pos:]

        return f_children, s_children


# mutación de los genes
def mutation_operator(child, len_code, mutation_prob = 0.001):
    if random() <= mutation_prob:
        l_child = list(child)
        for i in range(len_code):
            # si llega a haber mutación
            if random() <= mutation_prob:
                # intercambia los valores
                if l_child[i] == "0":
                    l_child[i] = "1"
                else:
                    l_child[i] = "1"
        # regresa un string
        child = "".join(l_child)
    return child

# función que retorna la nueva población
# probabilidades de crossover y de mutación se mantienen como las sugeridas
def f_new_pop(start_pop, l_fit_ratio, n_pop ,len_code,
            crossover_prob = 0.7, mutation_prob = 0.001 ):
    new_pop = []
    # hasta que la nueva población tenga los mismos habitantes que la inicial
    while len(new_pop) < n_pop:
        # selección de los padres
        parents = roulette_wheel_selection(l_fit_ratio)
        s_parents = (start_pop[parents[0]], start_pop[parents[1]])
        # non-mutated children
        children = crossover_operator(s_parents, len_code, crossover_prob)

        # mutated-children
        m_child_0 = mutation_operator(children[0], len_code, mutation_prob)
        m_child_1 = mutation_operator(children[1], len_code, mutation_prob)

        # anexo a la nueva población
        new_pop.append(m_child_0)
        new_pop.append(m_child_1)

    return new_pop

# función que determina si se cumple o no la condición de terminación
def termination_criterion(population):
    # la diferencia entre los números mayor y menor sea menor o igual a 5
    if abs(max(population)-min(population)) <= 2:
        return True
    else:
        return False


if __name__ == "__main__":

    len_code = 4
    n_pop = 6
    is_termination = False
    # población aleatoria
    start_pop = start_population(n_pop, len_code)


    while not is_termination:
        print(start_pop)

        # fitness de cada individuo
        l_fitness = chromo_fitness(start_pop)
        print(l_fitness)

        #fitness ratio
        l_fit_ratio = fitness_ratio(l_fitness)

        # nueva población
        start_pop = f_new_pop(start_pop, l_fit_ratio, n_pop ,len_code)

        # condición de terminación
        is_termination = termination_criterion(l_fitness)

    # población final después de la condición de terminación
    print("POBLACIÓN FINAL --- ", start_pop)
