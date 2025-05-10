import set_params
import generations
import graph_results
import matplotlib.pyplot as plt

tutorial = input("\nWelcome to the Population Growth Simulation! Would you like to see a tutorial?  (y/n): ").strip().lower()
if tutorial == 'y':
    print("\nThis simulation models the growth of a population over time.")
    print("You will be prompted to enter the following parameters:")
    print("1. Number of generations: The total number of generations to simulate. This must be a positive integer.")
    print("2. Initial population: The size of the population at the start of the simulation. This must be a positive integer.")
    print("3. Carrying capacity: The maximum population size that the environment can sustain. This must be an integer and is reccomended to be greater than the initial population.")
    print("4. Population growth rate: The rate at which the population grows. It can be any positive number and may have decimals.")
    print("If you enter invalid values, the program will default to the following:")
    print("Number of generations: 100")
    print("Initial population: 1000")
    print("Carrying capacity: 5000")
    print("Population growth rate: 0.1")
    print("After entering or defaulting parameters, the simulation will run and display the results in a separate window.\n")
elif tutorial == 'n':
    print("\nProceeding to customization.")
else:
    print("\nInvalid selection, proceeding to customization.")

mode_selection = input("\nWould you like a dark or light mode graph? (d/l): ").strip().lower()
if mode_selection == 'd':
    print("\nDark mode selected.")
    plt.style.use('dark_background')
elif mode_selection == 'l':
    print("\nLight mode selected.")
    plt.style.use('default')
else:
    print("\nInvalid selection. Defaulting to light mode.")
    plt.style.use('default')

include_carrying_capacity = input("\nWould you like to include the carrying capacity in the graph? (y/n): ").strip().lower()
if include_carrying_capacity == 'y':
    print("\nThe carrying capacity will be included in the graph.")
    include_carrying_capacity = True
    debug = False
elif include_carrying_capacity == 'n':
    print("\nThe carrying capacity will not be included in the graph.")
    include_carrying_capacity = False
    debug = False
elif include_carrying_capacity == 'schrodingercat':
    print("\nDebug mode activated. Errors are to be expected.")
    include_carrying_capacity = False
    debug = True
else:
    print("\nInvalid selection. Defaulting to not including the carrying capacity in the graph.")
    include_carrying_capacity = False
    debug = False
    
params = set_params.setparameters()
save = input("\n(Not recommended for large numbers of populations) Would you like to print the results to the console? (y/n): ").strip().lower()
if save == 'y':
    population_data, generation_number = generations.evaluate_population(params, params['Initial Population'], debug)
    print("\nPopulation data:")
    for i in range(len(population_data)):
        print(f"Generation {generation_number[i]}: Population {population_data[i]}")
elif  save == 'n':
    print("Results will not be printed to the console.")
else:
    print("Invalid selection. Defaulting to not printing results to the console.")
graph_results.graph_data(params,include_carrying_capacity,debug)
print("\nSimulation complete. Thank you for using the Population Growth Simulation.\n")
exit(0)