from packaging_backtracking import packaging_backtracking
from packaging_aproximation_next_fit import next_fit
from packaging_aproximation_first_fit import first_fit
import time

import sys

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        objects = []
        for i in range(2, len(lines)):
            objects.append(float(lines[i].strip()))
    return objects

def main():
    arguments = sys.argv
    if len(arguments) != 3:
        print("Error: la cantidad de argumentos es incorrecta")
        print("Usa: python3 programa_principal.py <E|A|A2> <archivo_datos>")
        return

    objects = read_file(arguments[2])
    if arguments[1] == "E":
        start = time.time()
        bins = packaging_backtracking(objects)
        end = time.time()
        print("Solución exacta: #" + str(bins))
    elif arguments[1] == "A":
        start = time.time()
        bins = next_fit(objects)
        end = time.time()
        print("Solución aproximada: #" + str(bins))
    elif arguments[1] == "A2":
        start = time.time()
        bins = first_fit(objects)
        end = time.time()
        print("Solución Aproximada Alumnos: #" + str(bins))

    print("Ejecutado en " + str((end - start) * 1000) + " milisegundos")

main()
