print("Welcome to your task planner")
tasks=[]
compTasks=[]
inputPass = input("Enter Your Password: ")
count = 0

while inputPass!= "1234":
    print("Invalid Password, Try Again!")
    inputPass = input("Enter Your Password: ")
    
while True:
    print("\nChoose a number option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Edit Task")
    print("5. Clear All")
    print("6. sort")
    print("7. Mark Complete")
    print("8. Exit \n")
    
    data=input()
    
    match data:
        case "1":
            task = input("Enter Task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully!")
            print("Select what to do next")
            
        case "2":
            print("Tasks:")
            for index,get in enumerate(tasks):
                index=index+1
                print(f"{index} - {get}") #or do print(index,"-",get)
            
        case "3":
            task = input("Enter Task to Delete: ")
            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' deleted successfully!")
            else:
                print(f"Task '{task}' not found!")
        
        case '4':
            for view in tasks:
                count=count+1
                print(f"{count}.{view}")
            count=0
            number=int(input("Enter the number of the task you want to edit"))
            number=number-1
            newtodo=input()
            tasks[number]=newtodo
            
        case "5":
            tasks.clear()
            print("All tasks cleared!")   
            
            
        case "8":
            print("Exiting...")
            break
        case "6":
            tasks.sort()
            print(tasks,"Tasks sorted successfully!")
        
        case "7":
            for serial,value in enumerate(tasks):
                serial=serial+1
                print(f"{serial}. {value}")
            comp=int(input("Select task to be marked as completed"))
            compTasks.append(tasks.pop(comp-1))
            for index,val in enumerate(compTasks):
                index=index+1
                print(f"Task '{index}'-{val} marked as completed!")
            
        case _:
            print("Invalid Option!")

print(tasks.sort())