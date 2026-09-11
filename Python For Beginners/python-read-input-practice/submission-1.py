def add_two_numbers() -> int:
    string_list = input().split(",")
    sum = 0

    for string in string_list:
        sum += int(string)

    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
