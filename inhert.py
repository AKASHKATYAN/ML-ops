# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#             print(f"{self.name} makes a sound.")


# class Dog(Animal):
#     def __init__(self):
#         self.behaviour='Friendly'
#     def speak(self):
#           print(f"{self.name}.He is very {self.behaviour}")
# animal=Animal("Generic animal")
# animal.speak()

# dog=Dog()
# dog.speak()  


#SUPER KEYWORD

class Animal:
    def __init__(self):
        self.name='Buddy'
        
    def speak(self):
        print(f"{self.name} makes a sound")    
    
class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed=breed
    
    def speak(self):
        super().speak()#Call the base class 
        print(f"{self.name} barks.It is a {self.breed}") 
        
dog=Dog("Golden Retriever") 
dog.speak()

             
    












