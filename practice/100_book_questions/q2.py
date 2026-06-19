# A Todo List Application
class Todolist:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_item(self):
        new_task = input("Enter The New Task Name : ")
        self.tasks.append(new_task)

    def complete_task(self):
        new_completed_task = input("Enter The Task Name You Have Completed : ")
        self.completed_tasks.append(new_completed_task)
        self.tasks.remove(new_completed_task)

    def remove_task(self):
        remove_task = input("Enter The Task To Remove : ")
        self.tasks.remove(remove_task)

    def show_tasks(self):
        return self.tasks

my_list = Todolist()

my_list.add_item()  
my_list.add_item()  
my_list.complete_task()
result = my_list.show_tasks()
print(result)