def trying(x1):
    #global x
    print "From function"
    x1.pop(0)
    x1.append("Bye")
    print x1[1]
    print id(x1)
    

x =  ["Hello","World"]
print id(x)
print "See"
trying(x)
print x[1]

