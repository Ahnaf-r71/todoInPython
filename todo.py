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

import sys
from unittest import TestCase
import re

class Evaluate(TestCase):
    def test_exercise(self):
        expected_output = "0-Document.txt\n1-Report.txt\n2-Presentation.txt"
        filenames = ['document', 'report', 'presentation']
        
        import exercise
        user_output = sys.stdout.getvalue().strip()
        
        self.check_print()
        self.check_output(expected_output, user_output)
    
    def check_print(self):
        with open("exercise.py") as file:
            content = file.read()
        check1 = re.compile("print\(.*").search(content)  # check for print statement
        
        forgot_message = "It looks like there is no print() function in your code. Did you forget to print out the output?"
        
        if check1:
            pass
        else:
            sys.exit(forgot_message)
            
    def check_output(self, expected_output, user_output):
        message_output = f"\n\nYour code printed {user_output}, but the expected output is {expected_output}. Please check again!"
        if user_output == expected_output:
            pass
        else:
            sys.exit(message_output)