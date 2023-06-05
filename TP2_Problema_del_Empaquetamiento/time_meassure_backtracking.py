from packaging_backtracking import packaging_backtracking
import time 
import matplotlib.pyplot as plt
import random

def time_meassure_backtracking(objects):
    start = time.time()
    packaging_backtracking(objects)
    end = time.time()
    return (end - start) * 1000

def generate_random_list(size):
    objects = []
    for i in range(size):
        objects.append(round(random.random(), 3))
    return objects

def main():
    random.seed(30)
    times = []
    amounts = []

    for i in range(50, 61):
        for j in range(1, 4):
            current_times = []
            objects = generate_random_list(i)
            print("Currently testing amount_{}_version_{}.txt".format(i, j))
            current_times.append(time_meassure_backtracking(objects))
        times.append(sum(current_times) / len(current_times))
        amounts.append(i)
    print("hola")
    plt.title("Tiempo de ejecución del algoritmo de backtracking \nal aumentar la cantidad de objetos")
    plt.xlabel("Cantidad de objetos")
    plt.ylabel("Tiempo de ejecución promedio (ms)")
    plt.plot(amounts,times, marker='o')
    plt.show()

main()