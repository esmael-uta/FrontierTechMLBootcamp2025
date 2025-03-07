def calculate_bmi():
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            if weight <= 0:
                print("Weight must be greater than 0. Please try again")
                continue
            height = float(input("Enter your height in meters: "))
            if height <= 0:
                print("Height must be greater than 0. Please try again")
                continue

            bmi = weight / (height ** 2)
            print("Your BMI is: ", bmi)

            if bmi < 18.5:
                print("Underweight")
            elif bmi >= 18.5 and bmi < 25:
                print("Normal weight")
            elif bmi >= 25 and bmi < 30:
                print("Overweight")
            elif bmi >= 30:
                print("Obesity")
            break
        except ValueError:
            print("Invalid input. Please enter a number")
calculate_bmi()


