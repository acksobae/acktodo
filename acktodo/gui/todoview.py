from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from acktodo.gui.viewmodel.vmtodo import *
from acktodo.domain.todo import *

class TodoView(Widget):
    _todo_id = ""
    todo_id_input = ObjectProperty(None)

    @property
    def todo_id(self):
        return self._todo_id
    
    @todo_id.setter
    def todo_id(self, value):
        self._todo_id = value
        self.vm.todo_id = value
        if self.todo_id_input.text != value:
            self.todo_id_input.text = value

    def on_text(self, value):
        print("todo_id changed: %s", value)
        self.todo_id = value

    def build(self):
        self.vm = VMTodo(TodoList())
        print("'%s'" % self.vm.todo_id)
        self.todo_id = self.vm.todo_id

class TodoApp(App):
    def build(self):
        view = TodoView()
        view.build()
        return view

