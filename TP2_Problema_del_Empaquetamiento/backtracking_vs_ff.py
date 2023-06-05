import random
from packaging_backtracking import packaging_backtracking
from packaging_aproximation_first_fit import first_fit
import time 
import matplotlib.pyplot as plt

def time_meassure(objects, algorithm):
    start = time.time()
    result = algorithm(objects)
    end = time.time()
    duration = (end - start) * 1000
    return duration, result

def generate_random_list(size):
    objects = []
    for i in range(size):
        objects.append(round(random.random(), 3))
    return objects

def main():

    random.seed(30)

    times_backtracking = []
    times_ff = []
    results_backtracking = []
    results_ff = []
    amounts = []

    for i in range(1, 65):
            
        current_times_backtracking = []
        current_times_ff = []
        
        current_results_backtracking = []
        current_results_ff = []

        objects = generate_random_list(i)
        print("Currently testing amount_{}.txt".format(i))

        time_backtracking, result_backtracking = time_meassure(objects, packaging_backtracking)
        time_ff, result_ff = time_meassure(objects, first_fit)

        current_times_backtracking.append(time_backtracking)
        current_times_ff.append(time_ff)

        current_results_backtracking.append(result_backtracking)
        current_results_ff.append(result_ff)

        times_backtracking.append(sum(current_times_backtracking) / len(current_times_backtracking))
        times_ff.append(sum(current_times_ff) / len(current_times_ff))

        results_backtracking.append(sum(current_results_backtracking) / len(current_results_backtracking))
        results_ff.append(sum(current_results_ff) / len(current_results_ff))

        amounts.append(i)

        if i % 5 == 0:
            plt.title("Tiempo de ejecución del algoritmo de backtracking y la\n aproximación first fit al aumentar la cantidad de objetos")
            plt.xlabel("Cantidad de objetos")
            plt.ylabel("Tiempo de ejecución (ms)")
            plt.plot(amounts,times_backtracking, marker='o')
            plt.plot(amounts,times_ff, marker='o')
            plt.legend(["Backtracking", "First Fit"])
            plt.show()

            plt.title("Cantidad de paquetes del algoritmo de backtracking y la \naproximación first fit al aumentar la cantidad de objetos")
            plt.xlabel("Cantidad de objetos")
            plt.ylabel("Cantidad de paquetes")
            plt.plot(amounts,results_backtracking, marker='o')
            plt.plot(amounts,results_ff, marker='o')
            plt.legend(["Backtracking", "First Fit"])
            plt.show()

    plt.title("Tiempo de ejecución del algoritmo de backtracking y la\n aproximación first fit al aumentar la cantidad de objetos")
    plt.xlabel("Cantidad de objetos")
    plt.ylabel("Tiempo de ejecución (ms)")
    plt.plot(amounts,times_backtracking, marker='o')
    plt.plot(amounts,times_ff, marker='o')
    plt.legend(["Backtracking", "First Fit"])
    plt.show()

    plt.title("Cantidad de paquetes del algoritmo de backtracking y la \naproximación first fit al aumentar la cantidad de objetos")
    plt.xlabel("Cantidad de objetos")
    plt.ylabel("Cantidad de paquetes")
    plt.plot(amounts,results_backtracking, marker='o')
    plt.plot(amounts,results_ff, marker='o')
    plt.legend(["Backtracking", "First Fit"])
    plt.show()

main()