"""
​ 在类中声明的变量我们称之为类变量【静态成员变量】，
在__init__()函数中声明的变量并且绑定在实例上的变量我们称之为成员变量。
类变量直接可以通过类名来调用。

1、若类变量与成员同时存在并且同名
使用对象来调用的时候，获取的结果是成员变量的值，
使用类名来调用，获取的是类变量的值。

2、若类变量存在，成员变量不存在，
使用对象来调用的时候，它首先寻找成员变量，
如果成员变量不存在。则去寻找类变量。

3、若类变量不存在，成员变量存在：
使用类名来调用，则会报错

总结：
类变量通过类名或者对象来调用都不会报错，但是成员变量只能通过对象来调用。
通过对象来修改类属性的时候，只能作用到对象自己本身，作用不到类，
若是通过类名来修改类属性，则只对类变量的值进行修改。
"""
class Person(object):
    name = "class-param"
    def __init__(self, name, lang, website):
        self.name = name
        self.lang = lang
        self.website = website

    def sayhi(self):
        print('self: ', self.name)
        print('type of self: ', type(self.name))
    def display(self):
        print("Person:(name: ",self.name," lang : ",self.lang ," website : ",self.website)

p = Person('Tim', 'English', 'www.universal.com')

p.sayhi()
p.display()

print(Person.name)
print(p.name)
