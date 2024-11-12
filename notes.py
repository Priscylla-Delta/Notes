import csv


## Loops Through the functionality of the Notes Application until the user is finished
def main():
    finished = False
    while finished == False:
        ## Requests which valid action the user would like to do
        action = get_Action()

        if action == "Add":
            add_Note()
        if action == "Read":
            print_Note()
        if action == "Delete":
            delete_Note()
        if action == "Update":
            update_Note()
    
        ## Every Loop the user is asked if they are done using the app, if not it loops
        finished = check_Done(finished)


def get_Action():
    ## Initializes valid functionality
    options = ["Add", "Update", "Delete", "Read"]
    selection_phrase = "Select from the available options Below \n'Add', 'Update', 'Delete', 'Read' \n: "
    
    ## Until one of the valid functions is typed it will continue asking them for a function
    valid_option = False
    while valid_option == False:
        selection = input(selection_phrase)
        
        for option in options:
            ## Handles Capitalization error, and normalizes the output
            if selection.lower() == option.lower():
                valid_option = True
                selection = option
                print(f"'{selection}' Selected")
            if selection not in options:
                selection_phrase = "Option You've Selected is either not in the expected list or not up to date, please try again\n: "

    return selection


def add_Note():
    with open("Notes.csv", newline="") as notes_File:
        reader = csv.DictReader(notes_File, delimiter=",")
        ## Opens Notes database file and creates a copy
        notes = list(reader)

    ## Iterating through this copy, it grabs all the titles of the notes and adds them to a list to check for duplicate titles
    titles = []
    for row in notes:
        titles.append(row["Title"])

    selection_phrase = "What is the title of the note you'd like to add?\n: "
    valid_option = False
    while valid_option == False:
        new_title = input(selection_phrase)
        
        if new_title in titles:
            selection_phrase = "That title is already the title of another note, if youd like to change that note, use the update feature, otherwise choose a new title\n: "
        else:
            valid_option = True

    message = input("What is the note you'd like to write?\n: ")

    ## Opens the Notes database file and adds a new row, with the new note
    with open("Notes.csv", "a", newline="") as notes_File:
        writer = csv.writer(notes_File, delimiter=',')
        writer.writerow([new_title, message])

    print(f"{new_title} : {message}")

    return


def print_Note():
    with open("Notes.csv", newline="") as notes_File:
        reader = csv.DictReader(notes_File, delimiter=",")
        ## Opens the Notes database file and makes a copy of it
        notes = list(reader)

    ## Iterating through this copy, it grabs all the titles of the notes and adds them to a list to validate user input with
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
                    ## Prints the Note with the matching name
                    if row["Title"] == selection:
                        print(row["Note"])

            if selection == "Cancel":
                return

            if selection not in title:
                selection_phrase = "Note youve selected doesnt share a name with a Note already in the list, please try again or type 'Cancel'\n: "

    return


def delete_Note():

    with open("Notes.csv", newline="") as notes_File:
        reader = csv.DictReader(notes_File, delimiter=",")
        ## Opens Notes database file and creates a copy
        notes = list(reader)

    ## Iterating through this copy, it grabs all the titles of the notes and adds them to a list to validate user input with
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
                    ## Removes the Note with the matching name from the copy
                    if row["Title"] == selection:
                        notes.remove(row)

            if selection == "Cancel":
                return
            
            if selection not in title:
                selection_phrase = "Note youve selected doesnt share a name with a Note already in the list, please try again or type 'Cancel'\n: "
            
    with open("Notes.csv", "w", newline="") as notes_File:
        writer = csv.DictWriter(notes_File, delimiter=",", fieldnames= ["Title", "Note"])
        writer.writeheader()
        ## Writes the copied and edited Notes database file over the original, now with the removed Note
        for row in notes:
            writer.writerow(row)
    
    return    


def update_Note():

    with open("Notes.csv", newline="") as notes_File:
        reader = csv.DictReader(notes_File, delimiter=",")
        ## Opens Notes database file and creates a copy
        notes = list(reader)
    
    ## Iterating through this copy, it grabs all the titles of the notes and adds them to a list to validate user input with
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
                    ## Updates the copy with whatever the user puts 
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
        ## Writes the copied and edited Notes database file over the original, now with the updated Note
        for row in notes:
            writer.writerow(row)

    return


def check_Done(finished):
    ## Very similar to the Get Action function, Initialize valid options, iterate until a valid option is chosen, then relay it back to the main function
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