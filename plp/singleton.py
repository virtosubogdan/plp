class SingletonClass(type):
    __instances__ = {}

    def __call__(cls, *args, **kwargs):
        if cls not in SingletonClass.__instances__:
            instance = super(SingletonClass, cls).__call__(*args, **kwargs)
            SingletonClass.__instances__[cls] = instance
            return instance
        return SingletonClass.__instances__[cls]
