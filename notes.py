

notes = {}

options = ["Add", "Update", "Delete", "Print"]

selection_phrase = "Select from the available options Below \n'Add', 'Update', 'Delete', 'Print' \n: "
finished = False
while finished == False:
    selection = input(selection_phrase)
    
    
    for option in options:
        if selection.lower() == option.lower():
            finished = True
            selection = option
            print(f"'{selection}' Selected")
        if selection not in options:
            selection_phrase = "Option You've Selected is either not in the expected list or not up to date, please try again"



if selection == "Add":
    title = input("What is the title of the note you'd like to add?\n: ")
    message = input("What is the note you'd like to write?\n: ")

    notes[title] = message

    print(f"{title} : {message}")


print("Done")
input()

## Add
## Update
## Delete