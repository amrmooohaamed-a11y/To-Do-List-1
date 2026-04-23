import os
import datetime
import re
# function Clear Screen
def clearScreen():
    os.system("cls") if os.name == "nt" else os.system("clear")

# function Load User
def loadUser(fileName = "users.txt"):
    users = {} # قاموس لاضافة المستخدمين
    if os.path.exists(fileName): # التحقق من ان الملف موجود
        with open(fileName, "r") as file: # فتح الملف في وضع القرائه
            for line in file: # علي محتويات الملف التي تمت قرائتها loop 
                line = line.strip() # ازالت المسافات من محتوي القرائه
                if ":" in line: # التحقق من وجود هذه النقتان في النص
                    userName, password = line.split(":", 1) # لاخذ النصف الاول من النص وهو الاسم والثاني الباسوردuserName عمل متغيرين ال
                    users[userName.strip()] = password.strip()

    return users

# function Save Users 
def saveUsers(userName, password, fileName = "users.txt"):
    with open(fileName, "a") as file:
        file.write(f"{userName}:{password}\n")

# function sign Up
def signUp(users):
    userName = input("Write Your Name: ").strip().lower()
    password = input("Write Your Password: ").strip()

    if userName in users:
        print("❌ Username already exists, please choose another one")

    else:
        password_pattern = (
            r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)"
            r"(?=.*[@#$%^&*!])[A-Za-z\d@#$%^&*!]{8,}$"
        )

        if re.fullmatch(password_pattern, password):
            users[userName] = password
            saveUsers(userName, password)
            print("✅ You have been successfully added")
        else:
            print(
                "The password must contain:\n"
                "- At least one capital letter\n"
                "- At least one small letter\n"
                "- At least one number\n"
                "- At least one special character (!@#$%^&*)\n"
                "- Minimum length of 8 characters"
            )
            input("\nPress Enter to continue...")
        

# function logIn
def logIn(users):
    userName = input("User Name: ").strip().lower()
    password = input("Password: ").strip()

    tries = 3
    while tries > 0:
        if userName in users and users[userName] == password:
            print(f"👋 Hello {userName}, login successful!")
            return userName
        else:
            tries -= 1
            print(f"❌ Wrong credentials. You have {tries} attempts left.")
            if tries == 0:
                print("❌ You have used all attempts. Please sign up first.")
                return False
            
            userName = input("User Name: ").strip().lower()
            password = input("Password: ").strip()

# function Load Tasks 
def loadTasks(userName):    

    fileNameTasks  = f"{userName}_tasks.txt"
    tasks = []

    if not os.path.exists(fileNameTasks):
        with open(fileNameTasks, "w") as file:
            pass

    with open(fileNameTasks, "r") as file:
        for line in file:
            tasks.append(line.strip())
    
    return tasks, fileNameTasks

# function Save Tasks
def saveTasks(tasks, fileNameTasks):
    with open(fileNameTasks, "w") as file:
        for line in tasks:
            file.write(f"{line}\n")

# function Add Task
def addTask(tasks):
    newTask = input("Write The New Task: ").strip()
    if newTask == "":
        print("Sorry, I Need To Write Something important.")
        return
    else:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        tasks.append(f"{newTask} ({time})\n")
        print(f"\nYou Have {len(tasks)} Task(s).")

# function Tasks Viewing
def tasksViewing(tasks):
    print("#" * 50)
    print("########## Your Tasks ##########")
    print("#" * 50)

    if not tasks: 
        print("=>❌No tasks yet <=") 
        return
    for i, task in enumerate(tasks, start = 1): 
        print(f"{i}- {task}")
     

# function Edit Task
def editTask(tasks, fileNameTasks):

    tasksViewing(tasks)

    try:
        taskNumber = int(input("Write The Task Number: ").strip())
        if taskNumber < 1 or taskNumber > len(tasks):
            print("❌ Error: Task number out of range.") 
        else:
            index = taskNumber - 1
            tasks[index] = input("Write the task after editing: ").strip()
            saveTasks(tasks, fileNameTasks)
            print("\n✅ Task edited successfully!")
    except ValueError:
        print("❌ Please enter a valid number.")

# function Delete Task
def deleteTask(tasks, fileNameTasks):

    tasksViewing(tasks)
    try:
        deleteTaskNumber = int(input("Enter the task number you want to delete: ").strip())

        if deleteTaskNumber < 1 or deleteTaskNumber > len(tasks):
            print("❌ Error: Task number out of range.")
        
        else:
            index = deleteTaskNumber - 1
            tasks.pop(index)
            saveTasks(tasks, fileNameTasks)
            print("\n✅ The task was successfully deleted")
    except ValueError:
        print("❌ Please enter a valid number.")

users = loadUser()

while True:
    clearScreen()
    print("*******************************")
    print("********** Main Menu **********")
    print("*******************************")

    print("1- Sign Up.")
    print("2- Login.")
    print("3- Exit.")

    choice = input("Choose Between (1 or 2 or 3): ").strip()

    if choice == "1":
        clearScreen()
        signUp(users)

    elif choice == "2":
        clearScreen()
        userName = logIn(users)

        if userName:
            tasks, fileNameTasks = loadTasks(userName)

            while True:
                print("*******************************")
                print("********** Task Main **********")
                print("*******************************")

                print("1- Add Task.")
                print("2- View Task.")
                print("3- Edit Task.")
                print("4- Delete Task.")
                print("5- Logout.")

                choose = input("Choose Between (1 or 2 or 3 or 4 or 5): ").strip()

                if choose == "1":
                    clearScreen()
                    addTask(tasks)
                    saveTasks(tasks, fileNameTasks)
                    input("\nPress Enter to continue...")
                    clearScreen()

                elif choose == "2":
                    clearScreen()
                    tasksViewing(tasks)
                    input("\nPress Enter to continue...")
                    clearScreen()

                elif choose == "3":
                    clearScreen()
                    editTask(tasks, fileNameTasks)
                    input("\nPress Enter to continue...")
                    clearScreen()

                elif choose == "4":
                    clearScreen()
                    deleteTask(tasks, fileNameTasks)
                    input("\nPress Enter to continue...")
                    clearScreen()

                elif choose == "5":
                    clearScreen()
                    break

                else:
                    clearScreen()
                    print("******************")
                    print("❌ Invalid choice")
                    print("******************")
    elif choice == "3":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice")