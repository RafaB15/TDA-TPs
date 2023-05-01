def min_packets(amounts, requested_amount):
    #Calculamos la diferencia de maxima cantidad que podmeos llenar con lo requerido
    max_items = sum(amounts)
    new_capacity = max_items - requested_amount

    #Creamos la matriz en donde guardaremos nuestras sumas
    table = [[0] * (new_capacity + 1) for _ in range(len(amounts) + 1)]

    #Iteramos sobre la matriz
    for i in range(1, len(amounts) + 1):
        for j in range(1, new_capacity + 1):
            if amounts[i - 1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], amounts[i - 1] + table[i-1][j - amounts[i - 1]])
    
    i, j = len(amounts), new_capacity

    not_selected = set()
    while i > 0 and j > 0:
        if table[i][j] != table[i-1][j]:
            not_selected.add(i-1)
            j -= amounts[i-1]
        i -= 1
    selected = set(range(len(amounts))) - not_selected
    
    extracted = []
    for index in selected:
        extracted.append(amounts[index])

    return extracted

def extract_packets_dynamic(packets, requests):
    extracted = {}
    for request in requests:
        extracted[request] = min_packets(packets[request], requests[request])
    
    return extracted