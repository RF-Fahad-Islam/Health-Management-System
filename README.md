# Health Management System

Health Management System is a menu-driven (Not a GUI) python program that helps you to manage your **diet and exercise records** on a **`.log`** file along with a specific `date and time and name`. It's maybe helpful for **Logging** your activities data. It's manages and named the log files as the person name and creates every log file (that needed) automatically along with the users name and also saved the names data on a ```{names.json}``` file.
## How it works
It is developed using ```Classes and Objects```. A class named Health manager used to manage all the things of the program. You can change the class functions for developing or adding new features for the guaranteed **pull requests**. Some Built-in modules used that given below


## Packages or Modules

**Note: No external packages used in this program**

### Built-in Modules

**Some Built-in modules used on this program Such as ```[datetime, os, json]```**
```
# Module name ---- # Why used

import datetime # To save the log data with time
import os       # To create the log files with the user name and type
import json     # To save the given usernames as .JSON format.
```

## Usage
You can get some command to manage such as : 
```{Assign names, Get names, log & retrieve , update names, remove name and delete all data }```

```python
1. Log everyday activities on a .log file with date and time
2. Retrieve the data when you need it.
3. Add as many names as you want for logging on different files
4. Delete names whose you want to remove
5. Update and access names with their given unique (int) keys
6. You don't need to worry about the names data and files. it's 
   managed all data using a JSON file
```
## Overview
**Here is an overview of the program when runs. It will show an interface  on the Python Interpreter described as below and took  input from the user.**
```
First: # Shows it first to assign names for start

---Assigning names---
Enter "q" to exit    
> Enter the name :
```

```
Then: # Then Shows the command palate.

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

> Enter the command :  
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Versions 
**Note : This is developed in the ```<PYTHON-3.9> (Version)``` Environment**

## License
[MIT](https://choosealicense.com/licenses/mit/) **[Made by Fahad]**

## Thanks for visiting
**Please help to improve the project further.**
