"""

Python’da try – except yapısı, hataları (exceptions) yakalayıp programın çökmesini önlemek için kullanılır.

🧠 Try–Except Nedir?
📌 Tanım:
try → Hata çıkabilecek kod bloğu
except → Hata olursa çalışacak kod bloğu

try:
    # Hata çıkabilecek kod buraya
except:
    # Hata olursa burası çalışır

"""

#Sifira Bölme

try:
    ergebnis = 10 / 0
except:
    print("Hata: Sıfıra bölme yapılamaz!")

#❗ Normalde program çökebilirdi ama except ile kontrol ettik.

"""
🧱 Yapının Tam Hali

try:
    # denenecek kod
except ExceptionTyp:
    # hata varsa yapılacak
else:
    # hata çıkmazsa yapılacak
finally:
    # her durumda yapılacak (isteğe bağlı)

"""
###
"""
try:
    x = int(input("Sayı gir: "))
except ValueError:
    print("Geçersiz giriş!")
else:
    print("Girilen sayı:", x)
finally:
    print("İşlem tamamlandı.")
"""
#######################
"""
🗣 Türkçe Özet:
try: Hata çıkabilecek kodu dener

except: Hata olursa devreye girer

else: Hata çıkmazsa çalışır (isteğe bağlı)

finally: Ne olursa olsun çalışır (genelde temizlik için)

🧠 Sık Kullanılan Hata Tipleri:
Hata Tipi	                    Açıklama
ValueError	                    Yanlış veri tipi (örneğin: sayı yerine harf)
ZeroDivisionError	            Sıfıra bölme hatası
TypeError	                    Uygun olmayan veri türü işlemi
IndexError	                    Liste sınırlarının dışına çıkmak
FileNotFoundError	            Dosya bulunamadı

"""

################

"""
🎯 Kullanıcıdan bir sayı alacağız
🎯 Bu sayıyı 2’ye böleceğiz
🎯 Hatalı giriş olursa kullanıcıya açıklama vereceğiz
🎯 Hata çıkmazsa sonucu göstereceğiz
🎯 Her durumda “İşlem tamamlandı” yazacağız
"""


def teile_durch_zwei():
    try:
        zahl=int(input("Geben Sie eine Zahl ein:"))
        ergebnis = zahl/2
    except ValueError:
        print("Geben bitte nur eine Zahl ein:")
    except ZeroDivisionError:
        print("Die Zahl kann nicht 0 durchteilen")
    else:
        print(f"Ergebnis: {zahl}/2 = {ergebnis}")
    finally:
        print("Prozess abgeschlossen")

#Beispiel
teile_durch_zwei()

##########Zwei Zahlen teilen

def teile_zwei_zahlen():
    try:
        zahl1 = float(input("Birinci sayıyı gir: "))
        zahl2 = float(input("İkinci sayıyı gir (bölen): "))

        ergebnis = zahl1 / zahl2

    except ValueError:
        print("❌ Hata: Lütfen sadece sayısal değer giriniz.")

    except ZeroDivisionError:
        print("❌ Hata: Sıfıra bölme yapılamaz.")

    except TypeError:
        print("OPERATION UNGÜLTIG FÜR Datentype")

    else:
        print(f"✅ Sonuç: {zahl1} / {zahl2} = {ergebnis:.2f}")

    finally:
        print("🔚 İşlem tamamlandı.")

teile_zwei_zahlen()