
# Fakultät

"""
Schreibe ein Skript, dass ermittelt,
welche Zahl möglichst groß ist
ohne dass ihre Fakultät über 1.000.000.000 ist.

Hinweis:
Fakultät von 5 (Kurzschreibweise: 5!):
1 * 2 * 3 * 4 * 5 = 120
"""
n=int(input("Geben Sie eine ganze Zahl ein: "))
ergebnis=1
teile=[]
for i in range(1,n+1):
    ergebnis *=i
    teile.append(str(i))

    if ergebnis>1000000000:
        print("größer als 1000000000")
        break

ausdruck = "*".join(teile)  #1*#2*#3*#4*6
print(f"{ausdruck} = {ergebnis}")
print(f"{i}!= {ergebnis}")
    #print(f"{i}*", end="")





