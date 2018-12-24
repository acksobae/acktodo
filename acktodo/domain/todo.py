from acktodo.exc import *

class TodoItem(object):
    def __init__(self, desc):
        self.desc = desc
        self.is_checked = False
    
    def check(self):
        self.is_checked = True

    def toggle(self):
        self.is_checked = not self.is_checked

    def uncheck(self):
        self.is_checked = False

class TodoList(object):
    def __init__(self):
        self.count = 0
        self.items = {}

    def add(self, id, desc):
        if id in self.items:
            raise DuplicateEntryError()
        self.items[id] = TodoItem(desc)
        self.count += 1

    def remove(self, id):
        self.count -= 1
        self.items.pop(id)