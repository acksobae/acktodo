import unittest
from unittest import mock

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

if __name__ == "__main__":
    pass
