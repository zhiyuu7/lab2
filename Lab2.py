def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    temp_list = get_user_input()
    calc_average(temp_list)
    find_min_max(temp_list)
    calc_median_temperature(temp_list)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    values = input("Enter a list of Temperatures separated by commas: ")
    temperatures = values.split(",")
    temp_list = [float(x) for x in temperatures]
    """creates a new list, use square brackets to define contents of list
    print(temp_list) 
    float(x) transforms each element in 'temperatures'
    'for x in temperatures': loop that iterates over each element in 'temperatures'
    """
    print(temp_list)
    return temp_list


def calc_average(mylist):
    total = sum(mylist)
    avg = total / len(mylist)
    print("The average is: ", avg)
    return avg


def find_min_max(mylist):
    minvalue = mylist[0]
    maxvalue = mylist[0]
    for num in mylist:
        if num < minvalue:
            minvalue = num
        if num > maxvalue:
            maxvalue = num
    print("The minimum temperature is: ", minvalue)
    print("The maximum temperature is: ", maxvalue)
    return minvalue, maxvalue


def calc_median_temperature(mylist):
    import statistics
    num = mylist
    num.sort()
    median = statistics.median(num)
    print("The median temperature is ", median)
    return median


if __name__ == "__main__":

    main()
