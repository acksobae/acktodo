import unittest
from unittest.mock import MagicMock as Moq
from acktodo.domain.todo import *
from acktodo.exc import *
from acktodo.gui.viewmodel.vmtodo import *

class Test_view_todo(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_get_current_id(self):
        todo_view = Moq()
        viewModel = VMTodo(todo_view, Moq())
        assert viewModel.todo_id == "-"
        # User inputs todo id of "a".
        todo_view.todo_id = "a"
        viewModel.get_current()
        assert viewModel.todo_id == "a"
        # User inputs todo id of "b".
        todo_view.todo_id = "b"
        viewModel.get_current()
        assert viewModel.todo_id == "b"

    def test_add_new_todo_and_view(self):
        todo_view = Moq()
        repository = Moq()
        view_model = VMTodo(todo_view, repository)
        # User inputs todo item a's information.
        todo_view.todo_id = "a"
        todo_view.todo_desc = "Buy an apple."
        view_model.add_current()
        todo = repository.get("a")
        assert todo.id == "a"
        assert todo.desc == "Buy an apple."
        # User inputs todo item b's information.
        todo_view.todo_id = "b"
        todo_view.todo_desc = "Buy a banana."
        view_model.add_current()
        todo = repository.get("b")
        assert todo.id == "b"
        assert todo.desc == "Buy a banana."
        # User inputs todo id of "a" and request its information in repos.
        todo_view.todo_id = "a"
        view_model.query()
        viewModel.get_current()
        assert view_model.todo_desc == "Buy an apple."

if __name__ == "__main__":
    pass
