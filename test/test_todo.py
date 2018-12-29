import unittest
from acktodo.domain.todo import *
from acktodo.exc import *

class Test_todo(unittest.TestCase):
    def check_item_of_id_with_desc(self, id, desc):
        return self.tlist.items[id].desc == desc

    def test_add_todo1(self):
        self.tlist = TodoList()
        self.tlist.add("bp", "Buy a pen.")
        assert self.tlist.count== 1
        assert self.tlist.count == len(self.tlist.items)
        assert self.check_item_of_id_with_desc("bp", "Buy a pen.")

    def test_add_todo2(self):
        self.tlist = TodoList()
        self.tlist.add("ba", "Buy an apple.")
        assert self.tlist.count== 1
        assert self.tlist.count == len(self.tlist.items)
        assert self.check_item_of_id_with_desc("ba", "Buy an apple.")

    def test_add_multi_todos(self):
        self.tlist = TodoList()
        self.tlist.add("bp", "Buy a pen.")
        self.tlist.add("ba", "Buy an apple.")
        assert self.tlist.count == 2
        assert self.tlist.count == len(self.tlist.items)
        assert self.check_item_of_id_with_desc("bp", "Buy a pen.")
        assert self.check_item_of_id_with_desc("ba", "Buy an apple.")

    def test_del_multi_todos(self):
        self.tlist = TodoList()
        self.tlist.add("bp", "Buy a pen.")
        self.tlist.add("ba", "Buy an apple.")
        self.tlist.remove("ba")
        assert self.tlist.count == 1
        assert self.check_item_of_id_with_desc("bp", "Buy a pen.")
        assert len(self.tlist.items) == 1
        self.tlist.remove("bp")
        assert self.tlist.count == 0
        assert len(self.tlist.items) == 0

    def test_add_del_todos(self):
        self.tlist = TodoList()
        self.tlist.add("ga", "Go pointA")
        self.tlist.add("gb", "Go pointB")
        self.tlist.add("gc", "Go pointC")
        assert self.tlist.count == 3
        assert self.check_item_of_id_with_desc("ga", "Go pointA")
        assert self.check_item_of_id_with_desc("gb", "Go pointB")
        assert self.check_item_of_id_with_desc("gc", "Go pointC")
        
class Test_todo_error_patterns(unittest.TestCase):
    def setUp(self):
        self.tlist = TodoList()
        self.tlist.add("bp", "Buy a pen.")
        self.tlist.add("ba", "Buy an apple.")

    def test_register_duplicate_ids(self):
        with self.assertRaises(DuplicateEntryError):
            self.tlist.add("bp", "Buy a pencil.")

    def test_remove_unregistered_id(self):
        with self.assertRaises(KeyError):
            self.tlist.remove("bc")

class Test_check_todo(unittest.TestCase):
    def setUp(self):
        self.tlist = TodoList()
        self.tlist.add("bp", "Buy a pen.")
        self.tlist.add("ba", "Buy an apple.")

    def test_check_one_todo(self):
        ti = self.tlist.items["ba"]
        ti.check()
        assert ti.is_checked
        ti.uncheck()
        assert not ti.is_checked
        ti.toggle()
        assert ti.is_checked
        ti.toggle()
        assert not ti.is_checked
        ti.toggle()
        assert self.tlist.is_checked("ba")

if __name__ == "__main__":
    pass
