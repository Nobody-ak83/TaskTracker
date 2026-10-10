from utils import *


def print_all_data():
    data = read_all_data()
    show(data)

def main():
    
    dir_of_commands={
        'read_all_data':print_all_data,
        'setTask': getTask,
        'read_done_tasks': read_done_tasks,
        'read_undone_tasks': read_undone_tasks,
        'read_inprogress_tasks': read_inprogress_tasks,
        'delete_task': delete_task
    }
    
    print('Hello! Enter command: ')
    
    while True:
        
        user_input=input(": ").strip()
        
        if user_input== 'exit':
            print("Bye")
            break
        
        if user_input in dir_of_commands:
            command_function= dir_of_commands[user_input]
            
            command_function()
            
        else:
            print('No such command.')
                
    
if __name__ == "__main__":
    main()       