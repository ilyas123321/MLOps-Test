#initiate a class
class employee:
    def __init__(self):
        print("line started")
        self.id = "A1213"
        self.salary = 50000
        self.designation = "lead engineer"
        print("lined ended")

#create an object/instance of the class

    def travel(self, destination):
        print(f"Employye is now travalling to {destination}")
#creating an object
sam = employee()

#calling a method
sam.travel("dubai")

print(type(sam))

lst = [1,2,3]
my_str = "hello hyd"
my_int = 12222
my_stre = my_str.capitalize()
print(my_stre)

print(type(my_str))
