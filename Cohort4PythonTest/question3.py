# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.

def main():
    total_sum = 0
    
    while True:
        try:
            number = float(input("Enter a number (0 to stop): "))
            if number == 0:
                break
            total_sum += number
        except ValueError:
            print("Please enter a valid number.")

    print(f"The sum of the numbers entered is: {total_sum}")

if __name__ == "__main__":
    main()




# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2

for number in range(1, 101):
    if number % 2 != 0:  #  if the number is not divisible by 2
        print(number)