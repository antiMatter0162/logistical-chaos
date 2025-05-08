def setparameters():
    """
    Set parameters for the simulation.
    """
    # Simulation parameters
    num_gens = input("\nEnter the number of generations: ")
    init_population = input("Enter the initial population: ")
    carrying_capacity = input("Enter the carrying capacity of the environment: ")
    pop_growth_rate = input("Enter the population growth rate: ")
    
    try:
        num_gens = int(num_gens)
        init_population = int(init_population)
        carrying_capacity = int(carrying_capacity)
        pop_growth_rate = float(pop_growth_rate)
    except ValueError:
        #Handle invalid input by setting default values
        print("Invalid input. Please enter integers for number of generations and initial population, and float for growth rate.")
        print("Defaulting to 100 generations, 1000 initial population, 5000 carrying capacity, and 0.1 growth rate.")
        num_gens = 100
        init_population = 1000
        carrying_capacity = 5000
        pop_growth_rate = 0.1
    if num_gens <= 0:
        print("Number of generations must be a positive integer. Defaulting to 100.")
        num_gens = 100
    if init_population <= 0:
        print("Initial population must be a positive integer. Defaulting to 1000.")
        init_population = 1000
    if carrying_capacity <= 0:
        print("Carrying capacity must be a positive integer. Defaulting to 5000.")
        carrying_capacity = 5000
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