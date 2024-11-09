


notes = {}

def main():
    finished = False
    while finished == False:
        action = get_Action()

        if action == "Add":
            add_Notes()
    
        finished = check_Done(finished)



def get_Action():
    options = ["Add", "Update", "Delete", "Print"]
    selection_phrase = "Select from the available options Below \n'Add', 'Update', 'Delete', 'Print' \n: "
    
    valid_option = False
    while valid_option == False:
        selection = input(selection_phrase)
        
        for option in options:
            if selection.lower() == option.lower():
                valid_option = True
                selection = option
                print(f"'{selection}' Selected")
            if selection not in options:
                selection_phrase = "Option You've Selected is either not in the expected list or not up to date, please try again"

    return selection

def add_Notes():
    title = input("What is the title of the note you'd like to add?\n: ")
    message = input("What is the note you'd like to write?\n: ")

    notes[title] = message

    print(f"{title} : {message}")


def check_Done(finished):
    options = ["Yes", "Y", "No", "N"]
    selection_phrase = "Are you Finished? ('Yes', 'Y', 'No', 'N')\n: "
    valid_option = False
    while valid_option == False:
        selection = input(selection_phrase)
        
        for option in options:
            if selection.lower() == option.lower():
                valid_option = True
                selection = option

    if selection == "Yes" or selection == "Y":
        finished = True

    return finished











main()