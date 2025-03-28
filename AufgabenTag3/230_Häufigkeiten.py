
# Häufigkeiten

# Schreibe eine Funktion hauefigkeiten(),
# die zu jedem Zeichen eines übergebenen Strings die Häufigkeit ermittelt,
# mit der dieses Zeichen im String vorkommt.
# Zurückgegeben wird ein Dictionary,
# in dem jedem Zeichen dessen Vorkommenshäufigkeit zugeordnet wird.

# Beispiel:
# print(haeufigkeiten('Erdbeere'))
# {'E': 1, 'r': 2, 'd': 1, 'b': 1, 'e': 3}


def hauefigkeiten(text):
    buchstaben={}
    for i in text:
        if i in buchstaben.keys():
            buchstaben[i] +=1  # wert 1 erhöhen
        else:
            buchstaben[i]=1    #key starten
    return buchstaben

print(hauefigkeiten("Erdbeere"))
print(hauefigkeiten("Heidelbeere"))
print(hauefigkeiten("Himbeere"))


