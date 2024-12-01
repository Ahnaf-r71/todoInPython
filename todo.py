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
    exit