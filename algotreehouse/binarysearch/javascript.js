function binary_search(lists, target) {
  let first = 0
  let last = lists.length - 1;

  while(first <= last) {
    let midpoint = first + Math.floor((last - first)/2);
    
    if(lists[midpoint] === target) {
      return midpoint;
    } else if(lists[midpoint] < target) {
      first = midpoint + 1;
    } else {
      last = midpoint - 1;
    }
  }

  return null;
}

function verify(index) {
  if(index !== null){
    console.log("Index Found: ", index);
  } else {
    console.log("Index not found");
  }
}

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let result = binary_search(numbers, 11)
verify(result)
let result2 = binary_search(numbers, 5)
verify(result2)
