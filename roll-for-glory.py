import time
import random
import sys

player_points = 0
house_points = 0
house_secret_points = 0
round = 0

def determerWinner() :
    if player_points > house_secret_points :
        print("<== Jij hebt gewonnen! ==>\n")
    else :
        print("<== De dealer heeft gewonnen! ==>\n")
    
    if round == 1:
        print("De dealer had een ", house_secret_points, " gegooit!")
    else :
        print("De dealer had in ", round, " rondes in totaal ", house_secret_points, " gegooit!")

print("Regels om Roll For Glory te winnen!\n" 
      + "Roll meer dan de dealer en win!\n"
      + "Je hebt maximaal 5 rondes. Succes!\n")
time.sleep(1)

print("Typ iets om te gooien!")
ans = input()

while True:
    time.sleep(1)
    round += 1

    if round == 5 :
        print("\n" 
              + "Laatste ronde!\n")
        time.sleep(1)

    if round >= 6:
        determerWinner()
        break

    print("<== Jouw beurt ==>")
    time.sleep(1)

    player_roll = random.randint(1, 10)
    player_points = player_points + player_roll

    print("\n" 
          + "Jij hebt een ", player_roll, "gegooit!")
    time.sleep(1)
    
    house_roll = random.randint(1, 10)
    house_secret_points = house_secret_points + house_roll

    print("<== Dealer's beurt ==>")
    time.sleep(1)

    print("\n" 
          + "De dealer heeft gegooit!")
    time.sleep(1)

    if round == 1:
        print("\n"
              + "Jij hebt een ", player_points, " gegooit.")
    else :
        print("\n" 
          +"De dealer heeft nu ", house_points, " punten in ", (round - 1), " beurt(en)\n"
          + "Jij hebt nu ", player_points, " punten in ", round, " beurt(en)\n")

    time.sleep(2)
    print("Wil jij hitten of zo blijven staan? (H/S)")
    choice = input().lower()

    if choice == 's':
        determerWinner()
        time.sleep(1)

        print("Wil je nog een keer spelen? (J/N)")
        ans = input().lower()

        if ans == 'n' or ans == 'nee':
            break
        else :
            round = 0
            player_points = 0
            house_points = 0
            house_secret_points = 0
    
    house_points = house_secret_points
print("Bedankt voor het spelen!")
sys.exit()
