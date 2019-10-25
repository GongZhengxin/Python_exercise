def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("you have {0} cheeses !".format(cheese_count))
    print("you have {0} cheeses !".format(boxes_of_crackers))
    print("man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)


print("Or we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers =50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("we can even do math inside:")
cheese_and_crackers(10+20,5+6)

print("And we can combine two variables snd math")
cheese_and_crackers(amount_of_crackers+9,amount_of_crackers)


# if you want ask from your participants you must use int() to convert

