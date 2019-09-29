// Title: Isograms
// Rank: 7 kyu
// Language Version: JavaScript Node v8.1.3

// Instructions //
// An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
// isIsogram("Dermatoglyphics") == true
// isIsogram("aba") == false
// isIsogram("moOse") == false // -- ignore letter case
//
// Solution //
String.prototype.count = function (c) {
  var res = 0;
  for (j = 0; j < this.length; j++) {
    if(this[j] == c) {
      res++;
    }
  }
  return res;
};

function isIsogram(str){
  str = str.toLowerCase();
  if (str == "") {
    return true;
  }
  else {
    for (i = 0; i < str.length; i++) {
      if (str.count(str[i]) >= 2) {
        return false;
      }
    }
  }
  return true;
}

// Test Case //
Test.assertSimilar( isIsogram("Dermatoglyphics"), true );
Test.assertSimilar( isIsogram("isogram"), true );
Test.assertSimilar( isIsogram("aba"), false, "same chars may not be adjacent" );
Test.assertSimilar( isIsogram("moOse"), false, "same chars may not be same case" );
Test.assertSimilar( isIsogram("isIsogram"), false );
Test.assertSimilar( isIsogram(""), true, "an empty string is a valid isogram" );
