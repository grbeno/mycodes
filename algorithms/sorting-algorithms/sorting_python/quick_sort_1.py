# pivot options:
# first,last, random, middle element
# selected pivot last element

def partition(arr,low,high):
    i = low - 1  # 0 - 1
    pivot = arr[high]  # len(arr)-1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # put smaller elements to the first part of the array 
    arr[i+1], arr[high] = arr[high], arr[i+1]  # put the pivot to its place to crate two partitions
    return i+1

def quick_sort(arr,low,high):
    if low < high:
        partition_index = partition(arr,low,high)
        # sorting the part of smaller elements
        quick_sort(arr,low,partition_index-1)
        # sorting the part of greater elements
        quick_sort(arr,partition_index+1,high)


arr = [1,4,2,8,345,123,43,32,-5643,63,123,43,2,55,1,234,92]
low = 0
high = len(arr)-1
quick_sort(arr,low,high)
print(arr)