"""

🔹 *args Nedir? (* = yıldız*)
✅ Tanım:
*args, bir fonksiyona istediğimiz kadar sayıdaki pozisyonel değer göndermemizi sağlar.

Gelen veriler bir tuple (demet) olarak alınır.

Parametreleri sırayla veririz → isim vermeyiz.
"""
def topla(*args):
    print("Gelen değerler:", args)
    print("Toplam:", sum(args))

topla(2, 4, 6)

"""
🔹 **kwargs Nedir? (** = çift yıldız)
✅ Tanım:
**kwargs, fonksiyona anahtar-değer çiftleri (sözlük gibi) göndermek için kullanılır.

Gelen veriler bir dictionary (sözlük) olarak alınır.

Parametreler isim = değer şeklinde verilir.

"""

def bilgiler(**kwargs):
    print("Gelen bilgiler:")
    for anahtar, deger in kwargs.items():
        print(anahtar, ":", deger)

bilgiler(ad="Sait", yas=30, sehir="Berlin")


"""
🔁 *args ve **kwargs Arasındaki Fark
Özellik          	    *args	                                        **kwargs
Tipi	                Tuple (sıralı değerler)	                         Dict (anahtar-değer çiftleri)
Kullanımı	            topla(1, 2, 3)	                                 bilgiler(ad="Sait", yas=30)
Erişim	                args[0], args[1], …	                            kwargs["ad"], kwargs["yas"]
Esneklik	            Değer sayısı önceden bilinmez	                 Anahtar sayısı bilinmez

"""
#🔁 Her İkisini Aynı Fonksiyonda Kullanmak

def ornek(a, b, *args, **kwargs):
    print("Zorunlu:", a, b)
    print("args:", args)
    print("kwargs:", kwargs)

ornek(1, 2, 3, 4, ad="Sait", sehir="Berlin")
ornek(1, 2, 3, 4,5,6,7,8, ad="Sait", sehir="Berlin", yas=30,beruf="ögretmen")

#🔧 Gerçek Hayat Örneği: Toplama Makinesi

def topla(*sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

print(topla(10, 20))
print(topla(5, 10, 15, 20))
print(topla(5, 10, 15, 250,-56,58,21,20,-65))

#🔧 Gerçek Hayat Örneği: Kullanıcı Bilgisi

def kullanici_bilgisi(**bilgi):
    for k, v in bilgi.items():
        print(f"{k}: {v}")

kullanici_bilgisi(ad="Sait", yas=30, email="sait@example.com")


"""
🧠 Hafızada Tutman Gerekenler:
Ne?	                                Açıklama
*args	                            Çok sayıda pozisyonel veri → tuple olur
**kwargs	                        Çok sayıda anahtar-değer verisi → dict olur
İkisi birden	                    Kullanabilirsin ama sıralama önemli: *args, sonra **kwargs
"""

#Siparis listesi alma
"""
🎯 Amaç:
Kullanıcı birçok ürün siparişi verebilsin (ürün1, ürün2, ürün3...) → *args

Ekstra bilgiler girsin: isim, adres, teslimat seçeneği → **kwargs
"""


def bestellung(*produkte, **details):
    print("🛒 Bestellte Produkte:")
    for produkt in produkte:
        print(f"– {produkt}")

    print("\n📋 Kundendaten:")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

#Örnek

bestellung(
    "Pizza", "Cola", "Salat",
    name="Sait", adresse="Berlin", lieferung="Express"
)
