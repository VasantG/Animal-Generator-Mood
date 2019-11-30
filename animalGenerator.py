#import the Animal class
from Animal import Animal  
#to create a new Animal object instance
animals=[]
choice="y"
print("Welcome to the animal generator!")
print("This program creates Animal objects.")

#while loop to add animals
while choice=="y":
    #prompt the user to enter type of animal
    Type=input("What type of animal would you like to create? ")
    #prompt the user to enter name of animal
    Name=input("What is the animal’s name? ")
    #create an object temp pf type Animal
    temp=Animal(Type,Name)
    #append temp to animals list
    animals.append(temp)
    choice=input("Would you like to add more animals (y/n)? ")

#to display the animals
print("Animal List:")
for i in animals:
    print(i.get_name()+" the "+i.get_animal_type()+" is "+i.check_mood())
