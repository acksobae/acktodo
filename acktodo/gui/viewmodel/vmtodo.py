from acktodo.gui.viewmodel.vmbase import *

class VMTodo(VMBase):
    def __init__(self, repository):
        self.todo_id = "-"
        self.repository = repository
    
    def add(self):
        self.repository.add(self.todo_id, self.todo_desc)
    
    def query(self):
        todo = self.repository.get(self.todo_id)
        self.todo_id = todo.id
        self.todo_desc = todo.desc

