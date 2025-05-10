import generations
import matplotlib.pyplot as plt

def graph_data(params, include_carrying_capacity, debug):
    if params is not None:
        # Evaluate the population
        population_data, generation_number = generations.evaluate_population(params, params['Initial Population'],debug)

        # Plot the results
        fig = plt.figure(figsize=(10, 6))
        plt.plot(generation_number, population_data)
        fig.canvas.manager.set_window_title('Population Growth Simulation')
        # Extremely scuffed solution issue of dimensions being different between the two lists but it works for every case
        if include_carrying_capacity is True:
            carrying_capacity_list = []
            for i in range(len(generation_number)):
                carrying_capacity_list.append(params["Carrying Capacity"])
            plt.plot(generation_number, carrying_capacity_list, 'r--', label='Carrying Capacity')
            plt.legend()
        plt.xlabel('Generation Number')
        plt.ylabel('Population Size')
        plt.title('Population Growth Over Generations')
        plt.grid()
        plt.show()