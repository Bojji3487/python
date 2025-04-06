class grandparent:
    num_of_grandparents=0
    def __init__(self,firstName:str,lastName,age):
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        firstName.capitalize

    def printVal(self):
        print(f'Name is {self.firstName+" "+self.lastName} and age is {self.age}')




class parent(grandparent):
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)



daadi=grandparent('Kaushalya','Narnolia','80')
father=parent('Deepak','Narnolia','50')
daadi.printVal()
father.printVal()