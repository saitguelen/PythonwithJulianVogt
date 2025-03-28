
# Binäre Zahlen

# Schreibe ein Skript, das alle Zahlen von 0-255 binär schreibt:
# Beachte die Leerzeichen zwischen den Ziffern!

"""
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1
0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 1
0 0 0 0 0 1 0 0
...
...
...
1 1 1 1 1 0 1 1
1 1 1 1 1 1 0 0
1 1 1 1 1 1 0 1
1 1 1 1 1 1 1 0
1 1 1 1 1 1 1 1
"""
for i in range(256): # zeile

    binary = format(i, '08b')  # Wandeln wir binär um
    print(" ".join(binary))  # leerzeichen
