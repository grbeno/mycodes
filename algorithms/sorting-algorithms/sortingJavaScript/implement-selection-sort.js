function selectionSort(array) {
  for(var i = 0; i < array.length; i++){
    var min_index = i;
    for(var j = i + 1; j < array.length; j++){
      if (array[min_index] > array[j]){
        min_index = j;
      }
    swap(array,min_index,i);
    }
  }
  return array;
}

function swap(array,x,y){
  let temp = array[x];
  array[x] = array[y];
  array[y] = temp;
}

console.log(selectionSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]));