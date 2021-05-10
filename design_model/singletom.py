'''class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance=super(Singleton,cls).__new__(cls)
        return cls._instance

class TestMode(Singleton):
    def __init__(self,a):
        self.a=a'''

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=super(Singleton,cls).__new__(cls)
        return cls._instance
class TestMode(Singleton):
    def __init__(self,x):
        self.a=x


a=TestMode(10)
print((a.a))
b=TestMode(20)
print(a.a)
print(b.a)
print(id(a),id(b))
