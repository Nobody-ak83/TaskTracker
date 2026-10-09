import os
import json
from pprint import pprint



def setTask(user_task,status='todo'):
    new_task ={
    "id": 1,
    "description":user_task,
    "status": status
    }
    
    

def read_all_data(task_list):
    if not os.path.exists(json_path):
        return []
    
    for item in task_list:
        task_id=item.get("id")
        description=item.get("description")
        status=item.get("status")
        
        print(f'''
        id: {task_id}
        description: {description}
        status: {status}''')
        
    current_dir=os.path.dirname(os.path.abspath(__file__))
    json_path=os.path.join(current_dir, 'task_list.json')

    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data=json.load(file)
            
        read_all_data(data)
        
    except FileNotFoundError:
        print(f"File {file} not found")
    except json.JSONDecodeError:
        print('Uncurrect format of file. (Not json)')