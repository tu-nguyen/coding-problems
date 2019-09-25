// Title: Decode the Morse code
// Rank: 6 kyu
// Language Version: JavaScript Node v8.1.3

// Instructions //
// ...
// Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.
// For example:
// decodeMorse('.... . -.--   .--- ..- -.. .')
// //should return "HEY JUDE"
// ...
//
// Solution //
decodeMorse = function(morseCode){
  code = morseCode.split(" ");
  
  var i;
  var res = "";
  for (i = 0; i < code.length; i++) {
    if (code[i] == '') {// && code[i + 1] == '') {
      res = res.concat(" ");
      while (code[i + 1] == '') {
        i++;
      }
    else {
      res = res.concat(MORSE_CODE[code[i]]);
    }
  }
  return res.trim();
}

// Test Case //
Test.describe("Example from description", function(){
Test.assertEquals(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
});

Test.describe("Your own tests", function(){
// Add more tests here
});