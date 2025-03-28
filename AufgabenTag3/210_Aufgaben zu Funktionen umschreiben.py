
# Aufgaben zu Funktionen umschreiben

# Wähle drei deiner bisher gemachten Aufgaben
# und schreibe sie jeweils so um,
# dass Funktionen benutzt werden.
# Im Ideafall wird innerhalb der Funktion nichts mehr geprinted
# und der errechnete Wert wird zurück gegeben.
"""
for i in range(1,10):
    QuadratZahlen= i*i
    print(QuadratZahlen, end=" ")

zahl=0
while zahl**2<100:
    print(zahl, zahl**2)
    zahl +=1

"""

def quadratzahl(zahl_1):
    quadrat=zahl_1*zahl_1
    return f"Quadrat von der {zahl_1} ist: {quadrat}"


print(quadratzahl(9))
print(quadratzahl(36))
print(quadratzahl(12))


"""
count=0
for j in range(1,100):
    if j%3==0 or j%7==0:
        print(j,end=" ")
        count +=1

print()
print("Es gibt durch 3 oder durch 7 teilbar Zahlen: ", count)

"""
def teilbar_3_oder_7(untergrenze,obergrenze):
    count=0
    for j in range(untergrenze,obergrenze):
        if j%3==0 or j%7==0:
            print(j, end=" ")
            count +=1

    print()
    print(f"Es gibt durch 3 oder durch 7 teilbare Zahlen: {count}")

teilbar_3_oder_7(1,45)
teilbar_3_oder_7(36,456)
teilbar_3_oder_7(1,100)