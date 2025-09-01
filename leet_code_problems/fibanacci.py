
def fibonacci(num):

    if num in [0,1]:
        return [num]


    prev, prev2 = 0, 1
    i = 1
    fib_series = [prev,prev2]
    while i  <= num:
        cur = prev+prev2
        prev, prev2 = prev2, cur
        fib_series.append(cur)
        i += 1
    return fib_series



FibArray = [0, 1]


def fibonacci_backtracking(n):
    # Check is n is less than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is less than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:
        FibArray.append(fibonacci_backtracking(n - 1) + fibonacci_backtracking(n - 2))
        return FibArray[n]

if __name__ == "__main__":
    print(fibonacci(2))

