"""

    Python ist ein interpretier Sprache, das  heißt dass ein Programm nicht vorab vollständig
    in Maschinensprache übersetzt wird, sondern zur Laufzeit (beim Ausführen) Schritt für Schritt
    von einem sogenannten Interpreter „übersetzt“ und ausgeführt wird.

    Über den Parameter 'sep' Seperator kann das Trennsymbol für die einzelnen positional Argumente gesetz werden.
"""

print("hallo", "welt", sep="-")
print("merhaba", end="!")
print()
# Input Eingabe

#eingabe= input("Bitte gibt einen Wert an: ")
#print("Die Eingabe war: ", eingabe)

#Variablen

name= "Thomas"
print(name, type(name))
alter=30
print(alter, type(alter))

#DatenTypen
"""
-integer
-float
-complex 
-Boolean
==>UND die zusammengesetzten Datentypen:
-String/zeichenkette: "thomas" oder 'thomas'
-List/Liste: ["Thomas", 30]
-Set/Satz: Set(30, "Thomas", 30) Werte im Set sind einmalig
-Tupel: wie list nur nicht veränderbar(immutable)
-Dictionary:{"name":"Thomas", "alter":30 } Key-Value_Paare, Zugriff über Keys anstelle von Indices
"""

mein_dict={
    "name":"Sait",
    "alter":35,
    "Stadt":"Heidelberg"
}
print(mein_dict)
print(mein_dict["name"])
mein_dict["name"]="Thomas"
print(mein_dict)
mein_dict["Beruf"]="Entwickler"
print(mein_dict)
"""
#🔹 4. .split() ile Ayırma ve Dictionary Oluşturma
eintrag="name:Sait"
key_value=eintrag.split(":")

mein_dict={}
mein_dict[key_value[0]]=key_value[1]
print(mein_dict)

"""
#DatenTypen sind Klassen
#Wie Java, alles in Objekt in Klassen
x=458712596
print(x.bit_length())
a="Ahmet"
print(a.upper())

###########################################################
##Binary und hexadezimal
print(0b101)
print(0x1f)
print(1e3)
print(1e8)
print(1e-3)
print(float("inf")- float("inf"))  ##nan undefiniert, inf heißt infinitive also unendlich

name= "Aliokulakos"
print(name[0:3])   ##bir stringe bir parca yer almak istiyorsak kullaniriz, baslangic indexi ve son indexi yapariz.

var="Hallo Welt!"
print(var[0:-1:2]) ##3. deger atlama durumunu gösterir ='dan basla 2 atlayarak git.yani birinciyi atla 2, yaz
print(var[1:-1:3]) #eoe 11111.den basla 1 , 2 3. yü yaz

#Wenn du eine Zeichenkette in umgekehrter Reihenfolge (rückwärts) haben willst, kannst du in
# #Python einfach Splicing mit negativem Schrittwert benutzen.

print(var[::-1]) #!tleW olleH
print(var[::-2])  #!lWolH
print(var[5:0:-1]) #5 bis 0 ausschließlich
print(var[0:5:1]) #0 bis 5 ausschließlich



