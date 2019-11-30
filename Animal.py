#import random class
import random
#Animal class
class Animal:
    #init method to define the three attributes
    #and assign default values
    def __init__(self, AnimalType, AnimalName):
        self.animal_type=AnimalType
        self.name=AnimalName
        self.mood=self.check_mood()
      
    #get_animal_type() returns the value of the animal_type field
    def get_animal_type(self):
        return self.animal_type
  
    #get_name returns the value of the name field
    def get_name(self):
        return self.name
  
    #check_mood returns the mood of the animal
    def check_mood(self):
        number=0
        number=random.randint(1,3)
        if number==1:
            return "happy"
        elif number==2:
            return "hungry"
        elif number==3:
            return "sleepy"
