class Employee:
    #special method/dunder method 
    def __init__(self):
      print("Started executing the attribute/data")
      self.id=123
      self.salary=50000
      self.designation="SDE"
      print("attribute/data have been exeecuted")

    def travel(self,destination):
       print("this travel function was called manually .")
       print("Employee is now travelling to ",destination )
         

sam=Employee()   
#sam.travel("Bangalore")
#print(sam.salary)  