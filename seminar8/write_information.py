def write_information(data, name):
    with open(name, 'a+') as file:
        file.write(";".join(map(str, data)))
        file.write(f"\n")


def count_inf(name):
    with open(name, 'r') as file:
        data = file.read()
    return data.count('\n')