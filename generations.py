def evaluate_one_generation(params, population):
    dt = 1.5
    """
    Evaluate one generation of the population.
    :param params: The parameters for the evaluation.
    :return: The evaluated generation.
    """
    new_population = population + population * params['Population Growth Rate'] * (params['Carrying Capacity'] - population)/params['Carrying Capacity'] * dt
    return round(new_population)

def evaluate_population(params, population):
    population_data = [params["Initial Population"]]
    population = params["Initial Population"]
    generation_number = [0]
    # Loop through the number of generations
    for i in range(params['Number of Generations']):
        # Evaluate the population for the current generation
        generation_number.append(i+1)
        population = evaluate_one_generation(params, population)
        population_data.append(population)
        if population < 0:
            print("Population has gone extinct.")
            break
        print(population)
    return population_data , generation_number
    # Return the population data for all generations
