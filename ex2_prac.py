def main():
    print("Lab 2 prac")
    display_main_menu()
    temp_list = get_user_input()
    calc_average(temp_list)
    min_max_temperature(temp_list)


def display_main_menu():
    print("Enter some numbers separated by commas")

def get_user_input():
    temp_values = input(print("Input some temperature values separated by commas here: "))
    temp_separated = temp_values.split(",")
    temp_list = [temp_separated]
    print("List of temperature values: " + str(temp_list))
    return temp_list

def calc_average(temp_list):
    sum_list = sum(temp_list)
    avg = sum_list / float(len(temp_list))
    print("Average: " + str(avg))
    return avg

def min_max_temperature(temp_list):
    min_value = min(temp_list)
    max_value = max(temp_list)
    print("Minimum value: " + str(min_value))
    print("Maximum value: " + str(max_value))
    return min_value,max_value


if __name__ == "__main__":

    main()
