#------------------------object-oriented programming (OOP)---------------------------------


#---------------------------------general--------------------------------

#paradigms:
#procedural --> top to bottom
#functional programming --> pass functions around, anonymus functions, lambda functions,...
#oject oriented




#tuple:

#-collection of values/data --> e.g. (name,house) or name,house
#-difference tuple vs. list: tuple not mutatable but you still can index into it
# used e.g. for defensive/secure programming
# tuples can also be nested into each other




# ------------------------------------OOP----------------------------------------

#-------------classes-------------------------

#-invent own data types and give them names
#-are mutable but can be made immutable

#----
#e.g. create class

    #class Student:         #-->this is the class (own classes by convention should start with upper case)
        #def __init__(self, argument a, argument b, ...):             #"self" just represents the class the specific input values(arguments) should be passed to to create specific instace attributes/variables for this class / gives you access to the specific class (could be namend anything, but "self" is convention)
            #self.variable1 = argument a
            #self.variable2 = argument b
            #...

    #-->argument a, argument b, ... are input values which become instance attributes/variables // an actual representation of the class is an object/instance --> e.g. Harry = Student(Gryffindor,male) --> Harry is object/instance of class Student with the specific instance attributes/variables Gryffindor and male

    #def main():
        #student = get_student()
        #print(f"{student.name} from {student.house}")


    #def get_student():
        #name = input("Name: ")
        #house = input("House: ")
        #student = Student(name,house)          #called construction call --> create object/instance of a class
        #return student
#-----

# classes are much more powerful than dictionaries, because you can manipulate the possible input given and what shall happen with it in the class much better
# all functionalities, checking, etc. relating to the class should be defined inside of the class itself --> individually created functions can be used outside of class afterwards
# it is possible to create classes and store the in libraries to reuse them
# things can be made optional by setting the input arguemnts to a class to None --> e.g. argument a = None
# use try/except to control which input is valid for specific classes (also raise errors


#much more functions usable in classes:
    # def __new__ a new empty class can be created (is done by python automatically before __init__)
    # def __str__ used in class handles the representation of the object as a string if other functions want to access it, not only show the position where it is in memory
    # def __rep__ used to give multiple infomrations about specific instance/object
    # ...
    # you can also define your own functions (methods) inside a class

#---------------------------------------------------------------------------

#IMPORTANT! (for the following content)
#====> the problem is, that we can never make input variables really unchangeable/constrain them, because if you use getter and setter, you will still assign the value to something, (if not self.name = name, then it will be self._name = name)
        #and you can easily change this by just assigning a new value to it. In python there is no functionality to prevent someone advisarily changing your input variables, it is just based on the honor system,
        #that when you see an input variable with an underscore (e.g. self._name = name) you just shouldn't touch it


#properties (@property):
    #used to be more defensive and have more control over arguments --> e.g. be able to determine if a instance variable can be overwritten later on or not

    #-->decorators:
        # -functions which influence the functionality of other functions so to speak (influences property function)
        # -needs a property to work on

#--> we use properties and decorators to make sure an instance variable has the right content if it is first defined and can't be overwritten at a later point in time:
    # -->e.g. a line like student.house = "abc" in main() wouldn't work anymore cause the call would always require the getter and setter function to be run through where the setter function contains specific constraints

#functionality of getter and setter:
    #--> so we "reproduce the value of specific input variables in the getter and then apply constraints to it in the setter.
    # --> we name the getter function exactly like the specific input variable, so if someone tries to change the input variable later on outside of the class (e.g. self.name =  "abc", the name function ) the setter function is called and forbids/constrains this alteration

        #getter is always called, when someone tries to access/retrieve the value of an input variable (for which getter function is defined) -> makes input variable a property
        #setter is always called, when someone tries to modify the value of an input variable (for which getter and setter function are defined) if the input variable is a property
#--------------------------------------------
#e.g.

#class Student:
 #   def __init__(self, name, house):
  #      self.name = name
  #         #-->will trigger getter and setter function of "name" further down in class and only set it, if it meets the constraints/requirements of setter function
            #-->if using getter and setter, instead of just assigning "name" to "self.name", python calls the getter and setter function and verify if the input "name" is valid and can be assigned (used methods on input = input to methods)
   #     self.house = house
#
 #   def __str__(self):
  #      return f"{self.name} from {self.house}"
#
 #   @property          #property, getter function --> get the value (called when someone accesses the value )
  #  def name(self):
   #     return self._name          #underscore needed because python gets confused otherwise ( if only name was used, python would call the name function (property) again --> infinite loop, and not the return of the attribute name )
