from acktodo.exc import *

class ITodoList(object):
    def add(self, id, desc): raise NotImplementedError
    def add_param(self, id): raise NotImplementedError
    def remove(self, id): raise NotImplementedError
    def is_checked(self, id): raise NotImplementedError

class TodoItem(object):
    def __init__(self, desc):
        self.desc = desc
        self.is_checked = False
        self.params = {"note": "This is a comment."}
    
    def check(self):
        self.is_checked = True

    def toggle(self):
        self.is_checked = not self.is_checked

    def uncheck(self):
        self.is_checked = False

class TodoList(ITodoList):
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

    def is_checked(self, id):
        return self.items[id].is_checked

    def add_param(self, id):
        pass