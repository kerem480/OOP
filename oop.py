class CAR:

    def __init__ (self,name,age,speed,color,price):
        self.name=name
        self.age=age
        self.speed=speed
        self.color=color
        self.__price=price
        self.__discount=None

    
    def way(self,road):
        return f"{self.name} is going to {road}"
    
    def get_discount(self,discount):
        self.__discount=discount
    
    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price
    
    def __repr__(self):
        return f"{self.name} is {self.age} age and have {self.speed} speed  color is {self.color} Price: {self.get_price()}"
        
car1= CAR("Mercedes",6,300,"grey",300)
car2=CAR("Mclaren",3,250,"orange",200)
car2.get_discount(0.20)
print(car1.get_price())
print(car2.get_price())
print(car1)
print(car2)
car2.way("Bristol")



class national(CAR):
    def __init__(self,name,age,speed,color,price,country):
        super().__init__(name,age,speed,color,price)
        self.country=country

car3=national("Porsche",2,220,"black",250,"German")
car3.get_discount(0.20)
print(car3)

class gear(CAR):
    def __init__(self,name,age,speed,color,price,gears):
        super().__init__(name,age,speed,color,price)
        self.gears=gears

car4=gear("Cadillac",1,170,"brown",110,4)
car4.get_discount(0.10)
print(car4)