def main():
    calculate_bmi(height=1.73, weight=57)


def calculate_bmi(height, weight):
    print("Height = ", str(height))
    print("Weight = ", str(weight))

    bmi = weight / (height * height)
    if bmi < 18.5:
        classification = "Under Weight"
        print("BMI value = " + str(bmi))
        print(classification)
        return -1
    if bmi >= 18.5 <= 25.0:
        classification = "Normal Weight"
        print("BMI value = " + str(bmi))
        print(classification)
        return 0
    if bmi > 25.0:
        classification = "Over Weight"
        print("BMI value = " + str(bmi))
        print(classification)
        return 1


if __name__ == "__main__":

    main()
