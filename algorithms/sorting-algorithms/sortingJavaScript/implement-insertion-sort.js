function insertionSort(array) {
  for(var i = 1; i < array.length; i++) {
    var current = array[i];
    var j = i - 1;
    while(current < array[j]){
       array[j+1] = array[j];  
       j--;
    }
    array[j + 1] = current;
  }
  
  return array;
  
}

console.log(insertionSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]));