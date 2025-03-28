"""
🧠 Magic Method Nedir?
📌 Tanım:
Magic methods, Python sınıflarına özel yetenekler kazandıran, çift alt çizgi ile tanımlanan (__init__, __str__, __len__, vs.) özel fonksiyonlardır.

Python bu metodları otomatik olarak çağırır. Sen çağırmasan bile, Python arka planda çağırır.

🔮 Neden “Magic”?
Çünkü bunlar Python’da:

Operatörlerin (+, ==, len() vs.)

Fonksiyonların (print(), str(), repr()...)

Nesne davranışlarının arka plandaki gizli işleyişini kontrol eder.

🔧 Örnek Magic Methods:
Metot	            Açıklama
__init__	        Nesne oluşturulunca otomatik çalışır
__str__	            print(obj) dediğinde görüntüyü belirler
__len__	            len(obj) çağrıldığında çalışır
__eq__	            obj1 == obj2 karşılaştırması yapılır
__add__	            obj1 + obj2 toplama işlemi yapılır

🎯 Neden Kullanılır?
✅ Nesneleri daha anlaşılır ve güçlü hale getirmek için
✅ Operatör davranışlarını özelleştirmek için
✅ Python’un yerleşik fonksiyonlarıyla (len, print, vs.) uyumlu nesneler oluşturmak için

🧠 Özet:
Magic Method	    Ne Zaman Çalışır?
__init__()	        Nesne oluşturulurken
__str__()	        print(obj) çağrıldığında
__len__()	        len(obj) çağrıldığında
__eq__()	        obj1 == obj2 yazıldığında
__add__()	        obj1 + obj2 yazıldığında
"""

class Auto:
    def __init__(self, marke):
        self.marke = marke

    def __str__(self):
        return f"Ein Auto der Marke {self.marke}"

mein_auto = Auto("BMW")
print(mein_auto)  # __str__ otomatik çağrılır!


#1️⃣ __str__ → Yazdırma (print) davranışı

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hallo, ich bin {self.name}."

p = Person("Sait")
print(p)   # Otomatik __str__ çalışır


#2️⃣ __len__ → len(obj) desteği

class Schule:
    def __init__(self, schueler_liste):
        self.schueler = schueler_liste

    def __len__(self):
        return len(self.schueler)

s = Schule(["Ali", "Sait", "Nora", "Thomas"])
print(len(s))  # __len__ çağrılır

#3️⃣ __add__ → Toplama + davranışı

class Zahl:
    def __init__(self, wert):
        self.wert = wert

    def __add__(self, andere):
        return Zahl(self.wert + andere.wert)

    def __str__(self):
        return f"Wert: {self.wert}"

a = Zahl(10)
b = Zahl(5)
c = a + b   # __add__ çağrılır
print(c)    # __str__ çağrılır

"""
🧠 __eq__(self, other) Nedir?
📌 Tanım:
Nesneler == operatörü ile karşılaştırıldığında otomatik olarak __eq__ metodu çağrılır.

📌 Açıklama:
p1 == p2 yazıldığında Python şunu yapar:


p1.__eq__(p2)
Eğer __eq__ metodu tanımlanmazsa Python varsayılan olarak id() adreslerini karşılaştırır, yani aynı nesne mi diye bakar (bu da genelde False olur).

🧠 Özet:
Kod	                                     Açıklama
== kullanılır	                        __eq__() otomatik çağrılır
return self.alter == other.alter	    içerik karşılaştırması yapılır


"""
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def __eq__(self, other):
        return self.name == other.name and self.alter == other.alter


p1 = Person("Sait", 30)
p2 = Person("Sait", 30)
p3 = Person("Ali", 25)

print(p1 == p2)  # True (aynı bilgiye sahip)
print(p1 == p3)  # False
