
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [9,4,2,8,345,123,43,-32,5643,63,123,43,2,55,1,234,92]

print(bubble_sort(arr))