# def binSearch(lst, val):
#     if len(lst) == 0:
#         return False
#     if len(lst) == 1:
#         if lst[0] == val:
#             return True
#     else:
#         start = 0
#         end = len(lst) - 1
#         mid = (start + end) // 2 

#         if lst[mid] == val:
#             return True
#         elif (val > lst[mid]):
#             new = mid + 1
#             right_lst = lst[new:]
#             return binSearch(right_lst, val)
#         elif (val < lst[mid]):
#             new = mid
#             left_lst = lst[0:new]
#             return binSearch(left_lst, val)
#     return False
        
def binSearch(lst, val):
    length = len(lst)
    if length == 0:
        return False
    elif length == 1:
        if lst[0] == val:
            return True
    else:
        start = 0
        end = length - 1
        mid = (start + end)//2

        if lst[mid] == val:
            return True
        elif lst[mid] < val:
            new = mid + 1
            new_lst = lst[new:]
            return binSearch(new_lst, val)
        elif lst[mid] > val:
            new_lst = lst[0:mid]
            return binSearch(new_lst, val)
    return False
    



if __name__ == "__main__":
    test_list = [2, 4, 6, 8, 10, 12]

    print(binSearch(test_list, 14))
    print(binSearch(test_list, 1))
    print(binSearch(test_list, 5))
    print(binSearch(test_list, 2))
    print(binSearch(test_list, 4))
    print(binSearch(test_list, 6))
    print(binSearch(test_list, 8))
    print(binSearch(test_list, 10))
    print(binSearch(test_list, 12))



