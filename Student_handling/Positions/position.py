import ui
import data_manager
import common
import sys
import main
from Application import aplication
from Student import student

def handle_menu():
    menu = ["Create position",
            "Check position by ID",
            "List all positions",
            "Update position description",
            "Delete position"
    ]
    menu_name = "Position manager menu:"
    ui.print_menu(menu, menu_name)

def choose():
    option = input("Choose a function: ")
    file_name = "Positions/position.txt"
    table = data_manager.get_data(file_name)
    if option == "1":
        data_manager.append_data(create_position(),file_name)
    elif option == "2":
        postion_id = input("Which position you want to check? Please enter the ID: ")
        ui.print_list(check_position(table, postion_id))
    elif option == "3":
        ui.print_list(read_all_position(table))
    elif option == "4":
        position_id = input("Which position you want to update? Please enter the ID: ")
        data_manager.export_data(update_position(table, position_id), file_name)
    elif option == "5":
        position_id = input("Which position you want to delete? Please enter the ID: ")
        data_manager.export_data(delete_position(table, position_id), file_name)
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
            print ("There is no such option, Plese choose from 0 to 5!")

def create_position():
    element_list = [common.random_id()]
    question = input("Describe the new position: ") 
    element_list.append(question)
    
    while True:
        question = input("Number of seats: ")
        try:
            if int(question) > 0:
                element_list.append(question)
                break
        except:
            pass

    process = True
    while process:
        id_ = 0
        company_id = input("Company ID for the position: ")
        table = data_manager.get_data("Company/company.txt")
        for element in table:
            if element[id_] == company_id:
                element_list.append(company_id)
                process = False

    return element_list

def check_position(table, id_):
    app_position_id = -1
    app_student_id = -2
    aplication_table = data_manager.get_data("Application/aplication.txt")
    student_table = data_manager.get_data("Student/students.txt")
    student_id = 0
    result = []

    for element in table:
        if id_ == element[student_id]:
            result.append(element)
            for elem in aplication_table:
                if elem[app_position_id] == id_:
                    print("hi")
                    for item in student_table:
                        if item[student_id] == elem[app_student_id]:
                            result.append(item)
    
    if result:
        return result
    
    return ["No such ID in the list."]

def read_all_position(table):
    table_a = table [:]
    num_of_seats = -2
    id_ = 0
    aplication_table = data_manager.get_data("Application/aplication.txt")
    app_position_id = -1
    tmp = []

    for elem in table_a:
        result = 0
        for item in aplication_table:
            if item[app_position_id] == elem[id_]:
                result += 1
        elem.append(str(elem[num_of_seats] + "/" + str(result)))
        tmp.append(elem)
    return tmp
        

def update_position(table, id_):
    position_id = 0
    description = 1
    tmp = []

    for element in table:
        if element[position_id] == id_:
            element[description] = input("Update the description: ")
            tmp.append(element)
        else:
            tmp.append(element)
    
    return tmp

def delete_position(table, id_):
    position_id = 0
    tmp = []

    application_id = -1
    application_table = data_manager.get_data("Application/aplication.txt")

    for field in application_table:
        if field[application_id] == id_:
            ui.print_result(["We can't delete position with active application."])
            return table

    for element in table:
        if element[position_id] != id_:
            tmp.append(element)
    return tmp