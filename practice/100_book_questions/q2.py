# A Todo List Application
class todo_list:
    def __init__(self, tasks, completed_tasks):
        self.tasks = tasks
        self.completed_tasks = completed_tasks

    def add_item(tasks):
        tasks = []
        new_task = input("Enter The New Task Name : ")
        tasks.append(new_task)

        print(tasks)

    def complete_task(items, completed_tasks, tasks):
        new_completed_task = input("Enter The Task Name You Have Completed : ")
        completed_tasks.append(new_completed_task)

        print(tasks)

    def show_tasks(tasks):
        return tasks

    def remove_task(tasks):
        remove_task = input("Enter The Task To Remove : ")
        tasks.remove = remove_task

        print(tasks)

item_1 = todo_list.show_tasks()
