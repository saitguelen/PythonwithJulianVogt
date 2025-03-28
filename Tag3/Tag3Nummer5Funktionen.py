"""
🧠 Was ist eine Funktion? (Fonksiyon nedir?)
Eine Funktion ist ein benannter Codeblock, den man mehrfach aufrufen kann, um eine bestimmte Aufgabe auszuführen.

👉 Fonksiyon = "görev yapan küçük bir program parçası"

✅ Warum benutzt man Funktionen?
Vorteil                         Türkçe Açıklama
Wiederverwendbarkeit	        Aynı kodu tekrar tekrar yazmadan kullanmak
Übersichtlichkeit	            Kodu küçük parçalara bölmek
Wartbarkeit	                    Hataları düzeltmek ve güncellemek kolay
Modulare Programmierung	        Her işlem için ayrı fonksiyon kullanmak

🔧 Aufbau einer Funktion (Fonksiyon Yapısı):
python
Kopieren
Bearbeiten
def begrüßung():
    print("Hallo! Willkommen!")
def: fonksiyon tanımlamak için kullanılır

begrüßung: fonksiyonun adı

(): parametre yeri (boş olabilir)

:: fonksiyon bloğunun başladığını gösterir

İçerideki kod girintili (indent) olmalı


"""

#🧪 Beispiel mit Parameter (Parametreli fonksiyon):
def hallo_name(name):
    print("Hallo,", name)

hallo_name("Sait")  # Ausgabe: Hallo, Sait


#🔁 Funktion mit Rückgabewert (return)

def quadrat(x):
    return x * x

ergebnis = quadrat(5)
print(ergebnis)  # Ausgabe: 25

#Parameter -------->An die Funktion gesendete Werte, 5 ist eine parameter oder x eine parameter
#return------------>Ergebnisse aus der Funktion

def ausgabe(erste, zweite):
    print(erste)
    print(zweite)

ausgabe("Hallo ", "Welt")

def dreifachsumme(zahl_1,zahl_2,zahl_3):
    return zahl_2+zahl_1+zahl_3


print(dreifachsumme(1,2,3))

list=[1,2,3]
list2=[4,5,6,7]
def add(zahl1,zahl2):
    return zahl1+zahl2

print(add(list,list2))

print(add("Hallo", " Welt"))


