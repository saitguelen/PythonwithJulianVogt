
# Liste umkehren

# Schreibe eine Funktion, die die Reihenfolge einer Liste umkehrt.
# Verzichte aber auf die Benutzung der Listen-Methode reverse().

"""
liste = ['a', 'b', 'c', 'd']
print(kehre_liste_um(liste))  # ['d', 'c', 'b', 'a']
"""
def kehre_liste_um(liste):
    """
        Gibt eine umgekehrte Version der übergebenen Liste zurück.

        Parameter:
        liste (list): Eine Liste beliebiger Elemente

        Rückgabe:
        list: Die umgekehrte Liste
        """
    umgekehrt=[]
    for i in range(len(liste)-1,-1,-1):  #listenin sonundan baslar sifirinci indexe gelir sifir yazarsak sifir ausschlißlich oldugu icin almaz dol -1 yazariz
        umgekehrt.append(liste[i])
    return umgekehrt

liste=['a','b','c','d','e']
print(kehre_liste_um(liste))
liste2=['sait', 'nesibe','mucteba', 'yakub']
print(kehre_liste_um(liste2))
help(kehre_liste_um)

"""
def kehre_liste_um(liste):
    return liste[::-1]

"""