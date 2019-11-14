def print_menu(table, menu_name):
    print(menu_name)
    print()
    for index, element in enumerate(table):
        print("\t" + "(" + str(index+1) +")" + " " + element)
    print("\t" + "(0) Exit")
    print()
    
def print_result(table):
    print()
    print((" ").join(table))
    print()

def print_list(table):
    print()
    for element in table:
        print(element)
    print()