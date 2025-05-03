import set_params
import generations
import graph_results
import matplotlib.pyplot as plt

tutorial = input("Welcome to the Population Growth Simulation! Would you like to see a tutorial? (y/n): ").strip().lower()
if tutorial == 'y':
    print("\nThis simulation models the growth of a population over time.")
    print("You will be prompted to enter the following parameters:")
    print("1. Number of generations: The total number of generations to simulate. This must be a positive integer.")
    print("2. Initial population: The size of the population at the start of the simulation. This must be a positive integer.")
    print("3. Carrying capacity: The maximum population size that the environment can sustain. This must be an integer greater than the initial population.")
    print("4. Population growth rate: The rate at which the population grows. It can be any positive number and may have decimals.")
    print("If you enter invalid values, the program will default to the following:")
    print("Number of generations: 100")
    print("Initial population: 1000")
    print("Carrying capacity: 5000")
    print("Population growth rate: 0.1")
    print("After entering or defaulting parameters, the simulation will run and display the results in a separate window.\n")

mode_selection = input("Do you want dark or light mode? (d/l): ").strip().lower()
if mode_selection == 'd':
    plt.style.use('dark_background')
params = set_params.setparameters()
graph_results.graph_data(params)
exit(0)