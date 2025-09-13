try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Execution completed.")