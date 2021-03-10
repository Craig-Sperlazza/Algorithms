# def max_sum_two_nums(arr):
#     if len(arr) == 0:
#         return print("No elements")
#     else:
#         largest_sum = 0
#         largest_num = arr[0]

#         for i in arr:
#             if i > largest_num:
#                 largest_num = i
#         arr.remove(largest_num)

#         for j in arr:
#             if largest_num + j > largest_sum:
#                 largest_sum = largest_num + j
        
#     return largest_sum

def max_sum(arr):
    if len(arr) == 0:
        return print("No elements")
    
    max_sum = arr[0]
    curr_sum = arr[0]

    for num in arr[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)
    
    return max_sum


if __name__ == "__main__":

    arr1 = [1, 2, 4, 5, 6, 2, 3]
    arr2 = [-3, -8, 19, 3, 4, 2]

    print(max_sum(arr1))
    print(max_sum(arr2))

