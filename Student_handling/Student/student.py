import ui
import data_manager
import common
import sys
import main



def handle_menu():
    menu = ["Add new student",
            "Check student by ID",
            "List all students",
            "Update student information",
            "Change the status of the student",
            "Delete Student"
    ]
    menu_name = "Student menu:"
    ui.print_menu(menu, menu_name)

def choose():
    option = input("Choose a function: ")
    file_name = "Student/students.txt"
    table = data_manager.get_data(file_name)
    if option == "1":
        data_manager.append_data(create_student(),file_name)
    elif option == "2":
        student_id = input("Which student you want to check? Please enter the ID: ")
        ui.print_result(check_student(table, student_id))
    elif option == "3":
        ui.print_list(list_students(table))
    elif option == "4":
        student_id = input("Which student you want to update? Please enter the ID: ")
        data_manager.export_data(update_student(table, student_id), file_name)
    elif option == "5":
        student_id = input("Which student status you want to update? Please enter the ID: ")
        data_manager.export_data(activate(table, student_id), file_name)
    elif option == "6":
        student_id = input("Which student you want to delete? Please enter the ID: ")
        data_manager.export_data(delete_student(table, student_id), file_name)
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
            print ("There is no such option, Plese choose from 0 to 6!")


def create_student():
    element_list = [common.random_id()]
    questions = ["The name of the student: ", "Age of the student: ", "Is he/she active? "]
    for question in questions:
        answer = input(question)
        element_list.append(answer)
    return element_list

def check_student(table, id_):
    student_id = 0
    for element in table:
        if id_ == element[student_id]:
            return element
    
    return "No such ID in the list."

def list_students(table):
    student_id = 0
    student_name = 1
    student_list = []

    for element in table:
        student_list.append(element[student_id] + " " + element [student_name])

    return student_list

def update_student(table, id_):
    student_id = 0
    tmp = []
    for element in table:
        if element[student_id] != id_:
            tmp.append(element)     
        else:
            element_list = [element[student_id]]
            questions = ["The name of the student: ", "Age of the student: ", "Is he/she active? "]

            for question in questions:
                answer = input(question)
                element_list.append(answer)
            
            tmp.append(element_list)
    return tmp

def activate(table, id_):
    student_id = 0
    status = -1
    tmp = []
    for element in table:
        if element[student_id] != id_:
            tmp.append(element)     
        else:
            element_list = element
            if element_list[status] == "Yes":
                element_list[status] = "No"
            else:
                element_list[status] = "Yes"
            tmp.append(element_list)
    return tmp

def delete_student(table, id_):
    student_id = 0
    tmp = []
    application_id = -2
    application_table = data_manager.get_data("Application/aplication.txt")

    for field in application_table:
        if field[application_id] == id_:
            ui.print_result(["We can't delete students with active application."])
            return table
    for element in table:
        if element[student_id] != id_:
            tmp.append(element)
    return tmp