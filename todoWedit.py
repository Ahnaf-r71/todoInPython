print("Welcome to your task planner")
tasks=[]
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
    print("5. Exit \n")
    data=input()
    
    match data:
        case "1":
            task = input("Enter Task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully!")
            
        case "2":
            print("Tasks:")
            for get in tasks:
                print(get)
            
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
            print("Exiting...")
            break
            
        case _:
            print("Invalid Option!")
            
            
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in nums+1:
                if i+j==target:
                    return [nums.index(i),nums.index(j)]
                


store=[]
x=1221    
while x > 0:
    store=x%10
    