
EXIT = "X"

def load_restrictions():
    restrictions = {}
    restriction_name = input(f"Ingrese el nombre del paquete para la restricción o [{EXIT}] para terminar: ")

    while(restriction_name.upper() != EXIT):
            value = input(f"Ingrese la cantidad a extraer para {restriction_name}: ")
            if(value.isnumeric()):
                restrictions[restriction_name] = int(value)

            restriction_name = input(f"Para ingresar una nueva resricción ingrese su nombre o [{EXIT}] para terminar: ")

    return restrictions

def load_packets():
    packets = {}

    packet_name = input(f"Ingrese el nombre del paquete o [{EXIT}] para terminar: ")
    while(packet_name.upper() != EXIT):
        i = 1
        value = input(f"Ingrese la cantidad del paquete n°{i} para {packet_name}\nPara ingresar un nuevo producto ingrese su nombre o [{EXIT}] para terminar: ")
        while(value.isnumeric()):
            value = int(value)
            try:
                packets[packet_name].append(value)
            except KeyError:
                packets[packet_name] = [value]
            i+=1
            value = input(f"Ingrese la cantidad del paquete n°{i} para {packet_name}\nPara ingresar un nuevo producto ingrese su nombre o [{EXIT}] para terminar: ")

        packet_name = value

    return packets