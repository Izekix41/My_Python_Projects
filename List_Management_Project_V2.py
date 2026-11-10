import json

class FileManager:
    def __init__(self, filename="inventory.json"):
        self.items = []
        self.filename = filename
        self.load_data()
        
    def add_items(self, item_name):
        item_name_clean = item_name.strip().lower()
        self.items.append(item_name_clean)
        
    def remove_items(self, item_name):
        item_name_clean2 = item_name.strip().lower()
        if item_name_clean2 in self.items:
            self.items.remove(item_name_clean2)
            print(f"successfully removed {item_name_clean2} from the list.")
        else:
            print("Item not found.")
            
    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.items, f)
            
    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                self.items = json.load(f)
        except FileNotFoundError:
            self.items = []
            
          
            
            
def main():
    Program_Startup = True
    while Program_Startup:
        print("---Program initialize?: (yes/no)---")
        P_Select = input("Enter here: ")
        P_SelectClean = P_Select.strip().lower()
                
        if P_SelectClean == "yes":
            Program_Run = True
            while Program_Run:
                print("-----------------------------[]\nWelcome to List Management V2 []\n-----------------------------[]")
                print("Would you like to start with a new list or you have one saved")
                print("1. New List \n2. Load Lists \n3. Return to program menu")
                selection = input("Enter here: ")
                if selection == "1":
                    filename = input("\n 1. Enter File name (e.g. inventory.json): ").strip() or "inventory.json"
                    manager = FileManager(filename)
                    manager.items = []   
                elif selection == "2":
                    filename = input("Enter File name to load: ").strip() or "inventory.json"
                    manager = FileManager(filename)
                    manager.load_data()
                elif selection == "3":
                    print("Returning back. . . ")
                    break
                else:
                        print("Invalid option, returning to start. . .")
                        continue
                        
                        
                Active_List = True
                while Active_List:
                    print(f"\n--- Current List = [{manager.filename}]: {manager.items} ---")
                    action = input("\nSelect: \n0.Add item \n1. Remove item \n2. Save & Exit \nEnter Here: ")
                    if action == "0":
                        item = input("Enter an Item to add: ")
                        manager.add_items(item)
                    elif action == "1":
                        item = input("Enter an Item to remove: ")
                        manager.remove_items(item)
                    elif action == "2":
                        manager.save_data()
                        print("Saved. . .Returning to the Main Menu. . .")
                        
                        
                        Active_List = False                 
                    else:
                        print("Command not found. Please try again.")
                        continue
                    
        elif P_SelectClean == "no":
            print("thank you for using the program.")
            break
        else:
            print("Not an option, please try again")
            
if __name__ == "__main__":
    main()
