import unittest
from unittest import mock
from acktodo.helper import *

class A(object):
    def __init__(self):
        self.a = "a"

    def call_a(self):
        return "a"

class B(object):
    def __init__(self):
        self.b = "b"

    def call_b(self):
        return "b"

class C(A,B):
    def __init__(self):
        pass

class Test_learn_python(unittest.TestCase):
    def test_inherit(self):
        c = C()
        assert c.call_a() == "a"
        assert c.call_b() == "b"

class Test_learn_mock(unittest.TestCase):
    def setUp(self):
        m = mock.MagicMock()
    
    def test_mock(self):
        def call_y(): return "y"
        def call_z(): return "z"
        m = mock.MagicMock(b="x", c = call_y, is_false=lambda:False)
        assert isinstance(m.x, mock.MagicMock)
        assert m.a
        assert m.b == "x"
        assert m.c() == "y"
        assert m.is_true()
        assert not m.is_false()
        m.c = call_z
        assert m.c() == "z"

    def test_side_effect(self):
        m = mock.MagicMock(
            s = mock.MagicMock(side_effect=[1,2,3])
        )
        assert m.s() == 1
        assert m.s() == 2
        assert m.s() == 3

class View(object):
    def initialize(self, viewmodel):
        self.vm = viewmodel
        self.text = viewmodel.text
        self.date = viewmodel.date
        def text_changed(value):
            if self.text != value: self.text = value
        self.vm.add_text_changed(text_changed)
        def date_changed(value):
            if self.date != value: self.date = value
        self.vm.add_date_changed(date_changed)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.vm.text = value
    
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
        self.vm.date = value
    
class ViewModel(object):
    @define_data_binding("text")
    @define_data_binding("date")
    def __init__(self):
        self.handlers_text_changed = []
        self.handlers_date_changed = []
        self.text = "a"
        self.date = 1

    def add_text_changed(self, handler):
        self.text_changed.append(handler)

    def add_date_changed(self, handler):
        self.date_changed.append(handler)

    def fire_update(self, handlers, value):
        for handler in handlers:
            handler(value)

class Test_learn_data_binding(unittest.TestCase):
    def test_data_binding(self):
        v = View()
        vm = ViewModel()
        assert vm.text == "a"
        v.initialize(vm)
        assert v.text == "a"
        v.text = "b"
        assert vm.text == "b"
        vm.text = "c"
        assert v.text == "c"

    def test_multi_data_binding(self):
        v = View()
        vm = ViewModel()
        assert vm.date == 1
        v.initialize(vm)
        assert v.date == 1
        v.date = 2
        assert vm.date == 2
        vm.date = 3
        assert v.date == 3

def define_property(self, id, value=None):
    field_name = "_{}_{}".format(self.__class__.__name__, id)
    setattr(self, field_name, value)
    getter = lambda _: getattr(self, field_name)
    def setter(self, value):
        setattr(self, field_name, value)
        self.flag = True
    setattr(self.__class__, id, property(getter, setter))

def define_properties(*names):
    def decorator(constructor):
        def wrapper(self, **kwargs):
            for name in names:
                define_property(self, name, kwargs.get(name))
            constructor(self, **kwargs)
        return wrapper
    return decorator

class User:
    @define_properties("name", "date")
    def __init__(self):
        self.name = "a"
        self.date = "b"

class Test_learn_decorate_property(unittest.TestCase):
    def test_define_property(self):
        self.flag = False
        define_property(self, "name", "a")
        assert self.name == "a"
        self.name = "b"
        assert self.name == "b"
        assert self.flag

    def test_decoreate_properties(self):
        u = User()
        assert u.name == "a"
        assert u.date == "b"

class Test_learn_event(unittest.TestCase):
    def set_text(self, value, event):
        self.text = value
        event.fire(value)
    
    def set_date(self, value):
        self.date = 2

    def test_event(self):
        self.text = "a"
        self.date = 1
        text_changed_event = Event()
        text_changed_event.add(self.set_date)
        self.set_text("b", text_changed_event)
        assert self.date == 2


if __name__ == "__main__":
    pass
