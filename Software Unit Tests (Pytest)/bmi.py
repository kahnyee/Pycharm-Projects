def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    BMI = weight / (height ** 2)

    if BMI < 18.5:
        BMI_Class = "Underweight"
        return BMI_Class, -1
    elif 18.5 <= BMI <= 25.0:
        BMI_Class = "Normal"
        return BMI_Class, 0
    else:
        BMI_Class = "Overweight"
        return BMI_Class, 1

bmi_class, UnitTest = calculate_bmi(1.73,57)

print("BMI Class:", bmi_class)
