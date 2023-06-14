import ex2_prac as lab2_ex2

def test_min_max_temperature():
    input_temp = [10.3, 5.5, 15.7, 27.9]
    result_min, result_max = lab2_ex2.min_max_temperature(input_temp)
    test_min, test_max = 5.5, 27.9

    assert(result_min == test_min)
    assert(result_max == test_max)

def test_calc_average():
    input_temp = [10.3, 5.5, 15.7, 27.9]
    result = lab2_ex2.calc_average(input_temp)
    test = 14.85

    assert(result == test)

def test_calc_median_temperature():
    input_temp = [3.5, 4.7, 10.8, 20.4, 25.9]
    result = lab2_ex2.calc_median_temperature(input_temp)
    test = 10.8

    assert(test == result)