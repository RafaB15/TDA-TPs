MAX_BIN_SIZE = 1
INFINITY = 10000000000000000000000000000
ERROR = -1

def packaging_greedy(objects):
    objects.sort(reverse=True) 
    
    bins = [] 

    for object in objects:
        best_bin_index = ERROR
        min_remaining_capacity = INFINITY

        for i in range(len(bins)):
            if object <=  MAX_BIN_SIZE - sum(bins[i]) < min_remaining_capacity:
                best_bin_index = i
                min_remaining_capacity = MAX_BIN_SIZE - sum(bins[i])

        if best_bin_index != ERROR:
            bins[best_bin_index].append(object)
        else:
            bins.append([object])

    return bins