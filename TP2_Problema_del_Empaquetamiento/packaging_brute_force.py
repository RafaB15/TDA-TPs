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

    if bins[len(bins)-1]:
        bins.append([objects[position]])  
    else:
        bins[len(bins)-1].append(objects[position]) 

    packaging_brute_force_aux(position+1, objects, bins, min_bins)
    bins.pop()
