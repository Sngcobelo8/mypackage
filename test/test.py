from recursion import factorial, fibonacci, reverse, sum_array
from sorting import bubble_sort, merge_sort, quick_sort

def test_functions():
    """
    make sure all functions work correctly
    """
    
    assert factorial(4) == 24, 'incorrect'
    assert fibonacci(8) == 21, 'incorrect'
    assert reverse('A sentence that has to be reversed by the reverse function') == 'noitcnuf esrever eht yb desrever eb ot sah taht ecnetnes A', 'incorrect'
    assert sum_array([[5, 5], [20], [2, 1]]) == 33, 'incorrect'
    assert bubble_sort([59, 69,3,58,494,4,13,30]) == [59, 3, 58, 69, 4, 13, 30, 494], 'incorrect'

    #lists to test merge_sort function

    x = [34,5,2,6]
    y = [12,34,54,1]
    assert merge_sort(x+y) == [1, 2, 5, 6, 12, 34, 34, 54], 'incorrect' 
    assert quick_sort([5,6,3,7,11,44]) == [3, 5, 6, 7, 11, 44], 'incorrect'
