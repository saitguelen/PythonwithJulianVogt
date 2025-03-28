from Tag2.Tag2Nummer1 import namen


class eine_klasse:
    pass

ein_objekt=eine_klasse()
print(type(ein_objekt))

#Methoden können wie Funktionen auch innerhalb der klassendefinition über def erstellt.
#Jede methoden nimmt als ersten Parameter self entgegen

class schüler:
    def begrüßen(self):
        print(self.name, "sagt hallo!")

thomas=schüler()
thomas.name="Thomas"
thomas.begrüßen()


#__init__(self,parameter..) --->Konstruktor#

class schüler:
    def __init__(self, name:str="Anonym",alter:int=0):
        self.name=name
        self.alter=alter
    def begrüßen(self):
        print(f"Der {self.alter} Jahre alte {self.name} sagt Hallo!")

thomas=schüler("Thomas",30)
thomas.begrüßen()
print(thomas.name.upper())


"""
🧠 AssertionError Nedir?
📌 Tanım:
AssertionError, assert ifadesiyle yapılan bir doğrulama (kontrol) başarısız olduğunda ortaya çıkan hata türüdür.

✅ assert Ne Yapar?
assert, “şu ifade doğru olmalı” diye bir kontrol yapar.

Eğer ifade True (doğru) ise hiçbir şey olmaz.

Ama ifade False (yanlış) ise: ❌ AssertionError hatası verir

📦 Ne İçin Kullanılır?
Test yazarken

Hatalı veri girişlerini engellemek için

Geliştirici kendine garanti koymak istediğinde


"""
def prüfe_positiv(x):
    try:
        assert x > 0, "Zahl muss positiv sein!"
        print(f"{x} ist positiv ✅")
    except AssertionError as fehler:
        print("❌ Fehler:", fehler)
prüfe_positiv(65)
prüfe_positiv(-8)
x = 5
assert x > 0    # bu doğru → sorun yok
#assert x < 0    # bu yanlış → AssertionError ❌


x = -3
assert x >= 0, "x darf nicht negativ sein"


