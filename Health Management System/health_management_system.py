import datetime # To save the log data with time
import os       # To create the log files with the user name and type
import json     # To save the given usernames as json format and reused.
class Healthmanager():
    filename = "names.json"

    def __init__(self, dictionary):
        self.i = 1
        self.clientDict = dictionary
        self.values = []
        self.readNames()
        if len(self.clientDict) == 0:
            self.assignNames()

    def initial(self):
        print("------------------------")
        try:
            self.showNames()
            print("------------------------")
            name = input("Your option : ")
            name = self.clientDict.get(name)
            print("------------------------")
            print(f"*** Initializing for \"{name}\" ***")
            print(f"1 for log")
            print(f"2 for retrieve")
            print("------------------------")
            option = input("Enter your option : ")
            print("------------------------")

            if option == "1":
                option = "log"
            elif option == "2":
                option = "retrive"
            else:
                main()

            print(f"What you want to {option}.\n1 for Diet\n2 for exercise")
            print("------------------------")
            a = input("Choose your option : ")
            print("------------------------")

            if a == "1":
                fileEx = "food"
            elif a == "2":
                fileEx = "exec"
            else:
                main()

            if option == "log":
                storevalue = input("Type Here :\n")
                self.log(name, storevalue, fileEx)
            else:
                self.retrieve(name, fileEx)

        except Exception as e:
            print("Invalid Value!")

    def updateValuesOfDict(self):
        for value in self.clientDict.values():
            self.values.append(value.lower())

    def log(self, name, storevalue, fileEx):
        for value in self.clientDict.values():
            if name == value:
                with open(f"{name.lower()}-{fileEx}.log", "a") as f:
                    f.write(f"[{self.getDate()}] {storevalue}\n")
        print(f"Successfully saved data of {name}")

    def retrieve(self, name, fileEx):
        with open(f"{name.lower()}-{fileEx}.log") as f:
            content = f.read()
            print(content)

    def readNames(self):
        if os.path.exists(self.filename):
            with open(self.filename) as f:
                jsonData = f.read()
                nameDict = json.loads(jsonData)
                self.clientDict = nameDict
                # print(self.clientDict)
                for value in self.clientDict.values():
                    self.values.append(value.lower())

                keys = []
                if len(self.clientDict) != 0:
                    for key in self.clientDict.keys():
                        keys.append(int(key))
                    i1 = max(keys)
                    i1 += 1
                else:
                    i1 = 1
                # print(i)
                self.i = i1
                print(self.i)

    def assignNames(self):
        print("---Assigning names---")
        print("Enter \"q\" to exit")
        while True:
            name = input("Enter the name : ")
            if name.lower() == "q":
                break

            if name.lower() not in self.values:
                self.clientDict[self.i] = name
                self.i += 1
                self.values.append(name.lower())
                print(f"Successfully assigned the name : {name}")
            else:
                print(
                    f"\"{name}\" is already present in the names data .Please choose a unique name.")
        # print(self.clientDict)
        self.saveNames()

    def saveNames(self):
        try:
            names = json.dumps(self.clientDict, indent=3)
            with open(self.filename, "w") as f:
                f.write(names)
        except Exception as e:
            print(e)

    def showNames(self):
        for key, value in self.clientDict.items():
            print(f"{key}. {value}")

    def updateDict(self):
        self.showNames()
        updateDict = {}
        print("Update the name in srl no. ")
        print("Enter \"q\" to stop.")
        while True:
            keyinput = input("Enter the key / srl no. : ")
            if keyinput == "q":
                break
            valueinput = input("Enter the new name : ")
            if valueinput == "q":
                break
            if valueinput.lower() not in self.values:
                updateDict[keyinput] = valueinput
                print("Successfully updated")
                self.updateValuesOfDict()
                self.clientDict.update(updateDict)
                self.saveNames()
            else:
                print(f"\"{valueinput}\" is already present in the names data. Please Enter a unique name.")
            
    def removeName(self):
        self.showNames()
        res = input("\n Enter the no. of name you want to delete : ")
        try:
            self.clientDict.pop(res)
            print(
                f"The {self.clientDict.get(int(res))} of srl. {res} is successfully deleted.")
            self.saveNames()
        except ValueError:
            print("Invalid Value! Please Enter the srl no.")

    def deleteAllNames(self):
        confirm = input("Do you really want to delete all names data (y/n) : ")
        if confirm == "y":
            print("All names data has been deleted!")
            self.clientDict = {}
            self.saveNames()
            print("Please insert some names to run the program.")
            self.assignNames()
        else:
            print("Thank you for your confirmation. Your data is saved!")

    @staticmethod
    def getDate():
        return datetime.datetime.now()


if __name__ == "__main__":
    #Change the directory to this folder
    path = os.path.join(os.getcwd(), "Health Management System")
    if os.getcwd() != path:
        os.chdir(path)
        
    clientDict = {}
    newHm = Healthmanager(clientDict)
    commands = ''' ************************ Health Management System ************************
            Commands: (Type the words or "srl"[such. 1 , 2, 3] for a command)
            srl|---- commands ---------| ---------------work-------------------
            1. | get names            :| Get the saved names
            2. | assign Names         :| Assign names in the dictionary
            3. | update names         :| To update names or insert names data
            4. | log & retrieve       :| To log or retrieve the data of a person
            5. | remove name          :| To remove any name
            6. | del all data         :| To delete all names
            7. | exit or quit or q    :| To exit the software
            8. | help or show commands:| To show the command interface again
        '''
    print(commands)
    while True:
        userinput = input("Enter the command : ")
        if userinput.lower() == "get names" or userinput == "1":
            newHm.showNames()
        elif userinput.lower() == "assign names" or userinput == "2":
            newHm.assignNames()
        elif userinput.lower() == "log & retrive" or userinput == "3":
            newHm.updateDict()
        elif userinput.lower() == "log & retrive" or userinput == "4":
            newHm.initial()
        elif userinput.lower() == "remove name" or userinput == "5":
            newHm.removeName()
        elif userinput.lower() == "del data" or userinput == "6":
            newHm.deleteAllNames()
        elif userinput.lower() == "exit" or userinput.lower() == "quit" or userinput.lower() == "q" or userinput == "7":
            print("Thanks for using these software!")
            input("Press Enter to exit ")
            exit()
        elif userinput.lower() == "help" or userinput.lower() == "show command" or userinput == "8":
            print(commands)
        else:
            print("***Invalid Keyword!***")
            print(commands)
