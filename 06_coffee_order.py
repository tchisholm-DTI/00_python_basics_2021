print()
print("*** Coffee Order Demo")

keep_going = ""
while keep_going == "":

    # Ask user if they want coffee
    want_coffee = input("Do you want coffee? ") .lower()

    # If the answer is no, continue the loop
    if want_coffee != "yes":
        print("wrong answer, you always want coffee")
        continue
    # Otherwise print good choice and break the loop
    else:
        print("Good choice")
        break

print()
print("End of program")
print()