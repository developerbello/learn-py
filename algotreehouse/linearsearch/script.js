function linearsearch(lists, target) {

  for(let i = 0; i < lists.length; i++) {

    if(lists[i] == target) {

      return i
    }
  }
  return -1
}

function verify(index) {
  console.log(index);
}

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let result = linearsearch(numbers, 6);
verify(result);
