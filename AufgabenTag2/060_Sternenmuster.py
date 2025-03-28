
# Sternenmuster

# Schreibe ein Python-Programm,
# das folgende Sternchen-Muster auf den Bildschirm schreibt:

"""
* * * *
* * * *
* * * *

*
* *
* * *
* * * *
* * * * *

      *
    * * *
  * * * * *
* * * * * * *
"""
###
""""
* * * *
* * * *
* * * *
"""
for i in range(3):   #3 Zeile
    for j in range(4):  #4 stern
        print("*", end=" ")
    print()
print("'##########################################################")
"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(6): #5 Zeile
    for j in range(1,i+1): # jeder zeile bis i Stern
        print("*", end=" ")

    print()

print("'##########################################################")

"""
      *
    * * *
  * * * * *
* * * * * * *
"""
#4 zeile
#jeder zeile gibt es 2 leerzeichen
#jeder zeile 1,3 ,5, 7 sternen

for i in range(4):  # 4 zeile
    # leerzeichen
    print("  " * (3 - i), end="")

    # stern 1, 3, 5 ,7
    print("* " * (2 * i + 1))



