
#inheritance - having child class with some properties of parent class
#we say child is inheritated from parent 

#parent class

class car():
    def __init__(self,brand,model,color,fuel):
        self.brand = brand
        self.model = model
        self.color=color
        self.fuel = fuel


    def get_color(self):
        return self.color
    
    def set_color(self,new_color):
        self.color = new_color

    def show_car(self):
        print("I am a car with Model {}  of brand of {} with color {} and taking {} of fuel".format(self.model,self.brand,self.color,self.fuel))

#child class
class SUV(car):
    def __init__(self,brand,model,color,fuel,transmission,turbo):
        car.__init__(self,brand,model,color,fuel)
        self.transmission = transmission
        self.turbo=turbo

    def show_car(self):
        print("I am a car with Model {}  of brand of {} with color {} and taking {}".format(self.model,self.brand,self.color,self.fuel))

#method
audi=SUV("audi","Q5","blue","100 percent fuel","automatic","True")
audi.show_car()
    



