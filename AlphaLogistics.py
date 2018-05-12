#!/usr/bin/env python3

from pick import pick

from route_info import get_route_info
from incoterms import get_incoterm
from file_opener import open_file
from qrcoder import qrcoder


opcije = {
    'Informacije o ruti': get_route_info,
    'Incoterms': get_incoterm
}
lista = ['Informacije o ruti', 'Incoterms', 'IZLAZ']
print("ALPHA LOGISTICS \n ")
doc_name = input("Naziv dokumenta: ")
file = open(doc_name+".txt", "w")


stop = 'n'
while stop!='y':
    opcija = pick(lista)
    print(opcija[0])
    if opcija[0] != 'IZLAZ':
        file.write(opcija[0] +"\n")
        info = [opcije[opcija[0]]()]
        print(info[0])
        for i in info[0]:
            file.write(i + "\n")
        file.write("\n")
    else:
        break


file.close()

tekst = open(doc_name+".txt", 'r')
qrcoder(doc_name, tekst.read())


open_file("./"+doc_name+".txt")
open_file("./"+doc_name+".png")
