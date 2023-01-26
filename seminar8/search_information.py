from export_information import export_information 
from print_information  import print_information

def search_information(word, data):
    if len(data) > 0:
        lst = []
        for item in data:
            if word in item:
                lst.append(item)
        if lst == []:
            return None
        else:
            return lst
    else:
        return None