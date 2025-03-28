"""

🧠 Docstring Nedir?
📌 Tanım:
Docstring, bir fonksiyonun, sınıfın ya da modülün ne işe yaradığını açıklayan özel bir metin bloğudur.

Üçlü tırnak (""" """" veya ''' ''') arasında yazılır.

Fonksiyonun hemen altına yazılır.

Fonksiyonun nasıl kullanıldığını, parametreleri ve dönüş değerini açıklar.
"""


def quadrat(x):
    """
    Gibt das Quadrat einer Zahl zurück.

    Parameter:
    x (int): Die Zahl, die quadriert werden soll

    Rückgabe:
    int: Das Quadrat der Zahl
    """
    return x * x


help(quadrat)


"""
📚 Nerelerde Kullanılır?
Fonksiyonlar

Sınıflar

Modüller

Dosya başlığı olarak

🧠 Neden Kullanılır?
Neden?	                        Açıklama
Kod okunabilirliği	            Başkası fonksiyonu okurken ne yaptığını anlar
Otomatik dokümantasyon	        help(), VS Code tooltip gibi yerlerde çıkar
Takım çalışması	                İş arkadaşların ne yaptığını kolay anlar
"""

def bestellung(*produkte, **details):
    """
    Gibt eine Übersicht über bestellte Produkte und Kundendetails.

    Parameter:
    produkte (tuple): Liste der bestellten Produkte
    details (dict): Kundendaten wie Name, Adresse, Lieferung

    Rückgabe:
    None
    """
    print("Bestellung wurde aufgenommen.")
