import bmi

print("Test_bmi")

def test_calculate_bmi_underweight():
    result = bmi.calculate_bmi(1.73,57)
    assert result == 0
