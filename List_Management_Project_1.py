Your_List = []
program = True
while program:
    Intro = input("Start Program?: (yes/no)")
    Intro_clean = Intro.strip().lower()
    if Intro_clean == "yes":
        User_Program = True
        while User_Program:
            print(" ")
            print(" ")
            print(f"Your current list {Your_List}")
            print(" ")
            print(" ")
            selection = input("""Select:\n[add (type 0)]\n[remove (type 1)]\n[end (type 2)] """)
            print(f"Your list {Your_List}")
            if selection == "0":
                add_input = input("Enter your list: ")
                add_input_clean = add_input.strip().lower()
                Your_List.append(add_input_clean)
            elif selection == "1":
                select = input("Select word to remove: ")
                select_clean = select.strip().lower()
                if select_clean in Your_list:
                    Your_List.remove(select)
                else:
                    print(f"Could not find the word\"{select_clean}\"")
            elif selection == "2":
                print(" ")
                print(" ")
                print("List Selection ended!")
                print(f"List preview: {Your_List}")
                break
            else:
                print("wrong command please try again.")
            
    elif Intro_clean == "no":
        print("Program ends, Goodbye")
        break
    else:
        print("Unknown answer please try again")
    
            
            
    
