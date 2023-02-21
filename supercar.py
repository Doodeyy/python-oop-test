#Λυτρίδης Αλέξανδρος

class SuperCar:
    maxSpeed = 330
    cars = []
    def __init__(self , car_model , color , price):
        self.car_model = car_model
        self.color = color
        if price <= 0:
            self.price = 140000
        
        else:
            self.price = price
        SuperCar.cars.append(self.car_model)
            
            
    def lastPrice(self):
        extra = self.price * 40 / 100
        teliki = self.price + extra
        return teliki
        
        
    def display(self):
        print ("Car model: " , self.car_model , "\n" , "Color: " , self.color , "\n" , "Price: " , self.price , "\n" , "Max speed: " , self.maxSpeed)
        
        
    @classmethod    
    def changeSpeed(cls):
        cls.maxSpeed = int(input("Enter new max speed: "))
        return cls.maxSpeed
    
    @staticmethod
    def searchModel(model):
        if model in SuperCar.cars:
            return True
        else:
            return False
        
   
car1 = SuperCar("Lambo Aventador" , "Yellow" , 190000)
car2 = SuperCar("Ferrari SF90" , "Red" , 230000)
car3 = SuperCar("Porsche 911 Turbo S" , "Gray" , -90000)

car1.display()
car2.display()
car3.display()

print ("Last price Lambo Aventador: " , car1.lastPrice())
print ("Last price Ferrari SF90: " , car2.lastPrice())

SuperCar.changeSpeed()

print (car3.maxSpeed , "km/h for Porsche 911 Turbo S")

print (SuperCar.searchModel("Ferrari SF90"))
