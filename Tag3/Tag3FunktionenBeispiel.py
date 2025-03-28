"""
🎯 Hedefimiz:
Birden fazla öğrencinin:

Adı

Puanı

Harf notu

Bu verileri bir liste içinde sözlük (dictionary) olarak tutacağız

JSON dosyasına kaydedeceğiz

Dosyayı tekrar okuyup ekrana yazdıracağız
"""

#✅ 1. Fonksiyon: Sayısal puanı harf notuna çevir

def not_hesapla(puan):
    if puan >= 90:
        return "AA"
    elif puan >= 80:
        return "BA"
    elif puan >= 70:
        return "BB"
    elif puan >= 60:
        return "CB"
    elif puan >= 50:
        return "CC"
    else:
        return "FF"
#✅ 2. Öğrenci verilerini al ve listeye ekle

import json

ogrenciler = []

while True:
    ad = input("Öğrenci adı (çıkmak için boş bırak): ")
    if ad == "":
        break

    puan = int(input("Notu: "))
    harf = not_hesapla(puan)

    ogrenci = {
        "ad": ad,
        "puan": puan,
        "harf": harf
    }

    ogrenciler.append(ogrenci)

#✅ 3. Verileri JSON dosyasına kaydet
with open("ogrenciler.json", "w", encoding="utf-8") as dosya:
    json.dump(ogrenciler, dosya, ensure_ascii=False, indent=4)

#✅ 4. JSON dosyasını okuyup yazdır

with open("ogrenciler.json", "r", encoding="utf-8") as dosya:
    veriler = json.load(dosya)

print("\n--- Kayıtlı Öğrenciler ---")
for ogr in veriler:
    print(f"{ogr['ad']} → {ogr['puan']} puan → {ogr['harf']}")


"""
🗂 Yapı Özeti:
🔢 puan → sayısal not

🔠 harf → harf notu (fonksiyonla hesaplandı)

📄 JSON dosyası: kalıcı olarak saklanır

📋 Tekrar okunduğunda tüm veriler geri gelir

"""