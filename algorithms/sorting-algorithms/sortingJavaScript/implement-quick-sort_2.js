function partition(array,low,high){
  var i = low - 1;
  var pivot = array[high];
  for(var j = low; j < high; j++){
    if (array[j] <= pivot){
      i++;
      swap(array,i,j);
    }
  }
  swap(array,i+1,high);
  return i+1;
}

function swap(array,x,y){ 
  let temp = array[x];
  array[x] = array[y];
  array[y] = temp;
}

function sorting(array,low,high) {
  if (low < high) { 
    var partitionIndex = partition(array,low,high);
    sorting(array,low,partitionIndex-1);
    sorting(array,partitionIndex+1,high);
  }
}

function quickSort(array){
  var low = 0;
  var high = array.length-1;
  sorting(array,low,high);
  return array;
}

var array = [1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92];

console.log(quickSort(array));

