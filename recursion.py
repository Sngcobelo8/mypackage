

def factorial(n):

    '''Return n!'''

    if n <= 1:
        return n
    else:
        return n * factorial(n-1)


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def sum_array(array):
    
    '''Return sum of all items in array'''

    if type(array) == int:
        return array

    sum = 0
    for i in array:
        if type(i) == list:
            sum = sum+sum_array(i)
        else:
            sum = sum+i
    return sum


def reverse(word):

    '''Return word in reverse'''

    reversal = word[::-1]
    return reversal
















