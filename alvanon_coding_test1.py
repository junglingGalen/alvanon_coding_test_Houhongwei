"""
Rearrange an array of integers so that the calculated value U is maximized.
Among the arrangements that satisfy that test,
choose the array with minimal ordering.
The value of U for an array with n elements is calculated as
: U = arr[1]×arr[2]×(1÷arr[3])×arr[4]×...×arr[n-1] × (1÷arr[n]) if n is odd
or U = arr[1]×arr[2]×(1÷arr[3])×arr[4]×...×(1÷arr[n-1]) × arr[n] if n is even
The sequence of operations is the same in either case, but the length of the array, n,
determines whether the calculation ends on arr[n] or (1÷arr[n]).
Arrange the elements to maximize U and the items are in the numerically smallest possible order.
"""


def sort_array(array):
    array.sort()
    res = []
    for i in range(len(array)):
        if i % 2 == 0 and i != 0:
            res.append(array.pop(0))
        if i % 2 == 1 or i == 0:
            res.append(array.pop())
    return res


if __name__ == '__main__':
    test_arrays = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [],
        [8, 8, 8, 5, 5, 5]
    ]
    res_arrays = [
        [9, 8, 1, 7, 2, 6, 3, 5, 4],
        [],
        [8, 8, 5, 8, 5, 5]
    ]
    for i in range(len(test_arrays)):
        print(f"input：{test_arrays[i]}", f"output：{res_arrays[i]}")
        assert sort_array(test_arrays[i]) == res_arrays[i]
    print("Congratulations you have passed!")
