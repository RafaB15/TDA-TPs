from packets_dynamic import extract_packets_dynamic as ext_dyn
from packets_greedy import extract_packets_greedy as ext_greedy

#Se hacen pruebas con solo un tipo de producto porque solo queremos mostrar la optimalidad

packets1 = {'pringles':[7,8,1]}
packets2 = {'pringles':[7,8,2,3]}
packets3 = {'pringles':[2,3,1,2]}
packets4 = {'pringles':[4,2,1]}
target = {'pringles':5}

print(f"Dado los paquetes: {packets1} y el target: {target}")
print(f"Al extraer con el algoritmo greedy se obtienen: {ext_greedy(packets1, target)}")
print(f"Al extraer con el algoritmo de programacion dinamica se obtienen: {ext_dyn(packets1, target)}")
print(f"La solucion optima es [7]\n")


print(f"Dado los paquetes: {packets2} y el target: {target}")
print(f"Al extraer con el algoritmo greedy se obtienen: {ext_greedy(packets2, target)}")
print(f"Al extraer con el algoritmo de programacion dinamica se obtienen: {ext_dyn(packets2, target)}")
print(f"La solucion optima es [2,3]\n")

print(f"Dado los paquetes: {packets3} y el target: {target}")
print(f"Al extraer con el algoritmo greedy se obtienen: {ext_greedy(packets3, target)}")
print(f"Al extraer con el algoritmo de programacion dinamica se obtienen: {ext_dyn(packets3, target)}")
print(f"La solucion optima es [2,3] o [1,2,2]\n")

print(f"Dado los paquetes: {packets4} y el target: {target}")
print(f"Al extraer con el algoritmo greedy se obtienen: {ext_greedy(packets4, target)}")
print(f"Al extraer con el algoritmo de programacion dinamica se obtienen: {ext_dyn(packets4, target)}")
print(f"La solucion optima es [1,4]\n")
