import set_params
import generations
import matplotlib.pyplot as plt

params = set_params.setparameters()
if params is not None:
    # Evaluate the population
    population_data, generation_number = generations.evaluate_population(params, params['Initial Population'])

    # Plot the results
    plt.plot(generation_number, population_data)
    plt.xlabel('Generation Number')
    plt.ylabel('Population Size')
    plt.title('Population Growth Over Generations')
    plt.grid()
    plt.show()