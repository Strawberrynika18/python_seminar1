from input_information import input_information
from write_information import write_information

def push_inf():
    dct = input_information()

    write_information([dct.get("id"), dct.get("surname"), dct.get("name"), dct.get("class"), dct.get("status")], "name.txt")

    write_information([dct["id"], dct["city"], dct["street"], dct["house"], dct["apartament"], dct["other"]], "adress.txt")

    write_information([dct["id"], dct["row"], dct["col"]], "class.txt")