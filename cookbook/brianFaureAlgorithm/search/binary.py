def binary_search(arr, val):
    """This is for integers, if you wanted to use a different data type you just change the >, < to custom compare functions"""

    #empty array or single value != target value
    if len(arr) == 0:
        #print("isnt here 0")
        return False
    
    elif len(arr) == 1 and arr[0] != val:
        #print("isnt here 1")
        return False
    
    #value at center of array
    mid = arr[len(arr) // 2]

    #3 cases: value is mid, value is less than mid, value is greater than mid

    if mid == val:
        #print("found it")
        return True
    
    elif val < mid:
        arr = arr[:len(arr) // 2]
        #print(arr)
        return binary_search(arr, val)
    
    else:
        arr = arr[len(arr) // 2 + 1:]
        print(arr)
        return binary_search(arr, val)


if __name__ == "__main__":
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(binary_search(test, 10))
    print(binary_search(test, 100))