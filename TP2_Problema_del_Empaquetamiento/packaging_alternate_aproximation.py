def first_fit(objects, bin_capacity):
    bins = []
    
    for item in objects:
        print(bins)
        for i in range(len(bins)):
            if bins[i] + item <= bin_capacity:
                bins[i] += item
                break
        else:
            bins.append(item)
    print(bins)
    print(len(bins))
    return len(bins)