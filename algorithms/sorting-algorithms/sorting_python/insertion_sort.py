
def insertion_sort(array):
    for i in range(1,len(array)):
        current = array[i]
        j = i - 1
        while(current < array[j]):
            array[j+1] = array[j] # moving up the greater one step!
            j -= 1
        array[j+1] = current # moving up current bacause j is decremented!
    
    return array

arr = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]

print(insertion_sort(arr))