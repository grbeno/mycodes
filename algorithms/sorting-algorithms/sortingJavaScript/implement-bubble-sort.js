function bubbleSort(array) {
 for(var i = 0; i < array.length; i++) {
   for(var j = 0; j < array.length-i-1; j++) {
     if(array[j] > array[j+1])
      swap(array,j,j+1);
   }
 }
  return array;
}

function swap(arr,x,y) {
  let temp = arr[x];
  arr[x] = arr[y];
  arr[y] = temp;
}

console.log(bubbleSort([9,4,2,8,345,123,43,-32,5643,63,123,43,2,55,1,234,92]));