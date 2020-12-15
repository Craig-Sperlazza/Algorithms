# https://www.youtube.com/watch?v=vuOpxXeFjg8&list=PLEJyjB1oGzx2h88Tj90B5_HadLq339Cso&index=5
#best O(n)
#worst/avg O(n^2)
#space O(1)

#I made the bubble sort myself----he used a while loop

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

if __name__ =="__main__":
    from random import randint
    from time import time

    def create_array(length=10, maxint=50):
        new_arr = [randint(0, maxint) for _ in range(length)]
        return new_arr

    #simple test
    test = create_array()
    print(test)
    test = bubble_sort(test)
    print(test)

    #ensure sorted test (compare our algorithim with built in sort function)
    #returns True if the passed in array is sorted
    def is_sorted(arr):
        sorted_arr = sorted(arr)
        return arr == sorted_arr
    print(is_sorted(test))

    #benchmark our bubble sort versus python's built in sort function
    def benchmark(n=[10, 100, 1000, 10000]):
        #list of each of our bubble sort times
        bubble_times = []
        #list of each of the built in sort times
        built_in_times = []

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

        #print times in table format
        print("n \t Built_in_Sort \tBubble_Sort")
        print("_______________________________________")
        for i, cur_n in enumerate(n):
            # print("%d\t%0.5f \t%0.5f"%(cur_n, built_in_times[i], bubble_times[i]))
            print(f"{cur_n} \t {built_in_times[i]:.5f} \t {bubble_times[i]:.5f}")
    benchmark()
