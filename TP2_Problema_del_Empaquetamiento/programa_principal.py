from packaging_backtracking_new_version import packaging_problem_backtracking
from packaging_aproximation import packaging_aproximation
from packaging_alternate_aproximation import first_fit


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
        bins = packaging_problem_backtracking(objects)
        print("Solución exacta: #" + str(bins))
    elif arguments[1] == "A":
        bins = packaging_aproximation(objects)
        print("Solución aproximada: #" + str(bins))
    elif arguments[1] == "A2":
        bins = first_fit(objects, 1)
        print("Solución Aproximada Alumnos: #" + str(bins))

    print(read_file(arguments[2]))

main()
