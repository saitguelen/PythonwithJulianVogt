###############   TUPLE     ##############
"""
🧠 Was ist ein Tupel?
Ein Tupel ist eine unveränderbare (→ immutable) Liste.

Man kann sich ein Tupel als eine Art feste Liste vorstellen – du kannst es lesen, aber nicht verändern
 (nicht hinzufügen, löschen oder ändern)

Türkisch zusammengefasst:
Tuple, Python'da değiştirilemeyen bir liste türüdür.
Parantez içinde yazılır: (1, 2, 3)

Eleman ekleyemezsin

Eleman silemezsin

Ama okuyabilirsin ✅

⚠️ Wichtiger Hinweis:
Ein Tupel mit nur einem Element braucht ein Komma:

eins = (42,)  # Das ist ein Tupel
nicht_ein_tupel = (42)  # Das ist nur die Zahl 42 in Klammern

🔒 Warum Tupel verwenden?
Wenn sich die Daten nicht ändern sollen → z. B. Wochentage

Tupel sind schneller als Listen

Tupel können in Dictionaries als Schlüssel (key) verwendet werden (Listen nicht!)

🔹 Tupel erkennt man an den runden Klammern: ()
🔹 Listen dagegen verwenden eckige Klammern: []

"""

#Örnek 1: Tuple tanımla ve elemanlarına eriş

stadt = ("Berlin", "Hamburg", "München")

print(stadt[0])  # Ausgabe: Berlin
print(stadt[1])  # Ausgabe: Hamburg


#Örnek 2: Tuple ile döngü

farben = ("rot", "grün", "blau")

for farbe in farben:
    print(farbe)

# Örnek 3: Tuple uzunluğu

zahlen = (10, 20, 30, 40)
print("Anzahl der Elemente:", len(zahlen))  # Ausgabe: 4


#Örnek 4: Tuple içinde Tuple

punkte = ((1, 2), (3, 4), (5, 6))

for p in punkte:
    print("X:", p[0], "Y:", p[1])

#Örnek 5: Tuple’ı değiştirmeye çalış (HATA!)

tiere = ("Hund", "Katze", "Maus")
# tiere[0] = "Fuchs"  ❌ HATA verir çünkü Tuple değiştirilemez!

## Ama list cevirerek eleman atama yapabiliriz.

liste= list(tiere)
print(liste)
liste[0]= "Fuchs"
print(liste)
print(tiere)
tiere=(liste,)
print(tiere)

"""
📊 Tuple vs. Liste Karşılaştırma:
Özellik	             Liste (list)	            Tuple (tuple)
Yazım	             [1, 2, 3]	                 (1, 2, 3)
Değiştirilebilir mi?	✅ Evet	                 ❌ Hayır
Hızlı mı?	           Normal	                 Daha hızlı
Kullanım amacı	       Değişen veri	             Sabit, değişmeyen veri
Sözlükte key olabilir mi?	❌ Hayır	          ✅ Evet


🎯 Hangi durumlarda Tuple kullanılır?


✅ Eğer bilgiler sabit kalacaksa (örneğin: koordinatlar, sabit listeler)
✅ Eğer performans gerekiyorsa
✅ Eğer verileri korumak istiyorsan

🗣 Türkçe Özet:
Tuple → () içinde, sabit veriler için idealdir

Liste → [] içinde, sık değişen veriler için kullanılır
"""

#######

"""
🎯 Görev:
Kullanıcıdan ad, yaş ve şehir bilgisi alınacak

Tuple içine kaydedilecek

Ekrana düzenli şekilde yazdırılacak
"""

# Kullanıcıdan veri al
name = input("Wie heißt du? ")
alter = input("Wie alt bist du? ")
stadt = input("Wo wohnst du? ")

# Tuple oluştur
person = (name, alter, stadt)

# Tuple içeriğini yazdır
print("\n--- Deine Daten ---")
print("Name:", person[0])
print("Alter:", person[1])
print("Stadt:", person[2])


""" 
🧠 Neden Tuple kullandık?
Çünkü:

Bu bilgiler değiştirilmeyecek

Sabit ve birlikte anlamlı: kişi bilgisi

Sade ve güvenli yapı

🗣 Türkçe Özet:
Kullanıcıdan alınan bilgiler person adında bir tuple içine kaydedildi.

Tuple’dan index ile bilgi alındı: person[0], person[1], person[2]

Tuple değiştirilmez, sadece okunur.
"""