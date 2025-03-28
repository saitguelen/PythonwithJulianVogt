# Testen Sie die folgenden Stringmethoden. 
# Machen Sie sich eine kurze Notiz, wofür die Stringmethode verwendet wird.

var= "Python ist toll!, wirklich toll"
print(var)


# replace
# Ersetzt die im ersten Parameter angegebene Zeichenfolge durch die im zweiten Parameter angegebene Zeichenfolge.

var=var.replace("o", "O") ##PythOn ist tOll!
print(var)

# name = "Thomas"
# name = name.replace("o", "0")
# print(name)



var= "Python ist toll!, wirklich toll"
# find/rfind und index/rindex
################   find
#Der erste vom Anfang (links) findet den Ort
print(var.find("i")) #7 7. indexde
print(var.index("o"))  #4
print(var.find("a")) #-1 es gibt keine 'a'
#print(var.index("a"))  #error
print(var.find("wirklich"))  #18
#################### rfind
##Wenn der Text nicht gefunden wird, gibt .rfind() -1 zurück.
##find() sucht von links, rfind() von rechts.

#Findet die letzte Stelle vom Ende her
print(var.rfind("wie")) #-1
print(var.rfind("ist"))


############ count

##zählt, wie oft eine bestimmte Teilzeichenkette übergeben wird
print(var.count("toll!")) #1
print(var.count("toll")) #2 weil es keine Ausrufzeichen gibt
print(var.count("l")) #5  es gibt 5 mal 'l' steht

########### split

#zerlegt eine Zeichenkette in Teile nach einem bestimmten Trennzeichen
#und gibt diese Teile als Liste zurück.

var1=var.split(",")
print(var1)   ############['Python ist toll!', ' wirklich toll']
var2= var.split(" ")
print(var2) #################['Python', 'ist', 'toll!,', 'wirklich', 'toll']



# isnumeric(Umfassender)Römische Ziffern, Prüft, ob ein numerischer Wert vorhanden ist, isdigit(begrenzt)Prüfungen für Ziffern und weitere is... Methoden
print(var.isdigit())  ##False es gibt keine Zahl
num="123654"
print(num.isdigit())  #True, das heißt variable hat Zahlen
print(num.isnumeric()) #True
print(var.isnumeric())  #False


####### join
## verkettet Zeichenketten in einer Liste
#und erzeugt eine einzige Zeichenkette.

obst= ["Apfel", "Banane","Birne", "Orange"]
satz=", ".join(obst)
print(satz)   ##Apfel Banane Birne Orange


########### startswith

#Sie wollen überprüfen, ob es am Anfang war character

print(var.startswith("Python"))  ##True
print(var.startswith("Java"))   #False

# Knobelaufgabe: maketrans und translate
"""
🔤 maketrans() ve translate() nedir?
🔹 str.maketrans():
Bir çeviri tablosu (translation table) oluşturur: hangi harf neye dönüşecek?

🔹 str.translate():
Bir string’de, maketrans() ile oluşturulan çeviri tablosuna göre harfleri değiştirir.


"""

text = "Hallo Welt"

# 'a' → '@', 'e' → '3', 'l' → '1'
tabelle = str.maketrans("ael", "@31")

neuer_text = text.translate(tabelle)
print(neuer_text)


# Ausgabe: H@111 W3t

tabelle = str.maketrans("", "", "aeiou")  # Sesli harfleri sil

text = "Programmieren"
print(text.translate(tabelle))
# Ausgabe: Prgrmmrn



