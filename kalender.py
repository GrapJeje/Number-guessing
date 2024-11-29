from datetime import datetime, timedelta
import os

tasks = [] 
time = datetime.now()

class Task:
    def __init__(self, day, time, task, completed):
        self.day = day
        self.time = time
        self.task = task
        self.completed = completed  
        
def askForInput(message):
    choose = input(f"{message} \n> ")
    return choose

def nextDay():
    global time
    time += timedelta(days=1)
    print(f"Volgende dag is: {time.strftime('%d %B %Y')}")

def previousDay():
    global time
    time += timedelta(days=-1)
    print(f"Volgende dag is: {time.strftime('%d %B %Y')}")

def addTask():
    addTime = askForInput("Voor hoelaat staat deze taak:")
    addInput = askForInput("Wat moet er gedaan worden:")
            
    tasks.append(Task(time, addTime, addInput, False))
    print("Task added successfully")
    
def showTasks():
    print("---------------- Kalender ----------------")
    print(time.strftime("Het is vandaag %d %B %Y, %H:%m:%S"))
    if tasks:
        for i, task in enumerate(tasks):
            status = "✓" if task.completed else "✗"
            print(f"[{i + 1}] {task.time} - {task.task} [{status}]")
    else:
        print("Geen taken beschikbaar.")
    print("------------------------------------------")

def completeTask():
    if tasks:
        print("Welke taak wil je als voltooid markeren?\n")
        showTasks()
        try:
            task_number = int(input("Voer het nummer van de taak in: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks[task_number].completed = True
                print("Taak gemarkeerd als voltooid!")
            else:
                print("Ongeldig nummer.")
        except ValueError:
            print("Ongeldige invoer.")
    else:
        print("Geen taken om te voltooien.")

while True:
    os.system("cls")
    print(time.strftime("Het is vandaag %d %B %Y, %H:%m:%S\n"))
    print("Wat wil je doen?")
    choose = askForInput("[Volgende] [Vorige] [Add] [Complete] [Show] [Stop]")
    
    match choose:
        case "volgende":
            os.system("cls")
            nextDay()
        case "vorige":
            os.system("cls")
            previousDay()
        case "add":
            os.system("cls")
            addTask()
        case "complete":
            os.system("cls")
            completeTask()
        case "show":
            os.system("cls")
            showTasks()
        case "stop":
            os.system("cls")
            break
        case _:
            print("Ongeldige keuze. Probeer opnieuw.")
    
    input("\nPress Enter to continue")