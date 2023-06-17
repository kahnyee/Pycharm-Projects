def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    BMI = weight/(height**2)

    if BMI < 18.5 :
        BMI_Class = "Under Weight"
    elif 18.5 <= BMI <= 25.0 :
        BMI_Class = "Normal"
    else :
        BMI_Class = "Over Weight"

    print("BMI = " + str(BMI))
    print("You are : " + BMI_Class)

calculate_bmi(weight=47, height=1.73)