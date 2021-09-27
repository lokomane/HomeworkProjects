# Ask user for two numbers
num1 = input("what is your first number")
num2 = input("what is your second number")
sum = (int(num1) + int(num2))
prod = (int(num1)*int(num2))
# Create a loop that does the following until the product and sum are the same
print(sum)
print(prod)
loop = 0
while (loop <= 1):
    while (sum != prod):
        print("your sums are not equal, try again")
        num1 = input("what is your first number")
        num2 = input("what is your second number")
        sum = (int(num1) + int(num2))
        prod = (int(num1) * int(num2))
        print(sum)
        print(prod)
    while (sum == prod):
        print("your sums are equal, congratulations!")
        num1 = input("what is your first number")
        num2 = input("what is your second number")
        sum = (int(num1) + int(num2))
        prod = (int(num1) * int(num2))
        print(sum)
        print(prod)


# Calculate and disply their sum


# Calculate and display their product


# If their sum and their product are equal - tell the user
# otherwise ask for two more numbers
