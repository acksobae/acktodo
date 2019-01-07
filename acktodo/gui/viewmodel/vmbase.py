
class VMBase(object):
    def __init__(self):
        self.property_changed = None

    def set_property(self, field_name, value, property_name = None):
        if self.__dir__[field_name] == value:
            return False
        self.__dir__[field_name] = value
        h = self.property_changed
        if h is not None:
            h(self, property_name)
        return True
    
