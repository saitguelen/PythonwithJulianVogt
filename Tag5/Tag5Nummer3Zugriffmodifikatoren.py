"""

🧠 Zugriffsmodifikatoren – Nedir?
📌 Tanım:
Erişim belirleyiciler, bir sınıfın içinde tanımlanan değişkenlerin (attribute) ve metotların (method) dışarıdan erişilip erişilemeyeceğini belirler.

🚦 Python’da 3 Tür Erişim Seviyesi:
Seviye	        Kullanımı	                Anlamı
public	        name	                    Her yerden erişilebilir
protected	    _name (tek alt çizgi)	    Sadece sınıf içi ve alt sınıflar
private	        __name (çift alt çizgi)	    Sadece tanımlandığı sınıf içinde

"""

class Mensch:
    def __init__(self):
        self.name = "Sait"         # public
        self._beruf = "Lehrer"     # protected (sözde)
        self.__gehalt = 3000       # private

    def zeige_gehalt(self):
        return self.__gehalt


p = Mensch()

print(p.name)           # ✅ public → Erişilebilir
print(p._beruf)         # ⚠️ protected → Erişilebilir ama önerilmez
# print(p.__gehalt)     # ❌ private → HATA verir

print(p.zeige_gehalt()) # ✅ doğru şekilde erişim
