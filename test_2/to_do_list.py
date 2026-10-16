todo = []



def options():
    print ("*****Menu*****")
    print("1. Add")
    print("2. view")
    print("3. Remove")
    print("4. Quit")





def add_task(tsk , lis):
    lis.append(tsk)



def view_tasks(tasks):
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]} ")


while True:

    options()
    user_choice = input("Enter user's choice: ").lower()
    if user_choice == "1" or user_choice == "add":
        task = input("Enter task: ")
        add_task(task, todo)
        print("Task added succesfully")

    elif user_choice == "2" or user_choice == "view":
        if not todo:
            print("Your todo list is empty guy!")
        else:
            view_tasks(todo)
    elif user_choice == "3" or user_choice == "remove":
        if not todo:
            print("You do not have any task to remove oo!")
        else:
            try:
                task_num = int(input("Enter task number: "))
                todo.pop(task_num - 1)
                print("Task removed succesfully.")
            except ValueError:
                print("Invalid input")
    elif user_choice == "4" or user_choice == "quit":
        print("You dey go na")
        break



