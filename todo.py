from pathlib import Path
import json
from datetime import datetime





All_tasks = []

try : 
    with open ('notes.txt', 'r', encoding='utf-8') as f :
        cont = f.read()
        if cont  :
            All_tasks = json.loads(cont)
        else : 
            pass    
except FileNotFoundError :
    pass 



def writeFile(filename : str, tasks : str) :
    with open (filename, 'w', encoding='utf-8') as f :
        f.write(json.dumps(tasks))



while(True) :
    print(" \n\n\nWelcome to todo by CLONNIEE\n")
    print("Choose task : " \
        "\n 1. Create a task. " \
        "\n 2. Read tasks. " \
        "\n 3. Delete a task. " \
        "\n 4. Update/check task status. "\
        "\n 5. exit \n")

    operation = int(input("Enter Your desired task number : "))

    match(operation):
        case 1 :            
            task_heading = input("Enter task heading : ")
            task_input = input("Write your task here : ")
            task_id = datetime.now()
            task_data = {
                # "id" : str(task_id),   not using it though
                "task-heading" : task_heading,
                "content" : task_input,
                "task-status" : False
            }

            All_tasks.append(task_data)
            writeFile('notes.txt',All_tasks)

            

            
        case 2 :  
            for key,tasks in enumerate(All_tasks):
                print(f"{key + 1}. {All_tasks[key]["task-heading"]}")

    
            user_asked = int(input("Select which task you waana read (Enter task number !) : "))
            print(f"Your task : {All_tasks[user_asked - 1]["content"]}") 
                
            
        case 3 : 
            print("Chose task number to delete :")
            for key,tasks in enumerate(All_tasks):
                print(f"{key + 1}. {All_tasks[key]["task-heading"]}   :   {All_tasks[key]["content"]}")

            user_input = int(input("Enter task Number : "))    
            del All_tasks[user_input-1]
            writeFile('notes.txt', All_tasks)

            
        case 4 : 
            for key,tasks in enumerate(All_tasks):
                print(f"{key + 1}. {All_tasks[key]["task-heading"]}  :  {tasks["task-status"]} ")

            usr_inpt = int(input("Enter task number to update : "))    
            All_tasks[usr_inpt - 1]["task-status"] = not All_tasks[usr_inpt - 1]["task-status"]
            writeFile('notes.txt', All_tasks)
        
        case 5 : 
            break
            
        case _:
            print("Invalid task ")

