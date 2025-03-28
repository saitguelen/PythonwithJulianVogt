
# Zahlenreihen

# 1. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5

i=1
while i<=5:
    print(i, end=" ")
    i +=1
print()

# 2. Schreibe eine Schleife, die Folgendes ausgibt:
# 100 90 80 70 60 50 40 30 20 10

for i in range(100,1,-1):
    if i%10==0:
        print(i, end=" ")
print()




# 3. Schreibe eine Schleife, die Folgendes ausgibt:
# 2000 3000 4000 5000 6000
i=2
while i<=6:
    zahlen=i*(10**3)
    print(zahlen, end=" ")
    i +=1

print()


# 4. Schreibe eine Schleife, die Folgendes ausgibt:
# 2.0 1.5 1.0 0.5 0.0 -0.5 -1.0

k= 2.0
print(type(k))
while k>=-1.0:
    print(k, end=" ")
    k -= 0.5

print()


# 5. Schreibe eine Schleife, die Folgendes ausgibt:
# 13 17 21 25 29
i=9
k=1
while k<=5:
    Schleife= i+4*k
    print(Schleife, end=" ")
    k +=1

print()

for i in range(13, 30, 4):  # 13'ten başla, 29'a kadar, 4'er art
    print(i, end=" ")
print()



# 6. Schreibe eine Schleife, die Folgendes ausgibt:
# 1.0 2.2 3.4 4.6 5.8 7.0 8.2 9.4

k=1.0
while k<=9.4:
    print(round(k,1), end=" ")
    k +=1.2

print()
print()




# 7. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5 6 8 9 10
for i in range(1,11):
    if i==7:
        continue
    print(i, end=" ")
print()



# 8. Schreibe eine Schleife, die Folgendes ausgibt:
# 13 17 21 29 33 37 45
for i in range(13,46,4):
    if i in [25,41]:
        continue
    print(i, end=" ")

print()

# 9. Schreibe eine Schleife, die Folgendes ausgibt:
# Z5 Z7 Z9 Z11 Z13

for i in range(5,14,2):
    print(f"Z{i}", end=" ")

print()

# 10. Schreibe eine Schleife, die Folgendes ausgibt:
# a2b3 a12b13 a22b23

for i in range(0,3):
    if i==0:
        i=""
    print(f"a{i}2b{i}3", end=" ")

print()
# 11. Schreibe eine Schleife,
# die alle Zahlen von 1 bis 20 addiert
# und danach das Endergebnis ausgibt.
summe=0
for i in range(1,21):
    summe +=i

print("Das Ergebnis Summe von 1 bis 20: ",summe)
print()
# 12. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5 4 3 2 1
print(*list(range(1, 6)) + list(range(4, 0, -1)))

