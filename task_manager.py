"""
Task Management App - Work Flow

1 - Show menu

- Add task
- View task
- Update task
- Delete task
- Exit

2 - Input from user ( choose an option 1-5)

3 - Proces (According to user choice)

if choice == 1 -> Add a new task
if choice == 2 -> View all tasks
if choice == 3 -> Update a task
if choice == 4 -> Delete a task
if choice == 5 -> Exit the app

4 - Operations Details

Case - 1 (Add task) :

- Take task input from user
- Add task to the task list
- Show success message

Case - 2 (View task) :

- If task list is empty -> Show "No task availabe."
- Else -> Show all tasks with numbers

Case - 3 (Update task) :

- Show all task
- Take task number to update
- Take new task input
- Update the task
- Show success or error message

Case - 4 (Delete task) :

- Show all task
- Take task number to delete
- Delete the task
- Show success or error message

Case - 5 (Exit) :

- Show thank you messaeg and exit the app


5 - Loop back to Menu (except when exit is choosen)

6 - End

"""


def task():
    tasks = []  # empty list
    print("---Welcome To Task Management App---")

    total_task = int(input("Enter how many task you want to add = "))

    for i in range(1, total_task + 1):
        task_name = input("Enter task {i} = ")  # enter task 2 =
        tasks.append(task_name)

    print(f"Today's tasks are\n {tasks}")

    while True:
        operation = int(
            input("Enter 1- Add\n 2- Update\n 3- Delete\n 4- View\n 5- Exit/Stop/")
        )

        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)

            print(f"Task {add} has been successfully added....")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = int("Enter new task = ")
                ind = tasks.index(updated_val)
                task[ind] = up

                print(f"Updated yask {up}")

        elif operation == 3:
            del_val = input("Enter task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]

                print(f"Task {del_val} has been deleted....")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print(f"Closing the program....")

            break

        else:
            print("Invalid Input")


task()
