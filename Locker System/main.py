# main.py
import time
import json
import os

dataFile = "data.txt"

def readLockers(file):
    """
    Leest de kluisgegevens uit een tekstbestand.
    
    Parameters:
    file (str): Het bestand waarin de kluisgegevens zijn opgeslagen.
    Returns:
    list: Lijst met kluisgegevens.
    """
    if not os.path.exists(file):
        return []

    try:
        with open(file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Fout bij het lezen van de kluis: {e}")
        return []

def saveLockers(lockerList, file):
    """
    Slaat de kluisgegevens op in een tekstbestand.
    
    Parameters:
    lockerList (list): Lijst met kluisgegevens.
    file (str): Het bestand waarin de kluisgegevens worden opgeslagen.
    """
    try:
        with open(file, 'w') as f:
            json.dump(lockerList, f, indent=4)
    except Exception as e:
        print(f"Fout bij het opslaan van de kluis: {e}")

def LockerCount(lockerList):
    """
    Toont het aantal beschikbare kluizen en welke kluizen beschikbaar zijn.
    
    Parameters:
    lockerList (list): Lijst met kluisgegevens.
    """
    availableLockers = [locker for locker in lockerList if locker['lockerPassword'] is None]

    aLCount = len(availableLockers)

    print(f"Aantal beschikbare lockers: {aLCount}")
    time.sleep(1)
    print("---------------\n" + "Beschikbare Lockers:")

    for locker in availableLockers:
        time.sleep(0.5)
        print(f"Locker: {locker['lockerNumber']} (Wachtwoord: {locker['lockerPassword']})")

    print("---------------\n")
    time.sleep(1)

def NewLocker(totalAmount: int, file):
    """
    Laat de gebruiker een nieuwe kluis openen. De gebruiker kiest een 
    beschikbare kluis en stelt een wachtwoord in.
    
    Parameters:
    totalAmount (int): Totaal aantal kluizen.
    file: Het bestand waarin de kluisgegevens worden opgeslagen.
    """
    while True:
        lockerNumber = input("Kies een kluisnummer:\n")
        
        if not lockerNumber.isnumeric() or not (1 <= int(lockerNumber) <= totalAmount):
            print("Ongeldig nummer. Kies een juiste lockernummer")
            continue

        locker = next((l for l in lockerList if l['lockerNumber'] == lockerNumber), None)

        if locker is None:
            print(f"Kluisnummer {lockerNumber} bestaat niet of is niet beschikbaar.")
            continue
        
        if locker['lockerPassword'] is not None:
            print(f"Kluisnummer {lockerNumber} is al bezet, kies een ander nummer:\n")
            continue

        password = input("Kies een wachtwoord voor uw kluis:\n")

        if not password.isnumeric() or not len(password) == 4:
            print("Wachtwoord moet bestaan uit vier cijfers")
            continue

        locker['lockerPassword'] = password
        print(f"Kluis ({lockerNumber}) is succesvol aangemaakt!")

        saveLockers(lockerList, file)
        break

def OpenLockerTemporary(file):
    """
    Laat de gebruiker een kluis tijdelijk openen. De gebruiker voert 
    het kluisnummer en het wachtwoord in. Bij succesvolle invoer 
    verschijnt een bericht dat de kluis nu tijdelijk open is.
    
    Parameters:
    file: Het bestand waarin de kluisgegevens zijn opgeslagen.
    """
    while True:

        lockerNumber = input("Vul hier je locker nummer in:\n")
        password = input("Vul hier je wachtwoord in:\n")

        locker = next((l for l in lockerList if l['lockerNumber'] == lockerNumber), None)

        if locker is None:
            print(f"Kluisje {lockerNumber} bestaat niet!")
            continue
    
        if locker['lockerPassword'] == password:
            print(f"Kluisje {lockerNumber} is nu tijdelijk open.")
            break
        else:
            print("Onjuist wachtwoord. Probeer het opnieuw.")
            continue

def OpenLocker(file):
    """
    Laat de gebruiker een kluis permanent openen. Na invoer van het 
    kluisnummer en wachtwoord wordt de kluis uit de lijst verwijderd.
    
    Parameters:
    file: Het bestand waarin de kluisgegevens zijn opgeslagen.
    """
    while True:

        lockerNumber = input("Vul hier je locker nummer in:\n")
        password = input("Vul hier je wachtwoord in:\n")

        locker = next((l for l in lockerList if l['lockerNumber'] == lockerNumber), None)

        if locker is None:
            print(f"Kluisje {lockerNumber} bestaat niet!")
            continue
    
        if not locker['lockerPassword'] == password:
            print("Onjuist wachtwoord. Probeer het opnieuw.")
            continue
        else:
            locker['lockerPassword'] = None
            print(f"Kluis {lockerNumber} is permanent geopend en verwijderd!")
            saveLockers(lockerList, file)
            break

def printChoiceMenu():
    return input("---------------\n" +
          "1 - Beschikbare kluizen\n" +
          "2 - Nieuwe kluis openen\n" +
          "3 - Kluis tijdelijk openen\n" +
          "4 - Kluis permanent opnenen\n" +
          "5 - Applicatie sluiten\n" +
          "---------------\n" +
          "\nMaak graag een keuze:\n")

lockerList = readLockers(file=dataFile)

while True:
    choice = printChoiceMenu()
    if not choice.isnumeric():
        choice =  print("Vul graag een nummer in!\n")
        continue
    
    match choice:
        case "1":
            LockerCount(lockerList)
        case "2":
            NewLocker(totalAmount=30, file=dataFile)
        case "3":
            OpenLockerTemporary(file=dataFile)
        case "4":
            OpenLocker(file=dataFile)
        case "5":
            break
