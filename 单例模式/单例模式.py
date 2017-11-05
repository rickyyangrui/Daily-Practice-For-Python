# 使用__new__
# 为了使类只能出现一个实例，我们可以使用__new__来控制实例的创建过程
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance

class Myclass(Singleton):
    a = 1




