def evaluate_one_generation(params, population):
    dt = 1.5
    """
    Evaluate one generation of the population.
    :param params: The parameters for the evaluation.
    :return: The evaluated generation.
    """
    new_population = population + abs(population) * params['Population Growth Rate'] * (params['Carrying Capacity'] - population)/params['Carrying Capacity'] * dt
    return new_population

def evaluate_population(params,debug):
    population_data = [params["Initial Population"]]
    population = params["Initial Population"]
    generation_number = [0]
    # Loop through the number of generations
    for i in range(params['Number of Generations']):
        # Evaluate the population for the current generation
        generation_number.append(i+1)
        population = evaluate_one_generation(params, population)
        population_data.append(round(population))
        if population < 0 and debug is False:
            print("Population has gone extinct.")
            break
        if population > 1e100:
            print("Population has exploded. Terminating simulation to prevent overflow error.") 
            break
    return population_data , generation_number
    # Return the population data for all generations
