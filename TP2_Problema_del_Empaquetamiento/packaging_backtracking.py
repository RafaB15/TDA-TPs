MAX_BIN_SIZE = 1
INFINITY = 10000000000000000000000000000

def packaging_brute_force(objects):
    bins = [[]]
    min_bins = [INFINITY]
    packaging_brute_force_aux(0, objects, bins, min_bins)
    return min_bins[0]

def packaging_brute_force_aux(position, objects, bins, min_bins):
    size = len(objects)
    if position == size:
        if(len(bins) < min_bins[0]):
            min_bins[0] = len(bins)
        print(bins)
        return
    
    for i in range(len(bins)):
        if objects[position] + sum(bins[i]) <= MAX_BIN_SIZE:
            bins[i].append(objects[position])
            packaging_brute_force_aux(position+1, objects, bins, min_bins)
            bins[i].remove(objects[position])

    bins.append([objects[position]])
    packaging_brute_force_aux(position+1, objects, bins, min_bins)
    bins.pop()


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
        print(bins)
        return
    
    for i in range(len(bins)):
        if objects[position] + sum(bins[i]) <= MAX_BIN_SIZE and len(bins) < min_bins[0]:
            bins[i].append(objects[position])
            packaging_backtracking_aux(position+1, objects, bins, min_bins)
            bins[i].remove(objects[position])

    if len(bins) < min_bins[0]:
        bins.append([objects[position]])
        packaging_backtracking_aux(position+1, objects, bins, min_bins)
        bins.pop()


def packaging_aproximation(objects):

    bins = []
    i = 0
    while i < len(objects):
        bins.append([])
        while i < len(objects) and objects[i] + sum(bins[len(bins)-1]) <= MAX_BIN_SIZE:
            bins[len(bins)-1].append(objects[i])
            i+=1

    print(bins)
    return len(bins)

objects = [0.82, 0.46, 0.7, 0.32, 0.54, 0.31,0.54, 0.31,0.54, 0.31,0.54, 0.31,0.54, 0.31,0.54, 0.31,0.54, 0.31,0.54, 0.31,0.54, 0.31,0.54, 0.31,0.54, 0.31,0.54, 0.31,0.54, 0.31]
print(packaging_brute_force(objects))
print(packaging_backtracking(objects))
print(packaging_aproximation(objects))