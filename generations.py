def evaluate_one_generation(params, population):
    """
    Evaluate one generation of the population.
    :param params: The parameters for the evaluation.
    :return: The evaluated generation.
    """
    new_population = params['Population Growth Rate'](population - params['Carrying Capacity'])
    return new_population

def evaluate_population(params, population):
    population_data = [params["Initial Population"]]
    population = params["Initial Population"]
    generation_number = []
    # Loop through the number of generations
    for i in range(len(params['Number of Generations'])):
        # Evaluate the population for the current generation
        generation_number.append(i)
        population = evaluate_one_generation(params, population)
        population_data.append(population)
        if population < 0:
            print("Population has gone extinct. This shouldn't happen.")
            break
        print(population)
    return population_data , generation_number
    # Return the population data for all generations
