from packaging_aproximation import packaging_aproximation
from packaging_backtracking import packaging_backtracking
from packaging_brute_force import packaging_brute_force
from packaging_greedy import packaging_greedy

objects = [0.82, 0.46, 0.7, 0.32, 0.54, 0.31]
print(packaging_brute_force(objects))
print(packaging_backtracking(objects))
print(packaging_aproximation(objects))
print(packaging_greedy(objects))