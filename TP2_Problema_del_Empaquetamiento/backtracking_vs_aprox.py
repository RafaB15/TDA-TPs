from backtracking_final import packaging_backtracking
from packaging_aproximation import packaging_aproximation
import time 
import matplotlib.pyplot as plt

def time_meassure(objects, algorithm):
    start = time.time()
    result = algorithm(objects)
    end = time.time()
    duration = (end - start) * 1000
    return duration, result

def main():
    times_backtracking = []
    times_aprox = []
    results_backtracking = []
    results_aprox = []
    amounts = []

    for i in range(1, 24):
        for j in range(1, 4):
            
            current_times_backtracking = []
            current_times_aprox = []
            
            current_results_backtracking = []
            current_results_aprox = []

            with open("testing/amount_{}_version_{}.txt".format(i, j), 'r') as file:
                
                objects = []
                for line in file.readlines()[2:]:
                    objects.append(float(line))
                print("Currently testing amount_{}_version_{}.txt".format(i, j))

                time_backtracking, result_backtracking = time_meassure(objects, packaging_backtracking)
                time_aprox, result_aprox = time_meassure(objects, packaging_aproximation)

                current_times_backtracking.append(time_backtracking)
                current_times_aprox.append(time_aprox)

                current_results_backtracking.append(result_backtracking)
                current_results_aprox.append(result_aprox)

        times_backtracking.append(sum(current_times_backtracking) / len(current_times_backtracking))
        times_aprox.append(sum(current_times_aprox) / len(current_times_aprox))

        results_backtracking.append(sum(current_results_backtracking) / len(current_results_backtracking))
        results_aprox.append(sum(current_results_aprox) / len(current_results_aprox))

        amounts.append(i)

    plt.title("Tiempo de ejecución del algoritmo de backtracking y la\n aproximación al aumentar la cantidad de objetos")
    plt.xlabel("Cantidad de objetos")
    plt.ylabel("Tiempo de ejecución promedio (ms)")
    plt.plot(amounts,times_backtracking, marker='o')
    plt.plot(amounts,times_aprox, marker='o')
    plt.legend(["Backtracking", "Aproximación"])
    plt.show()

    plt.title("Cantidad de paquetes del algoritmo de backtracking y la \naproximación al aumentar la cantidad de objetos")
    plt.xlabel("Cantidad de objetos")
    plt.ylabel("Cantidad de paquetes promedio")
    plt.plot(amounts,results_backtracking, marker='o')
    plt.plot(amounts,results_aprox, marker='o')
    plt.legend(["Backtracking", "Aproximación"])
    plt.show()

main()