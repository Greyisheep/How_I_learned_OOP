class User:     #Inheritance
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("I'm a teacher!")

class Customer(User):   #here Customer inherits from User
    def __init__(self, name, membership_type):  #The init method is a constructor / initializer, and the values passed in it are the parameters
        self.name = name
        self.membership_type = membership_type
    
    @property      #This is a decorator    
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
    @name.deleter
    def name(self):
        del self._name
        
    def update_membership(self, new_membership):
        #Things that can be done under new definition are:
        #invoke an API
        #update a database
        #charge the customer
        #calculate costs
        #pretty much anything else
        self.membership_type = new_membership
        
    def __str__(self):   #Invoked anytime we want to convert a customer to a string
        return self.name + " " + self.membership_type
    
    def print_all_customers(customers):
        for customer in customers:
            print(customer)
    
    def __eq__(self, other): #This method is invoked for comparing data
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False
    
    __hash__ = None
    
    __repr__ = __str__
             

users = [Customer("Caleb", "Gold"),  #Caleb and Gold here are refered to as arguments
             Customer("Brad", "Bronze"),
             Teacher()]

for user in users:
    user.log()