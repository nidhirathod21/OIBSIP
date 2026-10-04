print("===== BMI CALCULATOR =====")
try:
    # Get weight and height from the user
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if weight < 0:
        print("Weight cannot be negative.")
        exit()

    if height <= 0:
        print("Height must be greater than zero.")
        exit()
    # Calculate BMI
    bmi = weight / (height ** 2)
    print("Your BMI is:", round(bmi, 2))
    # Determine BMI category
    if bmi < 18.5:
        print("Category: Underweight")

    elif bmi < 25:
        print("Category: Normal")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")

    print("Thank you for using the BMI Calculator!")

except ValueError:
    print("Please enter numbers only.")