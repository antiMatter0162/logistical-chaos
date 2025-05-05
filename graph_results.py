import generations
import matplotlib.pyplot as plt

def graph_data(params):
    if params is not None:
        # Evaluate the population
        population_data, generation_number = generations.evaluate_population(params, params['Initial Population'])

        # Plot the results
        fig = plt.figure(figsize=(10, 6))
        plt.plot(generation_number, population_data)
        fig.canvas.manager.set_window_title('Population Growth Simulation')
        plt.xlabel('Generation Number')
        plt.ylabel('Population Size')
        plt.title('Population Growth Over Generations')
        plt.grid()
        plt.show()