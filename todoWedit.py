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
        case _ if "1" in data or "add" in data:     #previously case "1": // if "1" or "add" in data: // case"1"|"add" in data
            task = input("Enter Task To add: ") + "\n" 
            
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
            # for testing [4:7] etc etc
            # testcase=input("give me a data to splice up a bit")
            # testResults=testcase[4:]
            # print(testResults)

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
            #alternative: new_todos=[tasks.strip]
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
            # for view in tasks:   #this one is in case of manually read and show existing tasks
            #     count=count+1
            #     print(f"{count}.{view}")
            # count=0
            # number=int(input("Enter the number of the task you want to edit"))
            # number=number-1
            # newtodo=input() #same as line 94
            # tasks[number]=newtodo #for replacing without txt file
            with open("files/todo.txt", "r") as file:
                tasks=file.readlines()
            tempstore=[]
            
            for scan in tasks:
                new_item=scan.strip('\n')
                tempstore.append(new_item)
            for index,get in enumerate(tempstore):
                index=index+1
                print(f"{index} - {get}")
            # num=input("Select The no in besides taks to edit")   
            
            
            # print("Stored Tasks:",tasks) #will print array instead of normal tasks
            
            num=int(input("Enter task no"+'\n'))
            num=num-1 #this one rewrites
            newtodo=input("Enter new task"+'\n')

            tasks[num]=newtodo+'\n'
            
            
            with open("files/todo.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task {newtodo} updated successfully!")
            
            
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
            # for serial,value in enumerate(tasks):
            #     serial=serial+1
            #     print(f"{serial}. {value}")
            with open("files/todo.txt",'r') as file:
                tasks = file.readlines()
                
            tempstore=[itemstrip.strip("\n") for itemstrip in tasks]
            for index,get in enumerate(tempstore):
                index=index+1
                print(f"{index} - {get}")
            
            comp=int(input("Select task no to be marked as completed"))
            completed_task=tasks[comp-1]
            tasks.pop(comp-1)
            
            with open("files/todo.txt",'w') as file:
                file.writelines(tasks)
                
            print(f"Task {completed_task} completed")
                
            
        case _:
            print("Invalid Option!")
        
        
print(tasks.sort())

#continue from f10-003v