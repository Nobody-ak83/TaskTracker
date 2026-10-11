import os
import json


dir_of_commands=[
        'readall',
        'settask',
        'read_done',
        'read_undone',
        'read_inprogress',
        'deletetask',
        'info',
        'setnewstatus',
        'updatetask'
    ]

DATA_FILE='task_list.json'

current_dir=os.path.dirname(os.path.abspath(__file__))
json_path=os.path.join(current_dir, 'task_list.json')



def read_all_data():
    "Читает JSON-файл и возвращает данные (словарь/список)."
     
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    
    except FileNotFoundError:
        print(f"File from {json_path} not found")
        return {}
    
    except json.JSONDecodeError:
        print("Not JSON-file")
        return {}  



def setTask(user_task, status):
    tasks_list=read_all_data()
    
    if tasks_list:
        new_id=tasks_list[-1]['id']+1
    else:
        new_id=1
    
    new_task ={
        "id": new_id,
        "description": user_task,
        "status": status
    }
    
    tasks_list.append(new_task)
    
    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(tasks_list,file, ensure_ascii=False, indent=4)
        
        print('Task has been set')
        return new_task

def setNewStatus():
    user_task=input("Enter task: ").strip()
    newstatus=input("Enter new status: ").strip()
    tasks_list=read_all_data()
    was_updated=False
    
    for item in tasks_list:
        if item.get('description')==user_task:
            item['status']=newstatus
            was_updated=True
            break
    
    if was_updated:
        with open(json_path,'w',encoding='utf-8') as file:
            json.dump(tasks_list,file,ensure_ascii=False, indent=4)
            print("Status has been set")
        
    else:
        print('No such task found')
        
        
def UpdateTask():
    user_task_id=input("Enter task's id to update: ").strip()
    
    while not user_task_id:
        user_task_id=input("Task's id can't be empty: ").strip()
        
    user_task_id=int(user_task_id)
        
    user_task_newdescription=input("New description: ").strip()
    
    while not user_task_newdescription:
        user_task_newdescription=input("New description can't be empty: ").strip()
        
    records=read_all_data()
    was_updated=False
    
    for item in records:
        if item.get('id')==user_task_id:
            item['description']=user_task_newdescription
            was_updated=True
            break
    
    if was_updated:
        with open(json_path,'w',encoding='utf-8') as file:
            json.dump(records,file,ensure_ascii=False, indent=4)
            print('New description has been set')   
    else:
        print(f"Task with ID {user_task_id} not found.")  
    
 
    
def getTask():
    user_task=input("Enter task: ").strip()
    
    while not user_task:
        user_task=input("Task can't be empty.Enter task: ").strip()
    
    status=input("Enter status: ").strip()
    if not status:
        status='todo'
        
    return setTask(user_task,status)



def read_done_tasks():
    result_list=[]
    records = read_all_data() 
    
    for item in records:
        if item.get('status') == 'done':
            result_list.append(item)
        
    if result_list==[]:
        print('No such task.')
                
    return show(result_list)
            
            
            
            
def read_undone_tasks():
    result_list=[]
    records=read_all_data()
    for item in records:
        if item.get('status') != 'done':
            result_list.append(item)
                
    return show(result_list)
            
            
            
def read_inprogress_tasks():
    result_list=[]
    records = read_all_data()
    
    for item in records:
        if item.get('status') == 'in-progress':
            result_list.append(item)
                
    return show(result_list)
            

def delete_task():
    task=input("Name of task to delete: ").strip()
    records=read_all_data()
    
    updated_records=[item for item in records if item.get('description')!=task]
    
    if len(records)==len(updated_records):
        print('No such task.')
        return
    
    for index, item in enumerate(updated_records,start=1):
        item['id']=index
    
    with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(updated_records,file, ensure_ascii=False, indent=4)
            print("Task has been deleted.")
            


def show(arg):
    for k in arg:
        print(f'[{k.get('status')}] ID: {k.get('id')} | {k.get('description')}.')
        

def print_all_data():
    data = read_all_data()
    show(data)
    
    
def print_info():
    for k in dir_of_commands:
        print(f'{k}\n')