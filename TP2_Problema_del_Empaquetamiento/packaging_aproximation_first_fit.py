def first_fit(objects):
    objects.sort(reverse=True) 
    bins = []
    for item in objects:
        for i in range(len(bins)):
            if bins[i] + item <= 1:
                bins[i] += item
                break
        else:
            bins.append(item)
    return len(bins)