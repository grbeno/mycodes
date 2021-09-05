
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j # find the minimum
        arr[i], arr[min_index] = arr[min_index], arr[i] # swap minimum and current
    return arr

arr = [9,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]

print(selection_sort(arr))