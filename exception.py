#用户自定义异常类型
class ToolLongException(Exception):
    "this is user's exception for check the length of name"
    def __init__(self,leng):
        self.leng=leng
    def __str__(self):
        print(("姓名长度是"+str(self.leng)+"，超过长度了"))

#手动抛出用户自定义异常类型
def name_Test():
    try:
        name=input("enter your name:")
        if len(name)>4:
            raise ToolLongException(len(name))
        else:
            print(name)
    except ToolLongException as T:
        print(T)

name_Test()