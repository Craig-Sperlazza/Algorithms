# https://www.youtube.com/watch?v=qktBUYMO7o8&list=PLEJyjB1oGzx2h88Tj90B5_HadLq339Cso&index=7

#insertion sort goes faster at the end....good for inserting an item into a sorted list
#best O(n)
#worst, avg O(n^2)
#space (inplace so...) O(1)

#This insertion sort came from p.215 problem solving algorithms, his is same.

def insertion_sort(arr):
    for index in range(1, len(arr)):
        curr_val = arr[index]
        position = index
        
        while position > 0 and arr[position - 1] > curr_val:
            #you basically shift the lower value to the right (but technically the lower value remains in both positions until the while loop breaks)
            arr[position] = arr[position - 1]
            position = position - 1
    
        arr[position] = curr_val
    return arr



if __name__ == "__main__":
    from random import randint
    from bubble import bubble_sort
    from selection import selection_sort, selection_sort2
    from time import time


    #create array
    def create_array(size=10, max=50):
        return [randint(0,max) for _ in range(size)]
    
    #test array creation and sort
    print("----------------Testing array creation and insertion sort-----------------")
    b = create_array()
    a = create_array(4, 50)
    print(a)
    print(insertion_sort(a))
    print(b)
    print(insertion_sort(b))

    #make sure bubble sort imported correctly
    print("----------------Testing bubble sort---------------------------------------")
    c = create_array()
    print(c)
    print(bubble_sort(c))

    #make sure selection sort imported correctly
    print("----------------Testing selection sort------------------------------------")
    c = create_array()
    print(c)
    print(selection_sort(c))

     #make sure selection sort ver 2 imported correctly
    print("----------------Testing selection sort ver2------------------------------------")
    d = create_array()
    print(d)
    print(selection_sort2(d))

    print()
    print("----------------Benchmark Test -------------------------------------------")
    #benchmark test of insertion versus selection versus bubble versus built in
    
    def benchmark(n=[10, 100, 1000, 10000, 25000]):
        #list of each of our bubble sort times
        bubble_times = []
        #list of each of the built in sort times
        built_in_times = []
        #list of each of the selection sort times
        selection_times = []
        #list of each of the selection sort2 times
        selection_times2 = []
        #list of each of the insertion sort times
        insertion_times = []

        for length in n:
            alist = create_array(length, length)

            #sort with built in and append times
            start = time()
            s = sorted(alist)
            end = time()
            built_in_times.append(end - start)

            # sort with bubble sort and append times
            start = time()
            b = bubble_sort(alist)
            end = time()
            bubble_times.append(end - start)

            # sort with selection sort and append times
            start = time()
            se = selection_sort(alist)
            end = time()
            selection_times.append(end - start)

            # sort with selection sort and append times
            start = time()
            se2 = selection_sort2(alist)
            end = time()
            selection_times2.append(end - start)

            # sort with insertion sort and append times
            start = time()
            i = insertion_sort(alist)
            end = time()
            insertion_times.append(end - start)

        #print times in table format
        print("n \t Built_in_Sort \tBubble_Sort \tSelect_Sort \tSelect_Sort2 \tInsertion_Sort")
        print("____________________________________________________________________________")
        for i, cur_n in enumerate(n):
            # print("%d\t%0.5f \t%0.5f"%(cur_n, built_in_times[i], bubble_times[i]))
            print(f"{cur_n} \t {built_in_times[i]:.5f} \t {bubble_times[i]:.5f} \t {selection_times[i]:.5f} \t {selection_times2[i]:.5f} \t {insertion_times[i]:.5f}")
    benchmark()