hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
#input values come in as strings, we want to change them to floats in order to do math with them. This is done in the equation below using the float() function.
Pay = float(hours) * float(rate)
print("Pay:", Pay)