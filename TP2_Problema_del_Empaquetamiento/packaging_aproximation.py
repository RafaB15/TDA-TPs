MAX_BIN_SIZE = 1

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