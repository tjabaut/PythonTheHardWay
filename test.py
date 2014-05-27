globalVar = "This is global"


def myFunction():
    localVar = "This is local"
    print "myFunction - localVar:  ", localVar
    print "myFunction - globalVar: ", globalVar


myFunction()
print
print "global - globalVar: ", globalVar
print "global - localVar:  ", localVar