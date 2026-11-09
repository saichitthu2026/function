class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greeting(self):
        print(f"hello my name is {self.name},my age is {self.age}")

    def hay(self):
        self.greeting()