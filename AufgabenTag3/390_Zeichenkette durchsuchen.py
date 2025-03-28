
# Zeichenkette durchsuchen

# Schreibe eine Funktion find_all(), die eine Zeichenkette nach allen
# Vorkommen einer anderen Zeichenkette durchsucht
# und die Startpositionen als Liste zurückgibt.
# Wenn es kein Vorkommen gibt, soll die Liste leer sein.
# Beispiel:
# print(find_all('abcefgabcxyzabcd', 'abc'))  # [0, 6, 12]

def find_all(text:str,subtext:str) -> list[int]:
    indices=[]
    for i in range(len(text)):
        spliced_text=text[i:]
        if spliced_text.startswith(subtext):
            indices.append(i)
    return indices
    #return i

print(find_all('abcefgabcxyzabcd', 'abc'))
print(find_all('abcefgabcxyzabcd', 'c'))
print(find_all('abcefgabcxyzabcd', 'm'))