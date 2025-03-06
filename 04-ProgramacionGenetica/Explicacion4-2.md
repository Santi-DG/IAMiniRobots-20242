## 4.2
Suponga que desea utilizar Programación Genética para encontrar el diseño de un circuito lógico, tome como, ejemplo el codificador de 7 segmentos. Describa el conjunto de terminales, el conjunto de funciones y la función de aptitud.

## Sección 1: Definición de Conjuntos de Terminales y Funciones

* **Línea 7:** `pset = gp.PrimitiveSet("MAIN", 4)` - Crea un conjunto de primitivas llamado "MAIN" con 4 argumentos de entrada.
* **Línea 8:** `pset.addPrimitive(operator.and_, 2)` - Añade el operador lógico AND, que toma 2 argumentos.
* **Línea 9:** `pset.addPrimitive(operator.or_, 2)` - Añade el operador lógico OR, que toma 2 argumentos.
* **Línea 10:** `pset.addPrimitive(operator.not_, 1)` - Añade el operador lógico NOT, que toma 1 argumento.
* **Línea 11:** `pset.addPrimitive(operator.xor, 2)` - Añade el operador lógico XOR, que toma 2 argumentos.
* **Línea 12:** `pset.addTerminal(True)` - Añade la constante booleana `True` como un terminal.
* **Línea 13:** `pset.addTerminal(False)` - Añade la constante booleana `False` como un terminal.

## Sección 2: Creación de Tipos para Programación Genética (GP)

* **Línea 16:** `creator.create("FitnessMin", base.Fitness, weights=(-1.0,))` - Crea un tipo de aptitud llamado "FitnessMin" para minimizar el valor de aptitud (errores).
* **Línea 17:** `creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)` - Crea un tipo de individuo llamado "Individual" como un árbol de primitivas con el tipo de aptitud definido.

## Sección 3: Configuración de la Caja de Herramientas (Toolbox)

* **Línea 20:** `toolbox = base.Toolbox()` - Inicializa la caja de herramientas.
* **Línea 21:** `toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)` - Registra la función para generar expresiones (árboles de primitivas) usando el método "mitad y mitad".
* **Línea 22:** `toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)` - Registra la función para crear individuos iterando sobre las expresiones generadas.
* **Línea 23:** `toolbox.register("population", tools.initRepeat, list, toolbox.individual)` - Registra la función para crear poblaciones repitiendo la creación de individuos.
* **Línea 24:** `toolbox.register("compile", gp.compile, pset=pset)` - Registra la función para compilar árboles de primitivas en funciones ejecutables.

## Sección 4: Función de Aptitud (Fitness Function)

* **Líneas 27-34:** `def eval_decoder(individual, inputs, outputs): ...` - Define la función de aptitud que evalúa un individuo (circuito) comparando su salida con la salida deseada.
    * **Línea 28:** `func = toolbox.compile(expr=individual)` - Compila el árbol de primitivas del individuo en una función ejecutable.
    * **Línea 29:** `errors = 0` - Inicializa el contador de errores.
    * **Línea 30:** `for input_val, output_val in zip(inputs, outputs):` - Itera a través de pares de entrada y salida esperada.
    * **Línea 31:** `result = func(*input_val)` - Ejecuta la función compilada con la entrada actual.
    * **Línea 32:** `if result != output_val:` - Verifica si el resultado coincide con la salida esperada.
    * **Línea 33:** `errors += 1` - Incrementa el contador de errores si el resultado es incorrecto.
    * **Línea 34:** `return errors,` - Devuelve el número total de errores como la aptitud.

## Sección 5: Registro de la Función de Aptitud y Operadores Genéticos

* **Línea 37:** `toolbox.register("evaluate", eval_decoder, ...)` - Registra la función de aptitud `eval_decoder` con valores de entrada y salida específicos para la evaluación.
* **Línea 38:** `toolbox.register("select", tools.selTournament, tournsize=3)` - Registra el operador de selección por torneo con un tamaño de torneo de 3.
* **Línea 39:** `toolbox.register("mate", gp.cxOnePoint)` - Registra el operador de cruce de un punto.
* **Línea 40:** `toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)` - Registra la función para generar expresiones para la mutación usando el método "completo".
* **Línea 41:** `toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)` - Registra el operador de mutación uniforme.

## Sección 6: Decoradores para Limitar el Tamaño del Árbol

* **Línea 44:** `toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))` - Decora el operador de cruce para limitar la altura de los árboles después del cruce.
* **Línea 45:** `toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))` - Decora el operador de mutación para limitar la altura de los árboles después de la mutación.

## Sección 7: Configuración de la Población y Ejecución del Algoritmo Genético

* **Línea 48:** `pop = toolbox.population(n=300)` - Crea una población inicial de 300 individuos.
* **Línea 49:** `hof = tools.HallOfFame(1)` - Crea un objeto Hall of Fame para almacenar el mejor individuo.
* **Línea 50:** `stats = tools.Statistics(lambda ind: ind.fitness.values)` - Crea un objeto de estadísticas para rastrear las estadísticas de la población.
* **Líneas 51-54:** `stats.register("avg", ...)` - Registra estadísticas como la media, la desviación estándar, el mínimo y el máximo de la aptitud.
* **Línea 56:** `algorithms.eaSimple(pop, toolbox, 0.5, 0.2, 40, stats, halloffame=hof)` - Ejecuta el algoritmo evolutivo simple.

## Sección 8: Impresión del Mejor Individuo (Circuito) Encontrado

* **Línea 59:** `print(hof[0])` - Imprime el mejor individuo (circuito) encontrado por el algoritmo genético.
