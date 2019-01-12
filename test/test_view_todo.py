import unittest
from unittest.mock import MagicMock as Moq
from acktodo.domain.todo import *
from acktodo.exc import *
from acktodo.gui.viewmodel.vmtodo import *
from acktodo.helper import *

class User:
    @define_data_binding("name")
    @define_data_binding("date")
    def __init__(self):
        self.name = "a"
        self.date = "b"

class Test_define_property(unittest.TestCase):
    def test_define_property(self):
        self.test = "a"
        def test_change(value):
            self.test = "b"
        u = User()
        u.name_changed.append(test_change)
        assert self.test == "a"
        u.name = "c"
        assert self.test == "b"

class Test_view_todo(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_add_new_todo_and_view(self):
        repository = TodoList()
        view_model = VMTodo(repository)
        # User inputs todo item a's information.
        view_model.todo_id = "a"
        view_model.todo_desc = "Buy an apple."
        view_model.add()
        todo = repository.get("a")
        assert todo.id == "a"
        assert todo.desc == "Buy an apple."
        # User inputs todo item b's information.
        view_model.todo_id = "b"
        view_model.todo_desc = "Buy a banana."
        view_model.add()
        todo = repository.get("b")
        assert todo.id == "b"
        assert todo.desc == "Buy a banana."
        # User inputs todo id of "a" and request its information in repos.
        view_model.todo_id = "a"
        view_model.query()
        assert view_model.todo_desc == "Buy an apple."

if __name__ == "__main__":
    pass
