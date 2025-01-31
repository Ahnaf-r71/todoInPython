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
    # data=data.strip wont work with numbers  , will print <built-in method strip of str object at 0x00007FFD709ED6B0> Invalid Option!
    print(data)
    
    match data:
        case "1":
            task = input("Enter Task: ") + "\n" 
            
            file = open("files/todo.txt","r")
            tasks=file.readlines()
            file.close()
            tasks.append(task)
            print(f"Task '{task}' added successfully!")
            # file=open("todo.txt","w") #w for write r for read w for overwrite
            # file.writelines(tasks) #writting tasks to files but overwriting,prev one gone
            file=open("files/todo.txt","w") #w for write
            file.writelines(tasks)#writting tasks to files
            file.close()
            print("Select what to do next")
           
            #file.readlines returns array and file.read return string 
            
        case "2":
            print("Tasks:")
            # for manual with no files
            # for index,get in enumerate(tasks):
            #     index=index+1
            #     print(f"{index} - {get}") #or do print(index,"-",get)
            
            #with with context manager
            
            with open("files/todo.txt", "r") as file:
                tasks=file.readlines()#benefit is no need to close files
            
            #without with context manager
            # file = open("files/todo.txt", "r")
            # tasks=file.readlines()
            # file.close()
            
            new_todos = []
            for itemstrips in tasks:
                new_item = itemstrips.strip('\n')
                #new_item = [itemstrips.strip('\n') for itemstrips in tasks] #this is list COMPREHENSION
                new_todos.append(new_item)
            # for index,get in enumerate(tasks):
            for index,get in enumerate(new_todos):
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

#continue from f8-003v