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
