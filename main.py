#Author:Sherelene De Belen


def confirmNumbers(weight, height):
    if weight <= 0 or height <= 0:
        print("Error! please put a number bigger than 0\n")
        #weight = float(input("Enter how much you weigh in pounds: "))
        #height = float(input("Enter your height in inches: "))
        #confirmNumbers(weight, height)
        return True
    else:
        return False




def bmiRange(percentage):
    if percentage < 18.5:
        print("\nYour BMI is {}%\n You are considered UNDERWEIGHT".format(round(percentage, 2)))
    elif 18.5 <= percentage <= 24.9:
        print("\nYour BMI is {}%\n You are considered NORMAL WEIGHT".format(round(percentage, 2)))
    elif 25 <= percentage <= 29.9:
        print("\nYour BMI is {}%\n You are considered OVERWEIGHT".format(round(percentage, 2)))
    else:
        print("\nYour BMI is {}%\n You are considered OBESE".format(round(percentage, 2)))


def usa(runs):
    statement = True
    for i in range(0, runs):
        print("\n---------------------TEST RUN{}--------------------\n".format(i+1))
        while statement == True:
            weight = float(input("Enter how much you weigh in pounds: "))
            height = float(input("Enter your height in inches: "))
            confirmNumbers(weight, height)
        BMI = 703 * weight / (height ** 2)
        bmiRange(BMI)



def metric(runs):
    statement = True
    for i in range(0, runs):
        print("\n---------------------TEST RUN{}--------------------\n".format(i + 1))
        while statement == True:
            weight = float(input("Enter how much you weigh in kilograms: "))
            height = float(input("Enter your height in meters: "))
            statement = confirmNumbers(weight, height)
        BMI = (weight / (height ** 2))
        bmiRange(BMI)


def bmi(system):
    if system == "1":
        runs = int(input("\nHow many times would you like to check your BMI? Enter a number: "))
        usa(runs)
    elif system == "2":
        runs = int(input("\nHow many times would you like to check your BMI? Enter a number: "))
        metric(runs)
    else:
        print("--------------------ERROR! Please input only the number \"1\" or \"2\"-------------------\n")
        choice = input("Which system would you like to use?\nType \"1\" for USA or Type \"2\" for metric:" )
        bmi(choice)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to my BMI calculator!\n")
    choice = input("Which system would you like to use?\nType \"1\" for USA or Type \"2\" for metric: ")
    bmi(choice)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
