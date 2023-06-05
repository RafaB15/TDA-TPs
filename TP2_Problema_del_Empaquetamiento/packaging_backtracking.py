from packaging_aproximation_first_fit import first_fit

MAX_BIN_SIZE = 1

def packaging_backtracking(objects):
    bins = []
    min_bins = first_fit(objects)
    objects.sort(reverse=True)
    min_bins = packaging_backtracking_aux(0, objects, bins, min_bins)
    return min_bins

def packaging_backtracking_aux(position, objects, bins, min_bins):
    size = len(objects)
    if position == size:
        if(len(bins) < min_bins):
            min_bins = len(bins)
        return min_bins

    if len(bins) >= min_bins:
        return min_bins

    for i in range(len(bins)):
        if objects[position] + bins[i] <= MAX_BIN_SIZE:
            bins[i] += objects[position]
            min_bins = packaging_backtracking_aux(position+1, objects, bins, min_bins)
            bins[i] -= objects[position]
        
    bins.append(objects[position])
    min_bins = packaging_backtracking_aux(position+1, objects, bins, min_bins)
    bins.pop()
    
    return min_bins
