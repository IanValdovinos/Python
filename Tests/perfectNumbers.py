
def classify_number(number):
    integer = 1
    integer_sum = 0
    while integer < number:
        if number % integer == 0:
            integer_sum += integer
        integer += 1

    if integer_sum == number:
        return 'perfect'
    elif integer_sum < number:
        return 'deficient'
    elif integer_sum > number:
        return ' abundant'


def classify_number_list(upper_bound):
    number = 2
    number_dict = {}
    while number <= upper_bound:
        number_category = classify_number(number)
        number_dict[number] = number_category
        number += 1

    return number_dict


def get_ony(category, dict):

    number_lst = [number for number, cat in dict.items() if cat == category]
    return number_lst


upper_bound = int(input('Enter an upper bond: '))
print('Lower bound:', 2)
print('Upper bound:', upper_bound)

number_dict = classify_number_list(upper_bound)
for number, category in number_dict.items():
    message = 'The number {} is {}.'.format(number, category)
    print(message)

print('Perfect numbers:', get_ony('deficient', number_dict))




