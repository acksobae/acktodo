from acktodo.gui.viewmodel.vmbase import *

class VMTodo(VMBase):
    def __init__(self, todo_form, repository):
        self.todo_id = "-"
        self.form = todo_form
        self.repository = repository

    def get_current(self):
        self.todo_id = self.form.todo_id
        self.todo_desc = self.form.todo_desc

    def add_current(self):
        self.get_current()
        self.repository.add(self.todo_id, self.todo_desc)

