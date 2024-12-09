# import builtins execute to get all available funtion list results
# print("Installation Test") 
# print("waiting for input...")
# user_text=input("Enter here:")
# print("user entered text "+"''"+user_text)
# test done

# prompt="Enter a todo:"
# todo1=input(prompt)
# todo2=input(prompt)
# todo3=input(prompt)
# todo4=input(prompt)

# todos=[todo1,todo2,todo3,todo4] #pylist 
# counts=len(todo1)
# print(counts)
# print(type(todos))
# print(todos)

user_prompt="Enter a task todo:"

password=input("Type your password:")

while password != "1234":
    print("Enter your correct !password")
print("Pass is correct")
todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo)
    print(todos)
    break

caps = []

while True:
    cap=input(user_prompt)
    print(cap.capitalize())
    caps.append(cap)
    break


# days =["Mon", "Tue", "Wed"]

# for i in days:
#     print(i.capitalize())
#     print("nice day".capitalize())


new_prompt = " Show or Add ?Type in here:"

while True:
    user_action= input(new_prompt)
    
    match user_action:
        case "show":
            print(todos)
            break
        case "add":
            new_todo = input(user_prompt)
            todos.append(new_todo)
            print(todos)
            break
        case "quit":
            print("Goodbye!")
            break
        case "capitalize":
            print(caps)
            break
        case _:
            print("Invalid command. Please try again.")
    
store=[]

while True:
    user_input=input("Please enter an option:")
    
    match user_input:
        case "addition":
            todos=input("Please enter a todo:")
            store.append(todos)
            
        case "showing":
            for nigga in store:
                print(nigga)
        case "quiting":
            break
        case _:
            print("Invalid command. Please try again.")

