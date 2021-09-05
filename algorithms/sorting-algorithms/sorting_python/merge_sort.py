
def merge_sort(arr):
    
    if len(arr) <= 1:
        return
        
    mid = len(arr)//2

    l = arr[mid:]
    r = arr[:mid]

    merge_sort(l)
    merge_sort(r)

    i,j,k = 0,0,0

    while(i < len(l) and j < len(r)):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    
    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1
    
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1
    
    return arr

arr = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]

print(merge_sort(arr))