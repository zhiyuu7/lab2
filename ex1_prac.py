def calculate_bmi(height,weight):
    print("Height: " + str(height))
    print("Weight: " + str(weight))
    bmi = float(weight) / float(height * height)
    print("BMI = " + str(round(bmi,2)))


    if bmi > 25.0:
        print("BMI: " + str(round(bmi, 2)) + ", Over Weight")
        return 1
    elif bmi >= 18.5 and bmi <= 25.0:
        print("BMI: " + str(round(bmi, 2)) + ", Normal Weight")
        return 0
    else:
        print("BMI: " + str(round(bmi, 2)) + ", Under Weight")
        return -1
