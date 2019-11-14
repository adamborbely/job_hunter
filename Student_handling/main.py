import sys
import ui 
from Student import student
from Company import company
from Positions import position
from Application import aplication


def choose():
    
    option = input("Enter a number: ")
    if option == "1":
        student.start_module()
    elif option == "2":
        company.start_module()
    elif option == "3":
        position.start_module()
    elif option == "4":
        aplication.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Student menu",
               "Company menu",
               "Position manager",
               "Aplication"
]

    ui.print_menu( options, "Main menu")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError:
            print ("There is no such option, Plese choose from 0 to 4!")

if __name__ == '__main__':
    main()