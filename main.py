# Author:Sherelene De Belen
# Assignment: Project 1 Task 1
# Completed (or last revision): 02/11/0222

# Description: This project calculates a person's BMI percentage

# This function checks if user inputs a zero in numerator or denominator
def confirm_numbers(weight, height):
    if weight <= 0 or height <= 0:
        print("Error! please put a number bigger than 0\n")  # Safety flag so program doesn't crash from 0 denominator
        return True  # Will keep while statement that calls this function to keep looping
    else:
        return False  # Will stop loop and this function call


# Function prints out your BMI percentage and where that percentage is labeled
def bmi_range(percentage):
    if percentage < 18.5:
        print("\nYour BMI is {}%\n You are considered UNDERWEIGHT".format(round(percentage, 2)))
    elif 18.5 <= percentage <= 24.9:
        print("\nYour BMI is {}%\n You are considered NORMAL WEIGHT".format(round(percentage, 2)))
    elif 25 <= percentage <= 29.9:
        print("\nYour BMI is {}%\n You are considered OVERWEIGHT".format(round(percentage, 2)))
    else:
        print("\nYour BMI is {}%\n You are considered OBESE".format(round(percentage, 2)))


# Function for using USA system
def usa(runs):
    for i in range(0, runs):  # Loops test to user's requirement
        statement = True
        print("\n---------------------TEST RUN {}--------------------\n".format(i + 1))
        while statement:  # Will run only once if user DOES NOT input a zero for weight or height
            weight = float(input("Enter how much you weigh in pounds: "))
            height = float(input("Enter your height in inches: "))
            statement = confirm_numbers(weight, height)  # Calls function to check if weight or height == 0
        bmi = 703 * weight / (height ** 2)  # BMI formula for USA system
        bmi_range(bmi)  # Calls function to print out results


# Function for using metric system
def metric(runs):
    for i in range(0, runs):  # Loops test to user's requirement
        statement = True
        print("\n---------------------TEST RUN {}--------------------\n".format(i + 1))     # Keeps track of how many
        # test runs are being run
        while statement:    # Will run only once if user DOES NOT input a zero for weight or height
            weight = float(input("Enter how much you weigh in kilograms: "))
            height = float(input("Enter your height in meters: "))
            statement = confirm_numbers(weight, height)   # Calls function to check if weight or height == 0
        bmi = (weight / (height ** 2))    # BMI formula for metric system
        bmi_range(bmi)    # Calls function to print out results


# Function to determine which system to use to calculate BMI
def bmi_check(system):
    if system == "1":
        runs = int(input("\nHow many times would you like to check your BMI? Enter a number: "))
        usa(runs)
    elif system == "2":
        runs = int(input("\nHow many times would you like to check your BMI? Enter a number: "))
        metric(runs)
    else:   # Safety guard to ensure user only inputs a "1" or a "2"
        print("--------------------ERROR! Please input only the number \"1\" or \"2\"-------------------\n")
        num = input("Which system would you like to use?\nType \"1\" for USA or Type \"2\" for metric:")
        bmi_check(num)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to my BMI calculator!\n")
    choice = input("Which system would you like to use?\nType \"1\" for USA or Type \"2\" for metric: ")
    bmi_check(choice)
