# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).
def calculate_distance(x1, y1, x2, y2):
    # Calculate the distance using the distance formula
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Main program
if __name__ == "__main__":
    try:
        # Input coordinates from the user
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        # Calculate distance
        dist = calculate_distance(x1, y1, x2, y2)

        # Print the result
        print(f"The distance between points ({x1}, {y1}) and ({x2}, {y2}) is: {dist:.2f}")
    except ValueError:
        print("Please enter valid numbers.")






# Question 1(ii)
# Write a Python program to find maximum between three numbers.



