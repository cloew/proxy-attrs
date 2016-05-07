
def proxy_for(parent, attrs):
    """ Add properties for the attrs on the provided field to 
        hide interaction from a class to an internal component """
    def addProxyData(cls):
        def add_property(cls, attr):
            setattr(cls, attr, build_property(attr, parent))
            
        for attr in attrs:
            add_property(cls, attr)
        return cls
    return addProxyData
    
def ProxyAttr(parent, attr):
    """ Return the property to get, set and delete the attr aon the parent field """
    return build_property(attr, parent)
    
def build_property(attr, parent):
    """ Return the property to access the field """
    def getter(self):
        return getattr(getattr(self, parent), attr)
    def setter(self, v):
        setattr(getattr(self, parent), attr, v)
    def deleter(self):
        del getattr(getattr(self, parent), attr)
    return property(getter, setter, deleter)