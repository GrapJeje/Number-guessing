import random
import sys
import math

minimaal = int(input("Geef het minimale getal op: "))
maximaal = int(input("Geef een maximale getal op: "))

if (minimaal >= maximaal):
    print("Dit is een onjuist getal!")
    sys.exit()
    
number = random.randint(minimaal, maximaal)
chances = math.ceil((maximaal - minimaal) * 0.1)

print("\n\tJe hebt ", chances, " kansen om het juiste nummer te raden.")
count = 0

while count < chances :
    gok = int(input("Vul hier je gok in: "))

    if (gok == number) :
        print("Gefeliciteerd het getal was: ", number,)
        break

    if (gok > number) :
        print("Het getal is lager!")
        chances = chances - 1
    else :
        print("Het getal is hoger!")
        chances = chances - 1

if (chances == 0) :
        print("Jammer, je kansen zijn op. Het getal was: ", number,)
        sys.exit()
