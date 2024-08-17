#It is task management system. I used too many recursive methods for this program.
def init_tasks():
    return [
        {'id': 1, 'description': "Complete Project Proposal", 'assigned_to': "John Doe", "subtasks": [
            {'id': 2, 'description': "Research", 'assigned_to': "Alice Brown", 'time_estimate': 5},
            {'id': 3, 'description': "Outline", 'assigned_to': "Bob Johnson", 'subtasks': [
                {'id': 4, 'description': "Introduction", 'assigned_to': "Jane Smith", 'time_estimate': 3},
                {'id': 5, 'description': "Body", 'assigned_to': "Jane Smith", 'time_estimate': 6},
                {'id': 6, 'description': "Conclusion", 'assigned_to': "David Wilson", 'time_estimate': 2}
                ]}
        ]}]

def add_task_recursive(task_list): #it adds new task
    initialize = 0
    print("0. New Task")
    print_tasks(task_list,initialize)
    add_task = input("To add a new task, enter 0. To add a subtask, select the task ID: ")
    desc = input("Please enter the task description: ")
    resp = input("Please enter the task responsible: ")
    estimate = input("Please enter the estimated time for the task: ") 
    if add_task != "0":
        change(task_list,"id",add_task,desc,resp,estimate,1)
            
    else:
        task_list.insert(0,{"id":1, "description":desc, "assigned_to":resp,"time_estimate":int(estimate)})
        change(task_list,"id",0,desc,resp,estimate,5)

        
def print_tasks(task_list,initialize): #initialize used for count of "-" at the beggining of the each output lines
        ini = initialize
        for task in task_list:
            print(ini*2*"-" + str(task["id"]) + ". " + task["description"] + f"({task['assigned_to']})")
            if "subtasks" in task: #recursion
                print_tasks(task["subtasks"],ini+1)

def change(task_list,control_attribute,control_value,desc,resp,estimate,code):
    return_list = []
    recursion_time = 0 #it is for code == 3 (complete_task_recursively) and code == 1 (add_task_recursively)
    def change_task(task_list,control_attribute,control_value,desc,resp,estimate,code):
        nonlocal return_list, recursion_time
        for task in task_list:
            if task[control_attribute] == int(control_value):
                if code == 1: #code == 1 --> add_task_recursive
                    if "subtasks" not in task:
                        task["subtasks"] = []
                    task["subtasks"].insert(0,{"id":int(task["id"] +  1), "description":desc, "assigned_to":resp,"time_estimate":int(estimate)})
                    break
                elif code == 2: #code == 2 --> assign_task
                    task["assigned_to"] = resp
                    print(f"Task {task['description']} assigned to {resp}.\n")
                    break
                elif code == 3: #code == 3 --> complete_task_recursively
                    task["completed"] = True #add "completed" key
                    if recursion_time == 0:
                        print(f"Task '{task['description']}' marked as completed.\n")
                        recursion_time += 1
                    sub = task.get("subtasks",[])
                    if sub != []:
                        for i in sub:
                            control_value = i["id"]
                            change_task(sub,"id",control_value,0,0,0,3) #recursion
                    
            else:
                if "subtasks" in task: #recursion
                    change_task(task["subtasks"],control_attribute,control_value,desc,resp,estimate,code)
        
        current_id = -1
        def change_id(task_list): #since there could be same id when change tasks, it reorganises the tasks' id
            nonlocal current_id       
            for task in task_list:
                current_id += 1
                if task["id"] == current_id:
                    task["id"] += 1
                if "subtasks" in task:
                    change_id(task["subtasks"])
        if code == 1 or code == 5: #code == 1 --> add_task_recursive(when add_task != 0) , code == 5 --> add_task_recursive(when add_task == 0)
            if recursion_time == 0:
                print(f"{desc} is added.\n")
                recursion_time += 1
            change_id(task_list)
        return_list = task_list

    change_task(task_list,control_attribute,control_value,desc,resp,estimate,code)
    return return_list
    
def assign_task(task_list):#it assigns tasks
    print_tasks(task_list,0)
    task_no = input("Please select a task: ")
    name = input("Please enter the new team members name: ")
    change(task_list,"id",task_no,0,name,0,2)

def complete_task_recursive(task_list): #it completes tasks
    print_tasks(task_list,0)
    task_no = input("Enter task ID:")
    change(task_list,"id",task_no,0,0,0,3)
    
def generate_report_recursive(tasks):
    def report_recursive(task_list):
        total_time = 0
        remain_time = 0  
        for task in task_list:
            if "subtasks" in task:
                subtask_time, subtask_remain_time = report_recursive(task["subtasks"])
                total_time += subtask_time
                task["time_estimate"] = subtask_time 
                task["remain_time"] = subtask_remain_time #add "remain_time" key
                remain_time += subtask_remain_time
            else:
                task_time, task_remain_time = calculate_time_recursive(task)
                total_time += task_time
                task["time_estimate"] = task_time
                task["remain_time"] = task_remain_time #add "remain_time" key
                remain_time += task_remain_time

        return total_time, remain_time

    def calculate_time_recursive(task): #if completed == True then remain_time == 0
        completed = task.get("completed", False)
        time_estimate = task.get("time_estimate", 0)
        
        if completed:
            remain_time = 0
        else:
            remain_time = time_estimate

        return time_estimate, remain_time
    
    def print_report(task_list,initialize): #it prints the report
        ini = initialize
        for task in task_list:
            print(ini*2*"-" + str(task["id"]) + ". " + task["description"] + f"({task['assigned_to']}) -- Estimated Time to Finish: {task['remain_time']} out of {task['time_estimate']} ",end = "")
            if task["remain_time"] == 0:
                print("Completed")
            else:
                print("Pending")
            if "subtasks" in task:
                print_report(task["subtasks"],ini+1)

    report_recursive(tasks)
    print_report(tasks,0)
    calc_estimate = 0 #total time of project
    calc_remain = 0 #total remain time of project
    for task in tasks:
        calc_estimate += task["time_estimate"]
        calc_remain += task["remain_time"]
    print(f"The total time of the project is: {calc_estimate}\nThe remaining time of the tasks to finish the project is: {calc_remain}")


def main():  
    team_tasks = init_tasks()
    control_value = True
    while control_value:
        operation = input("Operations:\n1. Add a new task \n2. Assign a task to a team member \n3. Complete a task \n4. Generate report \n5. Exit\nPlease select an operation:")
        if operation == "1":
            add_task_recursive(team_tasks)
        elif operation == "2":
            assign_task(team_tasks)
        elif operation == "3":
            complete_task_recursive(team_tasks)
        elif operation == "4":
            generate_report_recursive(team_tasks)
        elif operation == "5":
            control_value = False
        else:
            print("Enter valid number")

        if control_value and (operation == "1" or operation == "2" or operation == "3" or operation == "4" or operation == "5"):
            inp = input("Please press enter to continue.\n")
            while inp != "":
                inp = input("Please press enter to continue.\n")
            
if __name__ == "__main__":
    main()