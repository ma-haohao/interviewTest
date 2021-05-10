#工厂方法的例子
class DogToy:
    def speak(self):
        print("wang wang")

class CatTory:
    def speak(self):
        print("miao miao")

def toy_factory(toy_type):
    if toy_type=='dog':
        return DogToy()
    elif toy_type=="cat":
        return CatTory()

#高层代码
p=toy_factory('dog')
p.speak()
