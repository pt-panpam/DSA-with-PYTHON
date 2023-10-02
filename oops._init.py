class Vehicle:
    def __init__(self,color,price,model,milage):
        self.color=color
        self.price=price
        self.model=model
        self.milage=milage
    def show_vehicle_details(self):
        print("details of vehicle is here")
        print("color of bike is:",self.color)
        print("price of bike is:",self.price)
        print("Model of bike is:",self.model)
        print("milage of bile is:",self.milage)
b1=Vehicle("yellow",74000,"Dawn","35km/litre")
b1.show_vehicle_details()