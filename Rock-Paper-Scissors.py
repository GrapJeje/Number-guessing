import random
import sys
import time

print("Regels om te winnen van STEEN PAPIER SCHAAR zijn:\n"
      + "Steen vs Papier -> Papier wint\n" 
      + "Steen vs Schaar -> Steen wint\n"
      + "Papier vs Schaar -> Schaar wint\n")

while True:
    time.sleep(1)
 
    print("Vul jouw keuze in \n" 
          + "1 - Steen\n" 
          + "2 - Papier\n"
          + "3 - Schaar\n")

    player_choice = int(input("Vul jouw keuze in: "))
    player_word_choice = ""

    while not (1 <= player_choice <= 3):
        player_choice = int(input("Ongeldige keuze. Vul een juiste keuze in (1, 2, 3): "))
    
    if player_choice == 1:
        player_word_choice = "Steen"
    elif player_choice == 2:
        player_word_choice = "Papier"
    else:
        player_word_choice = "Schaar"

    print("Jouw keuze is: ", player_word_choice)
    time.sleep(1)

    print("Nu is het de bot zijn keus...")
    time.sleep(1)

    computer_choice = random.randint(1, 3)
    computer_word_choice = ""

    if computer_choice == 1:
        computer_word_choice = "Steen"
    elif computer_choice == 2:
        computer_word_choice = "Papier"
    else:
        computer_word_choice = "Schaar"

    print("De bot zijn keuze is: ", computer_word_choice)
    time.sleep(1)

    print(player_word_choice, " vs ", computer_word_choice)
    time.sleep(1)

    if player_choice == computer_choice:
        print("<== Het is gelijkspel! ==>")
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        print("<== Jij hebt gewonnen! ==>")
    else:
        print("<== De bot heeft gewonnen! ==>")

    time.sleep(1)
    print("Wil je nog een keer spelen? (J/N)")
    ans = input().lower()

    if ans == 'n' or ans == 'nee':
        break
 
print("Bedankt voor het spelen!")
sys.exit()
