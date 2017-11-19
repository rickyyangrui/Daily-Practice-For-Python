# 设计模式
## 三种常见的设计模式
* 创建模式，提供实例化的方法，为适合的状况提供相应的对象创建方法。
* 结构化模式，通常用来处理实体之间的关系，使得这些实体能够更好地协同工作。
* 行为模式，用于在不同的实体建进行通信，为实体之间的通信提供更容易，更灵活的通信方法。
### 创建型

1. Factory Method（工厂方法）

2. Abstract Factory（抽象工厂）

3. Builder（建造者）

4. Prototype（原型）

5. Singleton（单例）

### 结构型

6. Adapter Class/Object（适配器）

7. Bridge（桥接）

8. Composite（组合）

9. Decorator（装饰）

10. Facade（外观）

11. Flyweight（享元）

12. Proxy（代理）

### 行为型

13. Interpreter（解释器）

14. Template Method（模板方法）

15. Chain of Responsibility（责任链）

16. Command（命令）

17. Iterator（迭代器）

18. Mediator（中介者）

19. Memento（备忘录）

20. Observer（观察者）

21. State（状态）

22. Strategy（策略）

23. Visitor（访问者）

### 创建型
１．Factory Method（工厂方法）
意图：

定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method 使一个类的实例化延迟到其子类。

适用性：

当一个类不知道它所必须创建的对象的类的时候。

当一个类希望由它的子类来指定它所创建的对象的时候。

当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候。
```
#!/usr/bin/python
#coding:utf8
'''
Factory Method
'''
 
class ChinaGetter:
    """A simple localizer a la gettext"""
    def __init__(self):
        self.trans = dict(dog=u"小狗", cat=u"小猫")
 
    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)
 
 
class EnglishGetter:
    """Simply echoes the msg ids"""
    def get(self, msgid):
        return str(msgid)
 
 
def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, China=ChinaGetter)
    return languages[language]()
 
# Create our localizers
e, g = get_localizer("English"), get_localizer("China")
# Localize some text
for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))
```
### 抽象工厂模式
意图：
提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。
适用性：

 一个系统要独立于它的产品的创建、组合和表示时。

 一个系统要由多个产品系列中的一个来配置时。

 当你要强调一系列相关的产品对象的设计以便进行联合使用时。

 当你提供一个产品类库，而只想显示它们的接口而不是实现时
 ```
 #!/usr/bin/python
#coding:utf8
'''
Abstract Factory
'''
 
import random
 
class PetShop:
    """A pet shop"""
 
    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.
        We can set it at will."""
 
        self.pet_factory = animal_factory
 
    def show_pet(self):
        """Creates and shows a pet using the
        abstract factory"""
 
        pet = self.pet_factory.get_pet()
        print("This is a lovely", str(pet))
        print("It says", pet.speak())
        print("It eats", self.pet_factory.get_food())
 
 
# Stuff that our factory makes
 
class Dog:
    def speak(self):
        return "woof"
 
    def __str__(self):
        return "Dog"
 
 
class Cat:
    def speak(self):
        return "meow"
 
    def __str__(self):
        return "Cat"
 
 
# Factory classes
 
class DogFactory:
    def get_pet(self):
        return Dog()
 
    def get_food(self):
        return "dog food"
 
 
class CatFactory:
    def get_pet(self):
        return Cat()
 
    def get_food(self):
        return "cat food"
 
 
# Create the proper family
def get_factory():
    """Let's be dynamic!"""
    return random.choice([DogFactory, CatFactory])()
 
 
# Show pets with various factories
if __name__ == "__main__":
    shop = PetShop()
    for i in range(3):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("=" * 20)
 ```
