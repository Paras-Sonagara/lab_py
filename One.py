try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    result = number1 / number2

except ZeroDivisionError:
    print("You cannot divide by zero!")

except ValueError:
    print("Please enter a valid number!")

else:
    print("Division successful! Result is:", result)

finally:
    print("This block always runs.")
