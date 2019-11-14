def get_data(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n","").split(",") for element in lines]
    return table

def export_data(table, filename):
    with open(filename, "w") as file:
        for record in table:
            row = (",").join(record)
            file.write(row + "\n")

def append_data(table, filename):
    row = ""
    with open(filename, "a") as file:
        for record in table:
            if record != table[-1]:
                row += record + ","
            else:
                row += record    
        file.write(row + "\n")