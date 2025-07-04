Todo_list = []
def show_menu():
    print("\n********** TO-DO LIST MENU **********")
    print("1. To View Tasks")
    print("2. To Add Task")
    print("3. To Delete Task")
    print("4. To Exit")
    print("**************************************")
def viewing_tasks():
    if not Todo_list:
        print("\n📭 Your To-Do List is empty.")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(Todo_list, 1):
            print(f"{i}. {task}")
def adding_task():
    task = input("Enter a new task: ")
    Todo_list.append(task)
    print("✅ Task added successfully!")
def deleting_task():
    viewing_tasks()
    if Todo_list:
        try:
            index = int(input("Enter the task number to delete: "))
            if 1 <= index <= len(Todo_list):
                removed = Todo_list.pop(index - 1)
                print(f"🗑️ Task '{removed}' deleted.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")
while True:
    show_menu()
    user_choice = input("Enter your choice (1-4): ")
    if user_choice == '1':
        viewing_tasks()
    elif user_choice == '2':
        adding_task()
    elif user_choice == '3':
        deleting_task()
    elif user_choice == '4':
        print("👋 Exiting the To-Do List App.Byeeee!")
        break
    else:
        print("❌ Invalid option. Please try again later.")
