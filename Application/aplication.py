import ui
import data_manager
import common
import sys
import main


def handle_menu():
    menu = ["Create application",
            "Update application",
            "Delete application"
    ]
    menu_name = "Application menu:"
    ui.print_menu(menu, menu_name)

def choose():
    option = input("Choose a function: ")
    file_name = "Application/aplication.txt"
    table = data_manager.get_data(file_name)
    if option == "1":
        data_manager.append_data(create_aplication(),file_name)
    elif option == "2":
        application_id = input("Which application you want to update? Please enter the ID: ")
        data_manager.export_data(update_application(table, application_id), file_name)
    elif option == "3":
        application_id = input("Which application you want to delete? Please enter the ID: ")
        data_manager.export_data(delete_application(table, application_id), file_name)
    elif option == "0":
        main.main()
    else:
        raise KeyError ("No such an option exist")

def start_module():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError:
            print ("There is no such option, Plese choose from 0 to 3!")
    
def create_aplication():
    element_list = [common.random_id()]
    question = input("Is it accepted? ")
    element_list.append(question)

    student_check = True
    while student_check:
        id_ = 0
        student_id = input ("Enter the ID of the student: ")
        table = data_manager.get_data("Student/students.txt")
        for element in table:
            if element[id_] == student_id:
                element_list.append(student_id)
                student_check = False
    
    position_check = True
    while position_check:
        id_ = 0
        position_id = input ("Enter the ID of the position: ")
        table = data_manager.get_data("Positions/position.txt")
        for element in table:
            if element[id_] == position_id:
                element_list.append(position_id)
                position_check = False

    return element_list

def update_application(table, id_):
    uniqe_id = 0
    status = 1
    tmp = []
    for element in table:
        if element[uniqe_id] != id_:
            tmp.append(element)
        else:
            element_list = element
            if element_list[status] == "Yes":
                element_list[status] = "No"
            else:
                element_list[status] = "Yes"
            tmp.append(element_list)

    return tmp

def delete_application(table, id_):
    tmp = []
    app_id = 0

    for element in table:
        if element[app_id] != id_:
            tmp.append(element)

    return tmp