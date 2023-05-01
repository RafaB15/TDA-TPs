def extract_amounts(amounts, restriction):

    extracted = []

    i = 0
    while restriction > 0:
        extracted.append(amounts[i])
        restriction -= amounts[i]
        i+=1
    
    return extracted

def extract_packets_greedy(packets, requests):
    retained_packets = {}

    for request in requests:
        packets[request].sort()
        retained_packets[request] = extract_amounts(packets[request], requests[request])

    return retained_packets
