__author__ = 'Red'

firstnum = raw_input("Enter first integer: ")
secondnum = raw_input("Enter second integer: ")

firstnum = int(firstnum)
secondnum = int(secondnum)

add = firstnum + secondnum
diff = firstnum - secondnum
prod = firstnum * secondnum
quot = firstnum / secondnum
remainder = firstnum % secondnum

print "The sum of " + str(firstnum) + " and " + str(secondnum) + " is " + str(add)
print "The difference of " + str(firstnum) + " and " + str(secondnum) + " is " + str(diff)
print "The product of " + str(firstnum) + " and " + str(secondnum) + " is " + str(prod)
print "The quotient of " + str(firstnum) + " and " + str(secondnum) + " is " + str(quot) + " with remainder " + str(remainder)


