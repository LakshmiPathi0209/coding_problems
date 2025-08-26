def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    lower_left = [x for x in arr if x < pivot]
    middle = [pivot]
    higher_left = [x for x in arr if x > pivot]

    return  quick_sort(higher_left) + middle + quick_sort(lower_left)

print(quick_sort([5, 4,12,3,45, 3, 2, 1]))


"""
time complexity of quick sort is O (n log n)

Working:
    I follows divide and conquer algorithm, in each iteration we fill find the pivot element (usually the frst element)
    and find the all element which is less than the pivot to the left and the greater than pivot to the left, And will 
    pass the left and right subset of the element to the same function

"""