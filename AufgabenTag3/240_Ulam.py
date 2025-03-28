
# Ulam

# Berühmt ist die (3a + 1)-Folge des amerikanischen Mathematikers Ulam.
# Sie ist durch folgenden Algorithmus definiert:
#
# 1. Beginne mit einem Startwert a.
# 2. Wenn a == 1 ist, stoppe.
# 3. Ist a gerade, setze a = a/2,
#    sonst setze a = 3*a + 1 und fahre mit 2. fort.
#
# Bis heute weiß man nicht,
# ob die Ulam-Folge bei jedem Startwert a zum stoppen kommt.
#
# Entwickle zu dem Algorithmus eine Funktion
# und teste sie mit verschiedensten Startwerten für a.



def ulam(a):
    """
    Berechnet die Ulam-(Collatz-)Folge für eine gegebene Startzahl.

    Parameter:
    a (int): Startwert der Folge (muss positiv sein)

    Rückgabe:
    list: Liste der Zahlen in der Ulam-Folge, endend mit 1
    """
    folge = [a]
    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
        folge.append(a)
    return folge

print(ulam(45))
print(ulam(25))
print(ulam(120))
help(ulam)





