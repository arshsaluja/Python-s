"""
Simple task list.
"""

def new(tasklist, task):
    """Add new task"""
    tasklist.append(task)
def remove_by_num(tasklist, tasknum):
    """Remove by number"""
    if tasknum > 0 and tasknum <= len(tasklist):
        tasklist.pop(tasknum - 1)
def remove_by_name(tasklist, taskname):
    """Remove by name"""
    if taskname in tasklist:
        tasklist.remove(taskname)
def printlist(tasklist):
    """Print task list"""
    print("========================")
    num = 1
    for task in tasklist:
        print(num, task)
        num += 1
    print("========================")
def run():
    """Manipulate task list"""
    tasks = []
    new(tasks, 'Teach Class')
    printlist(tasks)
    
    new(tasks, 'Buy some ties')
    new(tasks, 'Learn Python')
    printlist(tasks)
    
    new(tasks, 'Build new task list')
    printlist(tasks)
    
    remove_by_num(tasks, 1)
    printlist(tasks)
    remove_by_num(tasks, 2)
    printlist(tasks)
    
    remove_by_name(tasks, 'Buy some ties')
    printlist(tasks)

run()
