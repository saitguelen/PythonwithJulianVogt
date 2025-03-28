"""
📘 JSON Nedir?
JSON (JavaScript Object Notation), verileri metin olarak saklamak ve göndermek için kullanılan bir veri formatıdır.

Python’da JSON verisi genellikle dict (sözlük) gibi görünür.

🧠 Python'da JSON kullanmak için:
İlk olarak, yerleşik json modülünü import etmelisin:

python
Kopieren
Bearbeiten
import json
🔁 JSON ↔ Python dönüşümleri:
Amaç	Fonksiyon	Açıklama
Python verisini JSON'a çevir	json.dumps()	dict → JSON string (ekrana yazmak için)
Python verisini dosyaya yaz	json.dump()	dict → JSON dosyasına yazmak için
JSON string’ini Python’a çevir	json.loads()	JSON string → dict (okumak için)
JSON dosyasını Python’a çevir	json.load()	JSON dosya → dict
🧪 1. Python → JSON string (dumps())
python
Kopieren
Bearbeiten
import json

person = {"name": "Sait", "alter": 30, "stadt": "Berlin"}

json_string = json.dumps(person)
print(json_string)
📌 dumps() → dict'i JSON formatına çevirir.
🟢 Çıktı:

json
Kopieren
Bearbeiten
{"name": "Sait", "alter": 30, "stadt": "Berlin"}
🧪 2. JSON string → Python sözlük (loads())
python
Kopieren
Bearbeiten
import json

daten = '{"name": "Sait", "alter": 30, "stadt": "Berlin"}'

person = json.loads(daten)
print(person["name"])  # Sait
📌 loads() → JSON formatındaki metni Python dict’e çevirir.

📁 3. JSON'u dosyaya kaydetmek (dump())
python
Kopieren
Bearbeiten
import json

data = {"name": "Sait", "alter": 30}

with open("person.json", "w") as dosya:
    json.dump(data, dosya)
🟢 Bu kod "person.json" adlı dosyaya JSON olarak yazar.

📥 4. JSON dosyasını okumak (load())
python
Kopieren
Bearbeiten
import json

with open("person.json", "r") as dosya:
    inhalt = json.load(dosya)

print(inhalt["name"])  # Sait
📌 load() → JSON dosyasını okur ve dict olarak döner.

📚 Gerçek Hayat Senaryosu
Birden fazla kişiyi kaydeden bir yapı:

python
Kopieren
Bearbeiten
personen = [
    {"name": "Ali", "alter": 25},
    {"name": "Sait", "alter": 30},
    {"name": "Merve", "alter": 28}
]

with open("personen.json", "w") as f:
    json.dump(personen, f, indent=4)
Açıklama:
json.dump(...) → dosyaya yazar

indent=4 → dosyada güzel görünsün diye girinti ekler

🟢 Dosyanın içeriği şöyle olur:

json
Kopieren
Bearbeiten
[
    {
        "name": "Ali",
        "alter": 25
    },
    {
        "name": "Sait",
        "alter": 30
    },
    {
        "name": "Merve",
        "alter": 28
    }
]
✅ En sık kullanılan senaryolar:
Senaryo	Kullanman gereken
Veriyi ağ üzerinden göndermek	json.dumps()
JSON dosyasına yazmak	json.dump()
JSON cevabını okumak (API'den)	json.loads()
JSON dosyasını programla kullanmak	json.load()
🗣 Türkçe Özet:
json.dumps() → Python verisini JSON metnine çevirir

json.loads() → JSON metnini Python verisine çevirir

json.dump() → JSON verisini dosyaya yazar

json.load() → JSON dosyasını okur

"""