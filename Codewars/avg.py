def avg_array(arrs):
    result = []
    n = 0
    summa = 0
    for arr in arrs:
        summa += arr[n]

    return result


Test.assert_equals(avg_array([[1, 2, 3, 4], [5, 6, 7, 8]]), [3, 4, 5, 6])
Test.assert_equals(avg_array([[2, 3, 9, 10, 7], [12, 6, 89, 45, 3], [9, 12, 56, 10, 34], [67, 23, 1, 88, 34]]), [22.5, 11, 38.75, 38.25, 19.5])
Test.assert_equals(avg_array([[2, 5, 4, 3, 19], [2, 5, 6, 7, 10]]), [2, 5, 5, 5, 14.5])
Test.assert_equals(avg_array([[1.2, 8.521, 0.4, 3.14, 1.9], [2, 4.5, 3.75, 0.987, 1.0]]), [1.6, 6.5105, 2.075, 2.0635, 1.45])