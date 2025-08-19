def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr

if __name__ == "__main__":
    print(bubble_sort([2,3,5,1,4,6,7,3,5,6, -1,0]))


"""
In bubble sort we just compare the next element with the current element if it greater than we will interchange the 
elements and in each iteration we will be sorting the higher element at the end so the name bubble sort 

Time complexity = O(n2)
space complexity = O(1)
"""