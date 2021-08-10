# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Ethan Morgan, 08/09/2021, Added code to complete assignment 5
# ------------------------------------------------------------------------ #


# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"
objFile = ""   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "" # A variable for User Input at Step 4 for the Task
strPriority = "" # A variable for User Input at Step 4 for the Priority
strRemoveTask = "" # A variable for User Input to Remove a Task from the List in Step 5


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    objFile = open(strFile , "r")
    for row in objFile:
        strData = row.split(",")
        dicRow = {"Task" : strData[0] , "Priority" : strData[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
    print()
    print("There An Existing File, Data From File Is Saved To Memory")
except:
    print()
    print("No Available Existing File, List Will Start A New")
    print("Continue With The Menu Of Options")


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        try:
            print("Task -- Priority")
            print("=" * 30)
            for row in lstTable:
                print(row["Task"] + " -- " + row["Priority"])
        except:
            print("No Current Items In The List")
            print("Please Select Option 2 To Add Items To The List")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter A Task: ").strip()
        strPriority = input("Enter A Priority (High, Low): ").strip()
        if strPriority.lower() == "high" or strPriority.lower() == "low":
            dicRow = {"Task" : strTask , "Priority" : strPriority}
            lstTable.append(dicRow)
            print(strTask + " Has Been Added To The List")
        else:
            print("Please Enter Either 'High' or 'Low', '" + strPriority + "' Isn't A Valid Input")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemoveTask = input("Please Enter A Task To Remove: ").strip()
        Count = 1
        for row in lstTable:
            if row['Task'].lower() == strRemoveTask.lower():
                lstTable.remove(row)
                print(strRemoveTask + " Has Been Removed From The List")
                Count = Count + 1
        if Count == 1:
            print(strRemoveTask + " Is Not In The List")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile , "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("Data Is Saved To The Text File")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Thanks For Using The Program!")

        break  # and Exit the program