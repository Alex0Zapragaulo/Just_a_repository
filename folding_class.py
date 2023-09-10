class Class1:
    var = 20

    def envar(self):
        self.var = 40

class Class2:
    rav = 10

    def enrav(self):
        self.rav = 60

class Class3(Class1, Class2):

    def __init__(self):
        print(self.var)
        super().envar()
        print(self.var)
        print(super().var)
        class1 = Class1()
        print(class1.var)
        print(self.rav)
        super().enrav()
        print(self.rav)
        print(super().rav)
        class2 = Class2()
        print(class2.rav)

object = Class3()