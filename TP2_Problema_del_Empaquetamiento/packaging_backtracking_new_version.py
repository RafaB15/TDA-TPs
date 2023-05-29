from packaging_aproximation import packaging_aproximation

MAX_BIN_SIZE = 1

def packaging_problem_backtracking(objects):
    bins = []
    min_bins = packaging_aproximation(objects)
    objects_with_state = [[object, 1] for object in objects]
    return packaging_problem_backtracking_aux(objects_with_state, bins, min_bins)

def packaging_problem_backtracking_aux(objects_with_state, bins, min_bins):
    print(objects_with_state)
    if len(bins) >= min_bins:
        return min_bins
    
    if sum(state[1] for state in objects_with_state) == 0:
        print(bins)
        print(objects)
        if len(bins) < min_bins:
            min_bins = len(bins)
        return min_bins

    for index_o, object in enumerate(objects_with_state):
        if object[1] == 1:
            for index_b, bin in enumerate(bins):
                if object[0] + bin <= MAX_BIN_SIZE:
                    bins[index_b] += object[0]
                    objects_with_state[index_o][1] = 0
                    min_bins = packaging_problem_backtracking_aux(objects_with_state, bins, min_bins)
                    objects_with_state[index_o][1] = 1
                    bins[index_b] -= object[0]
            bins.append(object[0])
            objects_with_state[index_o][1] = 0
            min_bins = packaging_problem_backtracking_aux(objects_with_state, bins, min_bins)
            objects_with_state[index_o][1] = 1
            bins.pop()
    return min_bins

objects = [0.4, 0.6, 0.2, 0.6, 0.1, 0.9, 0.12, 0.87]
print(packaging_problem_backtracking(objects))

