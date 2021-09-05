function quickSort(array) {
  var low = [];
  var same = [];
  var high = [];

  if (array.length-1 < 2)
    return array;

  var pivot = array[array.length-1];

  for(var i = 0; i < array.length; i++){
    if (array[i] < pivot){
      low.push(array[i]);
    }
    else if(array[i]===pivot){
      same.push(array[i]);
    }
    else if(array[i] > pivot) {
      high.push(array[i]);
    }
  }

  return quickSort(low).concat(same).concat(quickSort(high));
  
}

console.log(quickSort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))