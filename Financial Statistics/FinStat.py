from math import log
from math import sqrt
import os

dataset = [1, 2, 0, 0, -1, 0, 2]
program_active = True

def main(params = 0):
    print('Hello there,')
    print("""

    Welcome to the Financial Statistics Calculator!
    Enter a number to choose calculation:
    1.- Simpe Return
    2.- Logarithmic Return
    3.- Convert Returns
    4.- Variance 
    5.- Standart Deviation
    6.- Correlation
    E.- Exit
    """)
    user_calc = input('Number: ')

    if user_calc == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('SIMPLE RETURN')
        start_price = input('Start price: ')
        end_price = input('End price: ')
        dividend = input('Dividends (Enter "0" if no dividends were paid): ')
        simple_return = calculate_simple_return(start_price, end_price, dividend)
        print('Simple return of investment is ', display_as_percentage(simple_return))
    elif user_calc == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('LOGARITHMIC RETURN')
        start_price = input('Start price: ')
        end_price = input('End price: ')
        log_return = calculate_log_return(start_price, end_price)
        print('Logarithmic return of investment is ', display_as_percentage(log_return))
    elif user_calc == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('CONVERT RETURNS')
        print('Type each rate of return to create a list. Type "done" when the list is finished.')
        returns_list = []
        element_count = 1
        while True:
          input_statement = 'Type elemnt number ' + str(element_count) + ': '
          return_input = input(input_statement)
          if return_input == 'done':
            break
          else:
            returns_list.append(float(return_input))
            element_count += 1

        print('List:', returns_list)
        print('')

        t = input('Amount of old periods that fit in the new time frame:')
        result = convert_returns(returns_list, t)
        print('The average converted return is', display_as_percentage(result))
    elif user_calc == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('DATA VARIANCE')
        print('Type each number to create a list. Type "done" when the list is finished.')
        data_list = []
        element_count = 1
        while True:
          input_statement = 'Type elemnt number ' + str(element_count) + ': '
          data_input = input(input_statement)
          if data_input == 'done':
            break
          else:
            data_list.append(float(data_input))
            element_count += 1

        print('List:', data_list)
        print('')
        print('Variance:', calculate_variance(data_list))
    elif user_calc == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('DATA STANDART DEVIATION')
        print('Type each number to create a list. Type "done" when the list is finished.')
        data_list = []
        element_count = 1
        while True:
          input_statement = 'Type elemnt number ' + str(element_count) + ': '
          data_input = input(input_statement)
          if data_input == 'done':
            break
          else:
            data_list.append(float(data_input))
            element_count += 1

        print('List:', data_list)
        print('')
        print('Standart Deviation:', calculate_stddev(data_list))
    elif user_calc == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('DATA CORRELATION')
        print('Type each number to create the FIRST list. Type "done" when the list is finished.')
        data_list_1 = []
        element_count = 1

        while True:
          input_statement = 'Type elemnt number ' + str(element_count) + ': '
          data_input = input(input_statement)
          if data_input == 'done':
            element_count = 1
            break
          else:
            data_list_1.append(float(data_input))
            element_count += 1
        
        print('')
        print('Type each number to create the SECOND list. Type "done" when the list is finished.')
        data_list_2 = []
        while True:
          input_statement = 'Type elemnt number ' + str(element_count) + ': '
          data_input = input(input_statement)
          if data_input == 'done':
            element_count = 1
            break
          else:
            data_list_2.append(float(data_input))
            element_count += 1

        print('List 1:', data_list_1)
        print('List 2:', data_list_2)
        print('')
        print('Correlation:', calculate_correlation(data_list_1, data_list_2))
    elif user_calc == 'E':
        print('Bye!')
        program_active = False
        return program_active
    else:
        print('Invalid input or function not yet supported')

def display_as_percentage(val):
  percentage = round(val*100, 1)
  return str(percentage) + "%"

def calculate_simple_return(start_price, end_price, dividend = 0):
  return (float(end_price) - float(start_price) + float(dividend)) / float(start_price)

def calculate_log_return(start_price, end_price):
  return log(float(end_price)) - log(float(start_price))

# t is the amount of old periods that fit in the new time frame
def annualize_return(log_return, t):
  return log_return*t

# t is the amount of old periods that fit in the new time frame
def convert_returns(log_returns, t):
  summation = 0
  for rate in log_returns:
    summation += rate
  average = summation/len(log_returns)
  return average*int(t)

def calculate_variance(dataset):
  mean = sum(dataset)/len(dataset)

  numerator = 0
  for number in dataset:
    op = (number - mean)**2
    numerator += op
  variance = numerator/len(dataset)
  return variance

def calculate_stddev(dataset):
  variance = calculate_variance(dataset)
  stddev = sqrt(variance)
  return stddev

def calculate_correlation(set_x, set_y):
  # Sum of all values in each dataset
  sum_x = sum(set_x)
  sum_y = sum(set_y)

  # Sum of all squared values in each dataset
  sum_x2 = sum([x ** 2 for x in set_x])
  sum_y2 = sum([y**2 for y in set_y])

  # Sum of the product of each respective element in each dataset 
  sum_xy = sum([element_x*element_y for element_x, element_y in zip(set_x, set_y)])

  # Length of dataset
  n = len(set_x)

  # Calculate correlation coefficient
  numerator = n * sum_xy - sum_x * sum_y
  denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))
  return numerator / denominator

while program_active:
    if main() == False:
        break
