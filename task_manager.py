''' the problem = "Task Management System" to design a system that allows users to 
add, view, and prioritize tasks. Tasks can have due dates, priorities, & descriptions. 
algorithmic thinking for this system follows: 1. Initialization; create an empty list 
to store tasks. Display a menu with options for the user. 2. Add a task; take user 
input for task details(descrip., due date, priority). Create a task object. Add 
task to list. 3. View Tasks; Display a list of tasks with their details. Allow 
sorting based on priority or due date. 4. Prioritize Tasks; Allow user to mark 
tasks as hi, med, or low priority 5. Allow user to exit program

flowchart: Start Program --> Initialize Task List --> Display Menu --> User chooses option
--> Take User input for task details --> Create Task & add to task list 
--> Repeat or Exit --> end program

#Step 1: Initialization
task_list = []

#Step 2: Add a task
def add_task():
    description = input('Enter task description: ')
    due_date = input('Enter due date: ')
    priority = input('Enter priority (high/medium/low): ')

    task = {
        'description': description,
        'due_date': due_date,
        'priority': priority
    }

    task_list.append(task)
    print('Task added successfully!')

#Step 3: view tasks
def view_tasks():
    # display a list of tasks with details
    # allow sorting based on priority or due date
    # (detailed implementaion depends on specific requirements)
    pass

#Step 4: prioritize tasks
def prioritize_tasks():
    # allow user to mark task as high, medium, or low priority
    # update the priority of the tasks accordingly
    # (detailed implementaion depends on specific requirements)
    pass

#Step 5: Exit 
def exit_program():
    # additional cleanup or save data if needed

# Main program loop
    while True:
        #Display menu
        print('1. Add a task')
        print('2. View task')
        print('3. Prioritize task')
        print('4. Exit')

        # user input for menu option
        choice = input('Enter your choice: ')

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice =='3':
        prioritize_tasks():
    elif coice == '4':
        exit_program()
        break
    else:
        print('Invalid choice. Please try again.')
'''


