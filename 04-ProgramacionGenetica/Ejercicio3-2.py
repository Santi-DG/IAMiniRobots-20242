import operator
import random
import numpy
from deap import algorithms, base, creator, tools, gp

# Definición del conjunto de terminales y funciones
pset = gp.PrimitiveSet("MAIN", 4)
pset.addPrimitive(operator.and_, 2)
pset.addPrimitive(operator.or_, 2)
pset.addPrimitive(operator.not_, 1)
pset.addPrimitive(operator.xor, 2)
pset.addTerminal(True)
pset.addTerminal(False)

# Creación de tipos para GP
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

# Configuración de la caja de herramientas
toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

# Función de aptitud (ejemplo simplificado)
def eval_decoder(individual, inputs, outputs):
    func = toolbox.compile(expr=individual)
    errors = 0
    for input_val, output_val in zip(inputs, outputs):
        result = func(*input_val)
        if result != output_val:
            errors += 1
    return errors,

# Registro de la función de aptitud y operadores genéticos
toolbox.register("evaluate", eval_decoder, inputs=[(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 1, 0), (0, 1, 1, 1), (1, 0, 0, 0), (1, 0, 0, 1)], outputs=[True, False, False, True, False, True, True, False, False, True]) # ejemplo de outputs para un segmento
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

# Decoradores para limitar el tamaño de los árboles
toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

# Configuración de la población y ejecución del algoritmo genético
pop = toolbox.population(n=300)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", numpy.mean)
stats.register("std", numpy.std)
stats.register("min", numpy.min)
stats.register("max", numpy.max)

algorithms.eaSimple(pop, toolbox, 0.5, 0.2, 40, stats, halloffame=hof)

# Impresión del mejor individuo (circuito) encontrado
print(hof[0])