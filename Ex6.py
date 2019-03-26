#binds 10 to types_of_people
types_of_people = 10
#this code uses the value types_of_people to add in another value, (10)
x = f"There are {types_of_people} types of people."
#this binds binary with "binary"
binary = "binary"
#this assigns do_not to "don't"
do_not = "don't"
#this code uses the values binary and do_not to add in the assigned values.
y = f"Those who know {binary} and those who {do_not}."
#these two codes will print out whatever value is assigned to (x) and (y)
print(x)
print(y)
#these two codes will use the values (x) and (y)
print(f"I said: {x}")
print(f"I also said: {y}")
#this assigns hilarious to False
hilarious = False
#and this assigns "Isn't that joke so funnny?! {}" to joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"
#this will substitute joke_evaluation and (hilarious) with the following texts assigned to them
print(joke_evaluation.format(hilarious))
#this assigns the two texts to w and e
w = "This is the left side of..."
e = "a string with a right side."
#this code will add the values assigned to w and e, making the text longer
print(w + e)