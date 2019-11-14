import ui
import data_manager
import common
import sys
import main

def handle_menu():
    menu = ["Add new company",
            "Check company by ID",
            "List all companies",
            "Update company name",
            "Delete company"
    ]
    menu_name = "Company menu:"
    ui.print_menu(menu, menu_name)

def choose():
    option = input("Choose a function: ")
    file_name = "Company/company.txt"
    table = data_manager.get_data(file_name)
    if option == "1":
        data_manager.append_data(create_company(),file_name)
    elif option == "2":
        company_id = input("Which company you want to check? Please enter the ID: ")
        ui.print_result(check_company(table, company_id))
    elif option == "3":
        ui.print_list(table)
    elif option == "4":
        company_id = input("Which company you want to update? Please enter the ID: ")
        data_manager.export_data(update_company(table, company_id), file_name)
    elif option == "5":
        company_id = input("Which company you want to delete? Please enter the ID: ")
        data_manager.export_data(delete_company(table, company_id), file_name)
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

def create_company():
    element_list = [common.random_id()]
    question = input("Give us a company name: ")
    
    element_list.append(question)
    return element_list

def check_company(table, id_):
    company_id = 0
    for element in table:
        if id_ == element[company_id]:
            return element
    
    return "No such ID in the list."

def update_company(table, id_):
    tmp = []
    company_id = 0
    for element in table:
        if element[company_id] != id_:
            tmp.append(element)
        else:
            element_list = [element[company_id]]
            answer = input("Give me the new name: ")
            element_list.append(answer)
            tmp.append(element_list)
    return tmp

def delete_company(table, id_):
    company_id = 0
    tmp = []
    position_id = -1
    position_table = data_manager.get_data("Positions/position.txt")
    for field in position_table:
        if field[position_id] == id_:
            ui.print_result(["Can't delete a company with open position."])
            return table
            
    for element in table:
        if element[company_id] != id_:
            tmp.append(element)
    return tmp