
def proxy_for(parent, attrs, **kwargs):
    """ Add properties for the attrs on the provided field to 
        hide interaction from a class to an internal component """
    def addProxyData(cls):
        def add_property(cls, attr):
            setattr(cls, attr, ProxyAttr(parent, attr, **kwargs))
            
        for attr in attrs:
            add_property(cls, attr)
        return cls
    return addProxyData
    
def ProxyAttr(parent, attr, **kwargs):
    """ Return the property to get, set and delete the attr aon the parent field """
    includeDefault = 'default' in kwargs
    return build_property(parent, attr) if not includeDefault else build_default_property(parent, attr, kwargs['default'])
    
def build_property(parent, attr):
    """ Return the property to access the field """
    def getter(self):
        return getattr(getattr(self, parent), attr)
    def setter(self, v):
        setattr(getattr(self, parent), attr, v)
    def deleter(self):
        delattr(getattr(self, parent), attr)
    return property(getter, setter, deleter)
    
def build_default_property(parentAttr, attr, default):
    """ Return the property to access the field or return a default value """
    def getter(self):
        parent = getattr(self, parentAttr)
        return getattr(parent, attr) if parent is not None else default
    def setter(self, v):
        setattr(getattr(self, parent), attr, v)
    def deleter(self):
        delattr(getattr(self, parent), attr)
    return property(getter, setter, deleter)