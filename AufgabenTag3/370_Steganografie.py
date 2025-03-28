
# Steganografie

# Steganografie ist die Technik, eine geheime Information in einem Dokument so zu verstecken,
# dass sie nur von einer eingeweihten Person gefunden werden kann.
# Schreibe eine Funktion mit zwei Argumenten s und n,
# die einen Klartext s auf folgende Weise durch Steganografie unleserlich macht:

# - Der String s wird in Großbuchstaben umgewandelt.
# - Hinter jedes Zeichen werden n zufällige Großbuchstaben eingefügt.
# - Das Argument n ist optional (Default=1).

# Beispielaufrufe:
# print(verstecke('Um acht an der Uhr'))
# AUSGABE z.B.: UFMF LACCRHXTF GAXNJ VDCEYRA IUGHBRW
# print(verstecke('Um acht an der Uhr', 2))
# AUSGABE z.B.: UALMVD SPAHNCWDHAHTPH PJAMUNSY REDKNEQBRIB PIUBTHZBRWN

def steganografie(klartext:str,n:int=1) :
    """
    Wandelt den klartext in Großbuchstaben um und fügt nach jedem Buchstaben n zufällig generierte Buchstaben ein.
    :param klartext: Der Eingabetext, der verschlüsselt werden soll
    :param n: Anzahl der zufälligen Großbuchstaben, die nach jedem Buchstaben hinzugefügt werden soll
    :return:
    """
    chiffretext_buchstaben=[]
    for klartext_buchstabe in klartext:
        chiffretext_buchstaben.append(klartext_buchstabe.upper())
        for _ in range(n):
            anz_großbuchstaben=len(string.ascii_uppercase)
            zufalls_buchstabe=string.ascii_uppercase[random.randint(0, anz_großbuchstaben-1)]
            chiffretext_buchstaben.append(zufalls_buchstabe)

    chiffretext= "".join(chiffretext_buchstaben)
    return chiffretext
print(steganografie('Um acht an der Uhr',2))


import random
import string

def verstecke(s, n=1):
    s = s.upper()
    geheim = ""

    for buchstabe in s:
        geheim += buchstabe
        zufall = ''.join(random.choices(string.ascii_uppercase, k=n))
        geheim += zufall

    return geheim


print(verstecke("Um acht an der Uhr"))       # varsayılan n=1
print(verstecke("Um acht an der Uhr", 2))    # n=2
"""
🧠 Açıklama:
string.ascii_uppercase → A’dan Z’ye büyük harfler

random.choices(..., k=n) → n tane rastgele büyük harf seçer

Her karakterin arkasına bu harfleri ekliyoruz

🗣 Türkçe Özet:
Harfleri büyüt

Her harften sonra n adet rastgele büyük harf ekle

Sonuç: sadece senin çözebileceğin gizli bir mesaj
"""

def entschluesseln(text, n=1):
    entschluesselt = ""
    i = 0
    while i < len(text):
        entschluesselt += text[i]    # her (n+1)'lik bloğun ilk harfi alınır
        i += n + 1                    # bir harf + n rastgele harf atlanır
    return entschluesselt



geheim = verstecke("Um acht an der Uhr", 2)
print("Verschlüsselt:", geheim)

klartext = entschluesseln(geheim, 2)
print("Entschlüsselt:", klartext)
