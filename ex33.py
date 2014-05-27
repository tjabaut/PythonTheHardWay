from sys import argv

#Define empty list
numbers = []

#Unpack the runtime parameters
script, first = argv

number = int(first)
#incrementor = int(second)
incrementor = 1

print "The name of the script is:", script
print "The number of iterations is:", first

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i

def NumFunc(nums):
    i = 0

    print "We are starting with the number: ", nums
    print "We will increment by: ", incrementor
    print "The current value of the counter i is: ", i

    while i < nums:
        print "At the top i is %d" % i
        numbers.append(i)

        i += incrementor
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

NumFunc(number)