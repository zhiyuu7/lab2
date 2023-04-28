

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height * height)
    if bmi < 18.5:
        classification = "Under Weight"
    if bmi >= 18.5 and bmi <= 25.0:
        classification = "Normal Weight"
    if bmi > 25.0:
        classification = "Over Weight"

    print("BMI value = " + str(bmi))
    print(classification)
calculate_bmi(weight=57, height=1.73)

