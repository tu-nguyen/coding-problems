// Title: Descending Order
// Rank: 7 kyu 
// Language Version: JavaScript Node v8.1.3

// Instructions //
// Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
// Examples:
// Input: 21445 Output: 54421
// Input: 145263 Output: 654321
// Input: 1254859723 Output: 9875543221
//
// Solution //
function descendingOrder(n){
  return parseInt(n.toString().split("").sort().reverse().join(""));
}

// Test Case //
Test.assertEquals(descendingOrder(0), 0)
Test.assertEquals(descendingOrder(1), 1)
Test.assertEquals(descendingOrder(123456789), 987654321)