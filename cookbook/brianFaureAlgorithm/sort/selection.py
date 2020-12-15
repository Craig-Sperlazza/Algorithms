# https://www.youtube.com/watch?v=JxTghISBmI8&list=PLEJyjB1oGzx2h88Tj90B5_HadLq339Cso&index=6

#this is from book hands on p. 261
#note that it is very similar to bubble sort but it makes the second loop progressively smaller as i increases
#this is because we assume the first element is sorted, then the second, etc. 
#this selection sort2 outperforms the other one by about half

def selection_sort2(arr):
    size_of_list = len(arr)

    for i in range (size_of_list):
        for j in range (i+1, size_of_list):
            #if the number on the right is smaller, then we must swap
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr

def selection_sort(arr):
    #length of sorted array
    sorted_len = 0

    while sorted_len < len(arr):
        #index of the smallest item found in unsorted protion
        min_index = None      
        #iterate over the unsorted portion getting both the index and value
        for index, value in enumerate(arr[sorted_len:]):
            #during each iteration check to see if the current index is the smallest and if so we update the current smallest 
            if min_index == None or value < arr[min_index]:
                min_index = index + sorted_len
            
        #swap after each for loop---1 more item is sorted
        temp = arr[min_index]
        arr[min_index] = arr[sorted_len]
        arr[sorted_len] = temp
        sorted_len += 1
    
    return arr




if __name__ == "__main__":
    from random import randint
    from bubble import bubble_sort
    from time import time


    #create array
    def create_array(size=10, max=50):
        return [randint(0,max) for _ in range(size)]
    
    #test array creation and sort
    print("----------------Testing array creation and selection sort-------------")
    b = create_array()
    a = create_array(4, 50)
    print(a)
    print(selection_sort(a))
    print(b)
    print(selection_sort(b))

    #make sure bubble sort imported correctly
    print("----------------Testing bubble sort------------------------------------")
    c = create_array()
    print(c)
    print(bubble_sort(c))

    print("----------------Benchmark Test ----------------------------------------")
    #benchmark test of selection versus bubble and built in
    #benchmark our bubble sort versus python's built in sort function
    def benchmark(n=[10, 100, 1000, 10000]):
        #list of each of our bubble sort times
        bubble_times = []
        #list of each of the built in sort times
        built_in_times = []
        #list of each of the built in sort times
        selection_times = []

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

        #print times in table format
        print("n \t Built_in_Sort \tBubble_Sort \tSelection_Sort")
        print("____________________________________________________________________")
        for i, cur_n in enumerate(n):
            # print("%d\t%0.5f \t%0.5f"%(cur_n, built_in_times[i], bubble_times[i]))
            print(f"{cur_n} \t {built_in_times[i]:.5f} \t {bubble_times[i]:.5f} \t {selection_times[i]:.5f}")
    benchmark()

