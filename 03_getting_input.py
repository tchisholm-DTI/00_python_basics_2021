# Ask the user for their name
username = input("What is your name? ")

# Ask the use for their favourite integer
fav_num = int(input("Favourite Number?"))

# Double, halve and square the number
double = fav_num * 2
half = fav_num / 2
squared = fav_num * fav_num

print()
# Greet the user
print("Hi {}, your favourite number is {}".format(username, fav_num))
print()
# Output the results of the doubling, halving 
# and squaring their favourite number
print("{} doubled is {}".format(fav_num, double))
print("{} halved is {}".format(fav_num, half))
print("{} squared is {}".format(fav_num, squared))
print()
