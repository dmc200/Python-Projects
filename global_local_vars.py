# Scope is a container of variables.
# Variables are temporary.
# Code in a local scope can access global variables. 

spam = 42 # global variable (Global Scope)


def eggs():
    spam = 42 # local variable (Local Scope)

print("Some code here.")
print("Some more code.")


# Local variables cannot be shared between local scopes. 
def spam():
    eggs = 0
    ham = 199
    bacon()
    print(eggs) #What value will this print out? 0 Because local scope var's cannot be shared. 

def bacon():
    eggs = 122
    ham = 5


spam()


# Global variables can be shared into local scopes.

def spam():
    print(eggs) # Would print out 99 as eggs is a global variable. 

eggs = 99
spam()
