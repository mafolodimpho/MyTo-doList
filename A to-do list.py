class MyToDoList:
    def __init__(self):
        self.tasks = []

    def input_task(self, task):
        self.tasks.append(task)
        print("Your task is now on the to-do list.")

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Your task has been deleted.")
        else:
            print("This task is not on the to-do list.")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("There are no tasks on the list. Get started.")

    def show_menu(self):
        print("\nHere is what you can do on this to-do list:")
        print("1. Input a Task")
        print("2. Delete a Task")
        print("3. View Tasks")
        print("4. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Select a number: ")

            if choice == '1':
                task = input("Input your task: ")
                self.input_task(task)
            elif choice == '2':
                task = input("Select the task which you wish to delete from the list: ")
                self.delete_task(task)
            elif choice == '3':
                self.view_tasks()
            elif choice == '4':
                print("You are now leaving your to-do list. Do visit again!")
                break
            else:
                print("We can't process your selection. Please select a number from 1 to 4.")


if __name__ == "__main__":
    todo_list = MyToDoList()
    todo_list.run()