#
 #   @name.setter               #decorator, setter function --> "set" the value, input variable value is set here, notat __init__
  #  def name(self, name):
   #     if not name:
    #        raise ValueError("Invalid name")
     #   self._name = name
#
 #   @property
  #  def house(self):
   #     return self._house
#
 #   @house.setter
  #  def house(self, house):
   #     if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    #        raise ValueError("Invalid house")
     #   self._house = house
#
#
#def main():
 #   student = get_student()
  #  print(student)
#
#
#def get_student():
 #   name = input("Name: ")
  #  house = input("House: ")
   # return Student(name, house)
#
#
#if __name__ == "__main__":
 #   main()

#--------------------------------------------


#IMPORTANT! (for the content above)
#====> the problem is, that we can never make input variables really unchangeable/constrain them, because if you use getter and setter, you will still assign the value to something, (if not self.name = name, then it will be self._name = name)
        #and you can easily change this by just assigning a new value to it. In python there is no functionality to prevent someone advisarily changing your input variables, it is just based on the honor system,
        #that when you see an input variable with an underscore (e.g. self._name = name) you just shouldn't touch it



#IMPORTANT!
    #int, str, list, dict, ... are also a classes which use different methods (e.g. str.strip()) inside of them
    #often times if you want to build something yourself/individually, you use an existing class and alter it/enhance it to a certain degree (build an individual subclass)
    #==> in python everything is an object/instance, so all data types are instances of classes



#---instance methods/instace variables vs. class methods/class variables:---

#difference between methods refering to instance variables and methods refering to whole class:
    #-->not all methods refer just to instance variables, some do refer to whole class (using another decorator: @classmethod), if not instance methods and instance variable are used by default
        #-->if you do not want to create several instances of the class and just use it to tie some functionalities or data together, you can use @classmethod and refer to the class variables (not instance variables) via "cls"
            #-->you should also move the function for creating an instance (which includes construction call) inside the class
            #---------------------------------------
            #e.g. sort student to random house

                #import random

                # class Hat:
                    #houses = ["a","b","c","d"]

                    #@classmethod
                    #def sort(cls,name)
                        #print(name,"is in", random.choice(cls.houses))


                #Hat.sort("Harry")

                #-->when to use classes, simple functions, libraries depends on the individual task. Often classes and libraries are more handy if the code gets bigger and bigger and you collaborate with different people
                #-->there are also more types of methods besides @classmethod, e.g. @staticmethod, ...
          #-------------------------------------------

#--------inheritance of classes:---------
    #you can structure classes in hierachical architecture and have some classes inherit parts of itself to other classes if both classes have those parts in common
        #avoid identical code for multiple classes and to just do error checking at one class

#-----------
#e.g.
#Demonstrates inheritance


#class Wizard:
 #   def __init__(self, name):
  #      if not name:
   #         raise ValueError("Missing name")
    #    self.name = name
#
 #   ...


#class Student(Wizard):             #give as input the super/parent class
 #   def __init__(self, name, house):
  #      super().__init__(name)     #access the instance variable name of the super class
   #     self.house = house

    #...


#class Professor(Wizard):
 #   def __init__(self, name, subject):
  #      super().__init__(name)
   #     self.subject = subject

    #...


#wizard = Wizard("Albus")
#student = Student("Harry", "Gryffindor")
#professor = Professor("Severus", "Defense Against the Dark Arts")
#...

#------------

#------operator overlaoding:------

    #use operators (+,-,:,*, etc. --> fixed list of operators in python usable) for example to add two whole classes and their values togehter --> we always need to teach/formulate for python how we want to use the operator
    #-->you can tweak the operator to function your way, using different functions inside classes like __add__ ofr +, __mul__ for * , ... (operators are part of syntax, but have no classes attached to them)
        #-->if you do not tweak them in your way, they will remain in default functionality for the specific use case (e.g. concatenate two strings // add two ints // ...))

#----------
    #e.g.
    # Adds vaults via operator overloading


#class Vault:
 #   def __init__(self, galleons=0, sickles=0, knuts=0):
  #      self.galleons = galleons
   #     self.sickles = sickles
    #    self.knuts = knuts
#
 #   def __str__(self):
  #      return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
#
 #   def __add__(self, other):              #self is here the value on the left of the plus sign, and other the value on the right side --> this works as a blueprint for python, and we now can add multiple vaults using this procedure, not just two
  #      galleons = self.galleons + other.galleons
   #     sickles = self.sickles + other.sickles
    #    knuts = self.knuts + other.knuts
     #   return Vault(galleons, sickles, knuts)     #needed to represent the new vault computed
#
#
#potter = Vault(100, 50, 25)
#print(potter)
#
#weasley = Vault(25, 50, 100)
#print(weasley)

#total = potter + weasley
#print(total)

#----------

