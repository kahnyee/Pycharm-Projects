def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    BMI = weight/(height**2)

    if BMI < 18.5 :
        BMI_Class = "Under Weight"
        return -1
    elif 18.5 <= BMI <= 25.0 :
        BMI_Class = "Normal"
        return 0
    else :
        BMI_Class = "Over Weight"
        return 1

    print("BMI = " + str(BMI))
    print("You are : " + BMI_Class)

calculate_bmi(weight=57, height=1.73)