class product_catlogue:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculator(self):
        total_value = self.price * self.quantity
        return(total_value)
# create an object 
p1 = product_catlogue("milk",price =500 ,quantity=3)
print(p1.calculator())
