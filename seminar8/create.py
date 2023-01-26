from export_information import export_information

def create():
    if not (len(export_information()) > 0):
        
        with open("name.txt", 'a+') as file:
            file.write("id;surname;name;class;status\n")

        with open("adress.txt", 'a+') as file:
            file.write("id;city;street;home;float;other\n")

        with open("class.txt", 'a+') as file:
            file.write("id;row;col\n")