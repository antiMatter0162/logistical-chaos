def setparameters():
    """
    Set parameters for the simulation.
    """
    # Simulation parameters
    num_gens = input("Enter the number of generations: ")
    init_population = input("Enter the initial population: ")
    carrying_capacity = input("Enter the carrying capacity of the environment: ")
    pop_growth_rate = input("Enter the population growth rate: ")
    
    try:
        num_gens = int(num_gens)
        init_population = int(init_population)
        carrying_capacity = int(carrying_capacity)
        pop_growth_rate = float(pop_growth_rate)
    except ValueError:
        print("Invalid input. Please enter integers for number of generations and initial population.")
        return None
    if pop_growth_rate <= 0:
        print("Population growth rate must be a positive number. Defaulting to 0.1.")
        pop_growth_rate = 0.1
    params = {
        'Number of Generations': num_gens,  # Total number of generations
        'Initial Population': init_population,  # Population size at the start of the simulation
        'Carrying Capacity': carrying_capacity,  # Carrying capacity of the environment
        'Population Growth Rate': pop_growth_rate,  # Growth rate constant of the population
    }
    
    return params