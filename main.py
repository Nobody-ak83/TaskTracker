import os
import json
from pprint import pprint

'''task_list=[]

user_text=input("What to do? \n")
'''



def setTask(user_task,status='todo'):
    new_task ={
    "id": 1,
    "description":user_task,
    "status": status
}

def read_data(task_list):
    for id, description, status in task_list:
        print(f'''
        id: {id}
        description: {description}
        status: {status}''')
        
        
        
current_dir=os.path.dirname(os.path.abspath(__file__))
json_path=os.path.join(current_dir, 'task_list.json')

try:
    with open(json_path, 'r', encoding='utf-8') as file:
        data=json.load(file)
        
    read_data(data)
    
except FileNotFoundError:
    print(f"File {file} not found")
except json.JSONDecodeError:
    print('Uncurrect format of file. (Not json)')
    
    
