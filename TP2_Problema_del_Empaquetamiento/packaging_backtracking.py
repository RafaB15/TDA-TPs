MAX_BIN_SIZE = 1
INFINITY = 10000000000000000000000000000

def packaging_backtracking(objects):
    bins = [[]]
    min_bins = [INFINITY]
    packaging_backtracking_aux(0, objects, bins, min_bins)
    return min_bins[0]

def packaging_backtracking_aux(position, objects, bins, min_bins):
    size = len(objects)
    if position == size:
        if(len(bins) < min_bins[0]):
            min_bins[0] = len(bins)
        return
    
    for i in range(len(bins)):
        if objects[position] + sum(bins[i]) <= MAX_BIN_SIZE and len(bins) < min_bins[0]:
            bins[i].append(objects[position])
            packaging_backtracking_aux(position+1, objects, bins, min_bins)
            bins[i].remove(objects[position])

    if len(bins) >= min_bins[0]:
        return
    
    if bins[len(bins)-1]:
        bins.append([objects[position]])  
    else:
        bins[len(bins)-1].append(objects[position]) 
    packaging_backtracking_aux(position+1, objects, bins, min_bins)
    bins.pop()

objects = [0.4, 0.6, 0.2, 0.6, 0.1, 0.9, 0.12, 0.87, 0.65, 0.41, 0.1, 0.9, 0.12, 0.87, 0.65, 0.41]
print(packaging_backtracking(objects))
