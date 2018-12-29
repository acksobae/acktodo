import unittest
from acktodo.domain.todo import *
from acktodo.exc import *

class Test_todo_param(unittest.TestCase):
    def setUp(self):
        self.tlist = TodoList()
        self.tlist.add("bp", "Buy a pen.")
        self.tlist.add("ba", "Buy an apple.")

    def test_todo_add_param(self):
        self.tlist.add_param("note")
        ti = self.tlist.items["ba"]
        ti.params["note"] = "This is a comment."
        assert ti.params["note"] == "This is a comment."

if __name__ == "__main__":
    pass
