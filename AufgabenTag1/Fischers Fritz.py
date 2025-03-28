
# Fischers Fritze

# Es steht folgender String zur Verfügung:
satz = "Fischers Fritz fischt frische Fische"
print(len(satz)) #36

# Gib durch String-Slicing des Strings 'satz' die folgenden Strings aus
# 1. ihsrzihf
print(satz[1:25:3]) #oder
print(satz[1:-13:3])


# 2. sifhrhi

print(satz[1:25:3][::-1]) #oder

# 3. sche (mit möglichst wenig Zeichen)
print(satz[2:6])



# 4. eci hsr hsfziFseci
print(satz[1:36:2][::-1]) #oder
print(satz[::-2])



# 5. ii i
print(satz[1::10])

