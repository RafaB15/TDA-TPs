import random
from packaging_aproximation_next_fit import next_fit
from packaging_aproximation_first_fit import first_fit
from packaging_aproximation_best_fit import best_fit
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

    times_nf = []
    times_ff = []
    times_bf = []

    results_nf = []
    results_ff = []
    results_bf = []

    amounts = []

    for i in range(1, 50):
        for j in range(1, 4):
            
            current_times_nf = []
            current_times_ff = []
            current_times_bf = []

            current_results_nf = []
            current_results_ff = []
            current_results_bf = []

            objects = generate_random_list(i)
            print("Currently testing amount_{}_version_{}.txt".format(i, j))

            time_nf, result_nf = time_meassure(objects, next_fit)
            time_ff, result_ff = time_meassure(objects, first_fit)
            time_bf, result_bf = time_meassure(objects, best_fit)

            current_times_nf.append(time_nf)
            current_times_ff.append(time_ff)
            current_times_bf.append(time_bf)

            current_results_nf.append(result_nf)
            current_results_ff.append(result_ff)
            current_results_bf.append(result_bf)

        times_nf.append(sum(current_times_nf) / len(current_times_nf))
        times_ff.append(sum(current_times_ff) / len(current_times_ff))
        times_bf.append(sum(current_times_bf) / len(current_times_bf))

        results_nf.append(sum(current_results_nf) / len(current_results_nf))
        results_ff.append(sum(current_results_ff) / len(current_results_ff))
        results_bf.append(sum(current_results_bf) / len(current_results_bf))
        
        amounts.append(i)

    plt.title("Tiempo de ejecución de diferentes algoritmos de aproximación")
    plt.xlabel("Cantidad de objetos")
    plt.ylabel("Tiempo de ejecución promedio (ms)")
    plt.plot(amounts,times_nf, marker='o', color = 'red')
    plt.plot(amounts,times_ff, marker='o', color = 'blue')
    plt.plot(amounts,times_bf, marker='o', color = 'green')
    plt.legend(["Next Fit", "First Fit", "Best Fit"])
    plt.show()

    plt.title("Cantidad de paquetes de diferentes algoritmos de\n aproximación al aumentar la cantidad de objetos")
    plt.xlabel("Cantidad de objetos")
    plt.ylabel("Cantidad de paquetes promedio")
    plt.plot(amounts,results_nf, marker='o', color = 'red')
    plt.plot(amounts,results_ff, marker='o', color = 'blue')
    plt.plot(amounts,results_bf, marker='o', color = 'green')
    plt.legend(["Next Fit", "First Fit", "Best Fit"])
    plt.show()

main()