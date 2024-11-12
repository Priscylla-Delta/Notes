import csv


## Loops Through the functionality of the Notes Application until the user is finished
def main():
    finished = False
    while finished == False:
        ## Requests which valid action the user would like to do
        action = get_Action()

        if action == "add":
            add_Note()
        if action == "read":
            print_Note()
        if action == "delete":
            delete_Note()
        if action == "update":
            update_Note()
    
        ## Every Loop the user is asked if they are done using the app, if not it loops
        finished = check_Done(finished)


def get_Action():
    options = ["Add", "Update", "Delete", "Read"]
    default_Question = "Select from the available options Below \n'Add', 'Update', 'Delete', 'Read' \n: "
    failure_Question = "Option You've Selected is either not in the expected list or not up to date, please try again\n: "

    validated_input = get_valid_input(options, default_Question, failure_Question)
    print(f"'{validated_input}' Selected")

    return validated_input.lower()      


def add_Note():
    with open("Notes.csv", newline="") as notes_File:
        reader = csv.DictReader(notes_File, delimiter=",")
        notes = list(reader)

    titles = []
    for row in notes:
        titles.append(row["Title"])

    default_Question = "What is the title of the note you'd like to add?\n: "
    failure_Question = "That title is already the title of another note, if youd like to change that note, use the update feature, otherwise choose a new title\n: "
    title = get_valid_input(titles, default_Question, failure_Question, prevent_duplicate=True)

    message = input("What would you like the note to be?\n: ")

    with open("Notes.csv", "a", newline="") as notes_File:
        writer = csv.writer(notes_File, delimiter=',')
        writer.writerow([title, message])

    print(f"{title} : {message}")

    return


def print_Note():
    with open("Notes.csv", newline="") as notes_File:
        reader = csv.DictReader(notes_File, delimiter=",")
        notes = list(reader)

    options = []
    for row in notes:
        options.append(row["Title"])
        
    default_Question = f"Select from the available notes below.\n{options}\n"
    failure_Question = "Note youve selected doesnt share a name with a Note already in the list, please try again or type 'Cancel'\n: "
    validated_input = get_valid_input(options, default_Question, failure_Question)

    if validated_input == "Cancel":
            return

    for row in notes:
        if row["Title"].lower() == validated_input.lower():
            print(row["Note"])
    
    return 


def delete_Note():
    with open("Notes.csv", newline="") as notes_File:
        reader = csv.DictReader(notes_File, delimiter=",")
        notes = list(reader)

    options = []
    for row in notes:
        options.append(row["Title"])
        
    default_Question = f"Select from the available notes below.\n{options}\n"
    failure_Question = "Note youve selected doesnt share a name with a Note already in the list, please try again or type 'Cancel'\n: "
    validated_input = get_valid_input(options, default_Question, failure_Question)

    if validated_input == "Cancel":
        return

    for row in notes:
        ## Removes the Note with the matching name from the copy
        if row["Title"] == validated_input:
            notes.remove(row)

    with open("Notes.csv", "w", newline="") as notes_File:
        writer = csv.DictWriter(notes_File, delimiter=",", fieldnames= ["Title", "Note"])
        writer.writeheader()
        ## Writes the copied and edited Notes database file over the original, now with the removed Note
        for row in notes:
            writer.writerow(row)
    
    print(f"'{validated_input}' deleted")

    return        


def update_Note():
    with open("Notes.csv", newline="") as notes_File:
        reader = csv.DictReader(notes_File, delimiter=",")
        notes = list(reader)
    
    options = []
    for row in notes:
        options.append(row["Title"])
        
    default_Question = f"Select from the available notes below.\n{options}\n"
    failure_Question = "Note youve selected doesnt share a name with a Note already in the list, please try again or type 'Cancel'\n: "
    validated_input = get_valid_input(options, default_Question, failure_Question)   

    if validated_input == "Cancel":
        return

    for row in notes:
        if row["Title"] == validated_input:
            print(row["Note"])
            new_note = input("What would you like the new note to be?\n: ")
            row["Note"] = new_note

    with open("Notes.csv", "w", newline="") as notes_File:
        writer = csv.DictWriter(notes_File, delimiter=",", fieldnames= ["Title", "Note"])
        writer.writeheader()
        for row in notes:
            writer.writerow(row)

    return


def check_Done(finished):
    options = ["Yes", "Y", "No", "N"]
    default_Question = "Are you Finished? ('Yes', 'Y', 'No', 'N')\n: "
    failure_Question = default_Question
    validated_input = get_valid_input(options, default_Question, failure_Question) 

    if validated_input == "Yes" or validated_input == "Y":
        finished = True
    
    return finished


def get_valid_input(options, default_Question, failure_Question, prevent_duplicate=False):
    input_phrase = default_Question
    while True:
        unvalidated_input = input(input_phrase)
        
        if prevent_duplicate == True:
            if unvalidated_input.lower() in [option.lower() for option in options]:
                input_phrase = failure_Question
            else:
                validated_input = unvalidated_input
                return validated_input
        else:
            if unvalidated_input.lower() not in [option.lower() for option in options]:
                input_phrase = failure_Question
            else:
                for option in options:
                    if unvalidated_input.lower() == option.lower():
                        validated_input = option
                        return validated_input
                

main()