from utils import *




def main():
    
    dir_of_commands={
        'readall':print_all_data,
        'settask': getTask,
        'read_done': read_done_tasks,
        'read_undone': read_undone_tasks,
        'read_inprogress': read_inprogress_tasks,
        'deletetask': delete_task,
        'info': print_info,
        'setnewstatus': setNewStatus,
        'updatetask': UpdateTask
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