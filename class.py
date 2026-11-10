class bag:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def promotion(self):
        self.price= (self.price)-(self.price*0.1)
        print(f"promotion price  , {int(self.price)}")

item=bag("Nice",100000)
print("real price" ,item.price)
item.promotion()
item.promotion()      