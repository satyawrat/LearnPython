#declare a function called cheese_and_crackers and make it accept two arguements, cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that is enough for the party!"
    print "Get a blanket. \n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)
#the above lines calls the cheese_and_crackers function and passes numerical values to it

print "OR, we use variables from out script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do the math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, both variables and math:"
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+ 1000)