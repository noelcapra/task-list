
task_list =[]

def show_list():
    print(task_list)

def add_list(task):
    task_list.append(task)
    print(task, "Has been added do your list")

def remove_list(task):
    if task in task_list:
        task_list.remove(task)
    else:
        print("That task does not exist in your list")

def clear_list():
    if input("Are you sure you want to clear your list? This can not be reverted (yes/no" ).lower() == "yes" or "y":
        task_list.clear()
    elif input("Are you sure you want to clear your list? This can not be reverted (yes/no" ).lower() == "no" or "n":
        print("Okay, list has not been cleared")
    else:
        print("Please answer with yes or no")




def ask_continue():
    response = input("Do you wish to make any other changes? (Yes/No)").lower()
    if response in ["yes", "y"]:
        return True
    if response in ["no", "n"]:
        return False
    else:
        print("Please answer with Yes or No")




while True:
    print("What do you want to do?")
    print("1. Show List")
    print("2. Add to list")
    print("3. Remove from list")
    print("4. Clear list")
    print("5. End")
    choices = ["1", "2", "3", "4","5"]

    choice_player = input("Please type the corresponding number:")

    if choice_player in choices:
        if choice_player == "1":
            show_list()
        elif choice_player == "2":
            add_list(input("What task do you want to add?"))
        elif choice_player == "3":
            remove_list(input("What task do you want to remove"))
        elif choice_player == "4":
            clear_list()

        elif choice_player == "5":
            print("Goodbye")
            break

        if not ask_continue():
            print("Goodbye")
            break


    else:
        print("Enter a valid number")
