from mathp import *

def get_sum(*args, **kwargs):
    sum = 0
    
    for i in args:
        try:
            sum += i
        except TypeError as e:
            pass

    return sum

def read_data():
    value = input('value: ')
    try:
        return int(value)
    except ValueError:
        print("not a number")
        return 0

# test get_sum
print("problem 1:")
print(get_sum(1, 5, -3, 'abc', [12, 56, 'cad']))
print(get_sum())
print(get_sum(2, 4, 'abc', param_1=2))

# test number retrieval
print("problem 2:")
print(read_data())

# test recursive
print("problem 3:")
print(sum_n(5))
print(sum_n_even(5))
print(sum_n_odd(5))