from packets_dynamic import extract_packets_dynamic as ext_dyn
from packets_greedy import extract_packets_greedy as ext_greedy
import random
import matplotlib.pyplot as plt

def create_data(requested_products, min_requested_amount, max_requested_amount, min_box, max_box, seed):
    random.seed(seed)
    requested = {}
    packets = {}

    for product in requested_products:
        value = random.randint(min_requested_amount, max_requested_amount)
        requested[product] = value

        packets[product] = []
        total_elements = 0
        elements_limit = value * 2

        while total_elements < elements_limit:
            random_val = random.randint(min_box, max_box)
            packets[product].append(random_val)
            total_elements += random_val
    
    return requested, packets

def increasing_products_test(products):
    amount_of_products = []
    diferences = []

    for i in range(1, len(products) + 1):
        print(i)
        requested_products, packets = create_data(products[:i], 10, 500, 0, 50, 15)
        extracted_g = ext_greedy(packets, requested_products)
        extracted_d = ext_dyn(packets, requested_products)

        amount_given_g = 0
        amount_given_d = 0

        for extracted_boxes_g in extracted_g.values():
            amount_given_g += sum(extracted_boxes_g)
        
        for extracted_boxes_d in extracted_d.values():
            amount_given_d += sum(extracted_boxes_d)

        diferences.append(amount_given_g - amount_given_d)
        amount_of_products.append(i)
    
    plt.title("Diferencia de productos entregados entre el algoritmo \ncon programación dinámica y el algoritmo greedy")
    plt.xlabel("Cantidad de tipos de productos")
    plt.ylabel("Diferencia de productos entregados")
    plt.plot(amount_of_products,diferences)
    plt.show()

def increasing_products_test_same_data(products):
    amount_of_products = [0]
    diferences = [0]

    requested_products, packets = create_data(products, 10, 500, 0, 50, 15)

    for i in range(1, len(products) + 1):
        print(i)
        visible_requests = products[:i]
        current_requests = {request: requested_products[request] for request in visible_requests}
        extracted_g = ext_greedy(packets, current_requests)
        extracted_d = ext_dyn(packets, current_requests)

        amount_given_g = 0
        amount_given_d = 0

        for extracted_boxes_g in extracted_g.values():
            amount_given_g += sum(extracted_boxes_g)
        
        for extracted_boxes_d in extracted_d.values():
            amount_given_d += sum(extracted_boxes_d)

        diferences.append(amount_given_g - amount_given_d)
        amount_of_products.append(i)
    
    plt.title("Diferencia de productos entregados entre el algoritmo \ncon programación dinámica y el algoritmo greedy")
    plt.xlabel("Cantidad de tipos de productos")
    plt.ylabel("Diferencia de productos entregados")
    plt.plot(amount_of_products,diferences)
    plt.show()

def main():
    products = [str(i) for i in range(1, 200)]
    increasing_products_test(products)
    increasing_products_test_same_data(products)
main()