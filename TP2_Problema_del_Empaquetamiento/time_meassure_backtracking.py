from backtracking_final import packaging_backtracking
import time 
import matplotlib.pyplot as plt

def time_meassure_backtracking(objects):
    start = time.time()
    packaging_backtracking(objects)
    end = time.time()
    return (end - start) * 1000

def main():
    times = []
    amounts = []

    for i in range(1, 24):
        for j in range(1, 4):
            current_times = []
            with open("testing/amount_{}_version_{}.txt".format(i, j), 'r') as file:
                objects = []
                for line in file.readlines()[2:]:
                    objects.append(float(line))
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