# AlcoProjekt

 Search for a Task

Recursion can help search for a specific task by name.

def find_task(tasks, task_name):
    if task_name in tasks:
        return tasks[task_name]
    for task, details in tasks.items():
        found = find_task(details["subtasks"], task_name)
        if found:
            return found
    return None
