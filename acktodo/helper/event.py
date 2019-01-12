

def _define_data_binding(self, id, value=None):
    field_name = "_{}_{}".format(self.__class__.__name__, id)
    event_name = "{}_changed".format(id)
    setattr(self, field_name, value)
    setattr(self, event_name, [])
    getter = lambda _: getattr(self, field_name)
    def setter(self, value):
        if getattr(self, field_name) == value:
            return
        setattr(self, field_name, value)
        for handler in getattr(self, event_name):
            handler(value)
    setattr(self.__class__, id, property(getter, setter))

def define_data_binding(name):
    def decorator(constructor):
        def wrapper(self, **kwargs):
            _define_data_binding(self, name, kwargs.get(name))
            constructor(self, **kwargs)
        return wrapper
    return decorator

class Event(object):
    def __init__(self):
        self.handlers = []

    def add(self, handler):
        self.handlers.append(handler)

    def fire(self, value):
        for handler in self.handlers:
            handler(value)