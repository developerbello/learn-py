function recusive_binary_search($lists, $target) {
  $first = 0;
  $last = count($lists) - 1;

  while($first <= $last) {
    $midpoint = ($first + $last) >> 1;

    if($lists[$midpoint] == $target) {
      return $midpoint; 
    } elseif ($lists[$midpoint] > $target) {
      $last = $midpoint - 1;
    } elseif ($lists[$midpoint] < $target) {
      $first = $midpoint + 1
    }
  }

  return -1
}

function verify($index) {
  if($index !== null){
    echo("Index Found: ", $index);
  } else {
    echo("Index not found");
  }
}


$numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
$result = binary_search(numbers, 11)
verify(result)
$result2 = binary_search(numbers, 5)
verify(result2)
