import csv


def main():
    finished = False
    while finished == False:
        action = get_Action()

        if action == "Add":
            add_Note()
        if action == "Read":
            print_Note()
        if action == "Delete":
            delete_Note()
        if action == "Update":
            update_Note()
    
        finished = check_Done(finished)


def get_Action():
    options = ["Add", "Update", "Delete", "Read"]
    selection_phrase = "Select from the available options Below \n'Add', 'Update', 'Delete', 'Read' \n: "
    
    valid_option = False
    while valid_option == False:
        selection = input(selection_phrase)
        
        for option in options:
            if selection.lower() == option.lower():
                valid_option = True
                selection = option
                print(f"'{selection}' Selected")
            if selection not in options:
                selection_phrase = "Option You've Selected is either not in the expected list or not up to date, please try again\n: "

    return selection


def add_Note():
    title = input("What is the title of the note you'd like to add?\n: ")
    message = input("What is the note you'd like to write?\n: ")

    with open("Notes.csv", "a", newline="") as notes_File:
        writer = csv.writer(notes_File, delimiter=',')
        writer.writerow([title, message])

    print(f"{title} : {message}")

    return


def print_Note():
    with open("Notes.csv", newline="") as notes_File:
        reader = csv.DictReader(notes_File, delimiter=",")
        notes = list(reader)

    titles = []
    for row in notes:
        titles.append(row["Title"])
        
    selection_phrase = f"Select from the available notes below.\n{titles}\n"
    valid_title = False
    while valid_title == False:
        selection = input(selection_phrase)
        
        for title in titles:
            if selection.lower() == title.lower():
                valid_title = True
                selection = title
                for row in notes:
                    if row["Title"] == selection:
                        print(row["Note"])

            if selection == "Cancel":
                return

            if selection not in title:
                selection_phrase = "Note youve selected doesnt share a name with a Note already in the list, please try again or type 'Cancel'\n: "

    return


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


def delete_Note():

    with open("Notes.csv", newline="") as notes_File:
        reader = csv.DictReader(notes_File, delimiter=",")
        notes = list(reader)

    titles = []
    for row in notes:
        titles.append(row["Title"])
        
    selection_phrase = f"Select from the available notes below.\n{titles}\n"
    valid_title = False
    while valid_title == False:
        selection = input(selection_phrase)
        
        for title in titles:
            if selection.lower() == title.lower():
                valid_title = True
                selection = title
                for row in notes:
                    if row["Title"] == selection:
                        notes.remove(row)

            if selection == "Cancel":
                return
            
            if selection not in title:
                selection_phrase = "Note youve selected doesnt share a name with a Note already in the list, please try again or type 'Cancel'\n: "
            
    with open("Notes.csv", "w", newline="") as notes_File:
        writer = csv.DictWriter(notes_File, delimiter=",", fieldnames= ["Title", "Note"])
        writer.writeheader()
        for row in notes:
            writer.writerow(row)
    
    return    


def update_Note():

    with open("Notes.csv", newline="") as notes_File:
        reader = csv.DictReader(notes_File, delimiter=",")
        notes = list(reader)
    
    titles = []
    for row in notes:
        titles.append(row["Title"])
        
    selection_phrase = f"Select from the available notes below.\n{titles}\n"
    valid_title = False
    while valid_title == False:
        selection = input(selection_phrase)
        
        for title in titles:
            if selection.lower() == title.lower():
                valid_title = True
                selection = title
                for row in notes:
                    if row["Title"] == selection:
                        print(row["Note"])
                        new_note = input("What would you like the new note to be?\n: ")
                        row["Note"] = new_note
            
            if selection == "Cancel":
                return
            
            if selection not in title:
                selection_phrase = "Note youve selected doesnt share a name with a Note already in the list, please try again or type 'Cancel'\n: "

    with open("Notes.csv", "w", newline="") as notes_File:
        writer = csv.DictWriter(notes_File, delimiter=",", fieldnames= ["Title", "Note"])
        writer.writeheader()
        for row in notes:
            writer.writerow(row)

    return


main()