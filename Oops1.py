class Employee:
    #special method/dunder method 
    def __init__(self):
      #print("Started executing the attribute/data")
      print(id(self))
      self.id=123
      self.salary=50000
      self.designation="SDE"
     # print("attribute/data have been exeecuted")

    def travel(self):
       print("this travel function was called manually .")
       print("Employee is now travelling to Delhi" )
         

sam=Employee()   

shaktiman=Employee()
print(id(sam))
print(id(shaktiman))
#sam.travel("Bangalore")
#print(sam.salary) 
#sam.travel()
