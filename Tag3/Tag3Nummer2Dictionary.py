################## Dictionary        #####################
"""
Dictionaries verwendetn anstelle der Indices Schlüssel, um auf die Werte zuzugreifen.
--Schlüssel sollten möglichst String sein.


📘 Dictionary (Sözlük) Nedir?
Python’daki dictionary (kısaca: dict), anahtar-değer (key-value) çiftleriyle çalışan bir veri yapısıdır.
Yani: Her bilginin bir anahtarı (key) ve karşısında değeri (value) vardır.

✅ Neden Dictionary Kullanırız?
Birden fazla veri türünü anlamlı bir şekilde saklamak için

Hızlı erişim sağlamak için

Yapılandırılmış veriler için (örneğin kişi bilgisi, ürün bilgisi)

"""

##Beispiel

wörterbuch = {"name":"thomas", "age": 30, 10:45}  #Key 10 geht , ist aber unschön
print(wörterbuch)
print(wörterbuch["name"])

##Das Hinzufügen neuer Werte oder Überschreiben vorhandener Werte ist über einfaches Setzen einer Valuezu dem neuen/vorhandenen Key möglich

wörterbuch["age"] = 31  #{'name': 'thomas', 'age': 31, 10: 45}
print(wörterbuch)

 # Oder neu Value hinzufügen
wörterbuch["beruf"]="Informatiker"
print(wörterbuch)  #{'name': 'thomas', 'age': 31, 10: 45, 'beruf': 'Informatiker'}

##❌ Anahtar Silmek

del wörterbuch[10]
print(wörterbuch)  #Ausgabe : {'name': 'thomas', 'age': 31, 'beruf': 'Informatiker'}

#🔑 keys()----------->Sie enthält alle Schlüssel.  tüm anahtarlari verir

person = {"name": "Sait", "alter": 30, "stadt": "Berlin"}
print(person.keys())
# Ausgabe: dict_keys(['name', 'alter', 'stadt'])


#📦 values()------------------>Gibt alle Werte zurück (value). tüm degerleri value verir.

print(person.values())
# Ausgabe: dict_values(['Sait', 30, 'Berlin'])

##🔁 items()---------------->Gibt alle Schlüssel-Wert-Paare (Schlüssel-Wert) zurück. → Als Tupel Tüm anahtar-değer çiftlerini (key-value) verir. → Tuple olarak

print(person.items())
# Ausgabe: dict_items([('name', 'Sait'), ('alter', 30), ('stadt', 'Berlin')])

# Schleife:
for key, value in person.items():
    print(key, "→", value)
"""
🔄 update() – Ne işe yarar?
 Methode wird verwendet, um ein neues Schlüssel-Wert-Paar zu einem Wörterbuch hinzuzufügen 
 oder den Wert eines vorhandenen Schlüssels zu aktualisieren.
👉 update() metodu, bir sözlüğe yeni anahtar-değer (key-value) çifti eklemek veya mevcut 
bir anahtarın değerini güncellemek için kullanılır.
"""

person = {"name": "Sait", "stadt": "Berlin"}

person.update({"alter": 30})

print(person)
# Ausgabe: {'name': 'Sait', 'stadt': 'Berlin', 'alter': 30}


person.update({"stadt": "Hamburg"})
print(person)
# Ausgabe: {'name': 'Sait', 'stadt': 'Hamburg', 'alter': 30}
