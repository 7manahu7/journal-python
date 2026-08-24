import os
from datetime import datetime
from rich import print
from rich.panel import Panel

def clear():
    os.system("clear")


def remove_file():
    try:
        os.remove("journal.txt")
    except FileNotFoundError:
        print(Panel("Journal doesn't exist yet, type something to get started.", title="No Such File Or Directory"))

def write():
    note = input(" -> ")
    now = datetime.now()
    
    with open("journal.txt", "a") as file:
        file.write(f"{now.strftime("%d %b %Y | %H:%M || ")}")
        file.write(f"{note} \n")

def read():
    
    try:
        
        with open("journal.txt", "r") as file:
            reading = file.read()
            print(Panel(reading, title="notes"))

    except FileNotFoundError:
        print("[green]write something to get started![/green]")


def help():
    print(Panel("     JOURNAL    ", title="journal cli"))
    print(Panel(" 1. Write --allows you to write some text in your journal \n 2. read --allows you to read your text \n 3. quit --quits the current running programme, your journal data is not deleted \n 4. /remove --deletes the journal entirely \n 5. /clear --clars the screen \n 6. /help --prints this message\n"))


def main():

    print(Panel("=========================\n      journal      \n =======================", title="Journal-cli"))
    print("1. write")
    print("2. read")
    print("3. quit")
    print()

    while True:

        print("[cyan] ------------------------")
        choice = input("what to do? ")
        print("[cyan] ------------------------")

        if choice == "1":
            write()

        elif choice == "2":
            read()

        elif choice == "3":
            print(Panel ("[bold magenta]i hope you return :) [/bold magenta]", title=" :)"))
            break

        elif choice.lower() == "/clear":
            clear()
        elif choice.lower() == "/help":
            help()

        elif choice.lower() == "/remove":
            print("[bold red]are you sure you want to remove this file?  [/bold red]")
            choice2 = input("all your journal entries will be deleted forever!  ")

            if choice2.lower() in ("yes", "yeah", "yup"):

                remove_file()

            elif choice2.lower() in ("no", "nah", "nope"):
                write()
            else:
                print("[bold red] you need to choose my guy/girl! [/bold red]")


        else:
            print("you've entered an unseen territory")




main()


