
#  Urlaubsanspruch
#
#  Für die Bestimmung des Urlaubsanspruch der Beschäftigten einer Firma
#  soll ein Programm entwickelt werden.
#  Die Grundlage für die Berechnung des Urlaubsanspruch
#  bildet die Betriebsvereinbarung.
#  Das Programm soll die Anzahl der Urlaubstage für
#  jeweils einen Beschäftigten berechnen.
#
#  Betriebsvereinbarung:
#  Allen Beschäftigten stehen 26 Tage Urlaub zu.
#  Minderjährige Beschäftigte erhalten 30 Tage Urlaub.
#  Beschäftigte, die älter als 55 Jahre sind, erhalten 28 Tage Urlaub.
#  Beschäftigte mit einer Behinderung ab 50 % erhalten
#  zusätzlich 5 weitere Tage Urlaub.
#  Beschäftigte mit einer Betriebszugehörigkeit von mehr als 10 Jahren
#  erhalten 2 zusätzliche Tage Urlaub.


print(" Urlaubsanspruch-Rechner ")

alter = int(input("Wie alt sind Sie: "))
behinderung = int(input(" Behinderungsgrad (in %)? "))
betriebszugehörigkeit = int(input(" Betriebszugehörichkeit? :  "))


# Grundurlaub

if alter < 18:
    urlaub = 30
elif alter > 55:
    urlaub = 28
else:
    urlaub = 26

#  Behinderung

if behinderung >= 50:
    urlaub += 5

#  Betriebszugehörigkeit

if betriebszugehörigkeit > 10:
    urlaub += 2
print(f"Der Beschäftigte hat Anspruch auf insgesamt {urlaub} Urlaubstage.")

