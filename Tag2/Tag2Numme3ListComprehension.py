"""
📚 Was ist eine List Comprehension?
List Comprehension ist eine kompakte, elegante Schreibweise, um Listen zu erstellen –
besonders, wenn sie auf Basis einer Schleife entstehen sollen.

👉 Sie ersetzt viele Zeilen for-Schleife durch eine Zeile Code.

[ Ausdruck for Element in Iterable if Bedingung ]


🧠 Vorteile von List Comprehension:
✅ Kürzer
✅ Lesbarer
✅ Oft schneller
✅ Eleganter Code


Türkçe özet:
List Comprehension, Python’da listeleri kısa yoldan oluşturmanın yoludur.

🧠 List Comprehension Nedir?
List Comprehension, bir listeyi oluşturmak için kullanılan kısa ve etkili bir yazım şeklidir.
Normalde birkaç satırda yazacağımız for döngüsünü, tek satırda yazmamıza olanak tanır.

ChatGPT:
Elbette! 🐍
Şimdi sana Python’daki List Comprehension konusunu detaylı ve anlaşılır bir şekilde Türkçe olarak adım adım anlatayım.

🧠 List Comprehension Nedir?
List Comprehension, bir listeyi oluşturmak için kullanılan kısa ve etkili bir yazım şeklidir.
Normalde birkaç satırda yazacağımız for döngüsünü, tek satırda yazmamıza olanak tanır.

✅ Temel Yazım Şekli (Söz Dizimi)
python
Kopieren
Bearbeiten
[ ifaden for öğe in liste ]
ifaden: Listeye eklenecek eleman (dönüştürülmüş hal olabilir)

for öğe in liste: hangi öğeler üzerinde işlem yapılacağını belirler

🧪 Örnek 1 – 0'dan 4’e kadar sayıları listele
python
Kopieren
Bearbeiten
liste = [x for x in range(5)]
print(liste)  # Çıktı: [0, 1, 2, 3, 4]
Aynısı uzun yolla şöyle olurdu:

python
Kopieren
Bearbeiten
liste = []
for x in range(5):
    liste.append(x)
🧪 Örnek 2 – Her sayının karesini alma
python
Kopieren
Bearbeiten
karesel = [x**2 for x in range(1, 6)]
print(karesel)  # Çıktı: [1, 4, 9, 16, 25]
🧪 Örnek 3 – Sadece çift sayıları listele
python
Kopieren
Bearbeiten
ciftler = [x for x in range(10) if x % 2 == 0]
print(ciftler)  # Çıktı: [0, 2, 4, 6, 8]
🧪 Örnek 4 – if-else ile koşullu içerik
python
Kopieren
Bearbeiten
durumlar = ["çift" if x % 2 == 0 else "tek" for x in range(5)]
print(durumlar)  # Çıktı: ['çift', 'tek', 'çift', 'tek', 'çift']
🧪 Örnek 5 – Metinleri dönüştürme
python
Kopieren
Bearbeiten
kelimeler = ["elma", "armut", "muz"]
buyukler = [k.upper() for k in kelimeler]
print(buyukler)  # Çıktı: ['ELMA', 'ARMUT', 'MUZ']
🧪 Örnek 6 – Sayılardan negatif olanları filtrele
python
Kopieren
Bearbeiten
sayilar = [4, -1, 0, -6, 3]
negatifler = [s for s in sayilar if s < 0]
print(negatifler)  # Çıktı: [-1, -6]
🎯 Avantajları:
✅ Daha kısa ve okunabilir kod

✅ Döngü ve append() yerine tek satırda liste üretimi

✅ Filtreleme (if) ve dönüşüm (if-else) desteği

📝 Kural:
Eğer listen üzerinde işlem yapıyorsan ve sonucu yeni bir listeye koymak istiyorsan,
List Comprehension neredeyse her zaman en güzel yoldur.

🗣️ Türkçe Özetle:
Ne yapmak istiyorsun?	     Nasıl yapılır?
Listeyi hızlı oluştur	     [x for x in range(5)]
Filtrele	                 [x for x in liste if x > 0]
Koşullu ifade (if-else)	     [x if x > 0 else 0 for x in liste]

[x for x in range(10) if x % 2 == 0]
➜ Bu satır, 0’dan 9’a kadar olan çift sayıları içeren bir liste üretir.
Normalde 4–5 satırlık for döngüsünü tek satıra indirir.


"""

#### Quadratzahlen

quadrate = [x**2 for x in range(1, 6)]
print(quadrate)  # ➜ [1, 4, 9, 16, 25]


######## Nur gerade Zahlen

gerade = [x for x in range(10) if x % 2 == 0]
print(gerade)  # ➜ [0, 2, 4, 6, 8]


#################  Liste mit if–else innerhalb (ternärer Ausdruck)

ergebnis = ["gerade" if x % 2 == 0 else "ungerade" for x in range(5)]
print(ergebnis)  # ➜ ['gerade', 'ungerade', 'gerade', 'ungerade', 'gerade']

############## ✅ 2. Pozitif sayıları filtrele

werte = [-4, -2, 0, 3, 5, -1, 6]

positiv = [x for x in werte if x > 0]
print(positiv)  # ➜ [3, 5, 6]


#####    Uzunluğu 5’ten büyük olan kelimeleri filtrele

wörter = ["Hund", "Katze", "Elefant", "Haus", "Schmetterling"]

lange_wörter = [wort for wort in wörter if len(wort) > 5]
print(lange_wörter)  # ➜ ['Elefant', 'Schmetterling']


############## Tenary Operator

zahlen = [-2, -1, 0, 1, 2]

absolute_verdoppelte_zahlen_ohne_0 = [
    (zahl if zahl >= 0 else -zahl) * 2
    for zahl in zahlen
    if zahl != 0
]

print(absolute_verdoppelte_zahlen_ohne_0)


"""
📌 Anlamı Adım Adım:
1. Liste:
zahlen = [-2, -1, 0, 1, 2]
Bu, pozitif, negatif ve sıfır içeren bir sayı listesi.

2. Filtreleme:

for zahl in zahlen if zahl != 0
Sıfır olan değerleri listeye dahil etme! (0 atlanır)

3. Pozitifleştirme (Mutlak Değer):

(zahl if zahl >= 0 else -zahl)
Pozitifse → olduğu gibi al

Negatifse → işaretini değiştir (örneğin -2 → 2)

Aynı şey şu anlama gelir: abs(zahl)

4. İkiyle Çarpma:

(...) * 2
Her değeri ikiyle çarp

5. ✅ Sonuç:

[-2, -1, 0, 1, 2]  
→ 0 hariç  
→ [2, 1, 1, 2]  
→ ×2 → [4, 2, 2, 4]
📤 Çıktı:


[4, 2, 2, 4]
🗣 Türkçe Özet:
Listedeki 0 hariç her sayı alınır.

Sayı negatifse pozitife çevrilir.

Hepsi 2 ile çarpılır.

Yeni liste bu değerleri içerir.
"""