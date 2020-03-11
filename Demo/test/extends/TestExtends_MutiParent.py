class ParentClass1:
    def __int__(self, name, age):
        self.name = name;
        self.age = age;

    def speak(self):
        print('speak ParentClass1');

class ParentClass2:
    def speak(self):
        print('speack ParentClass2');

    def walk(self):
        print('walk ParentClass2');


class SubClass1(ParentClass2,ParentClass1):
    def __init__(self, name, age, country):
        ParentClass1.__int__(self, name, age);
        self.country = country;

    #新增方法
    def write(self):
        print('wirte SubClass1');


b1 = SubClass1('jack',21,'China');

#子类包含父类的所有属性和方法

print(b1.name);
print(b1.age);
print(b1.country);

#speak 在父类1和2中都有定义，则按照继承顺序来调用
b1.speak();
b1.write();

b1.walk();


