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
