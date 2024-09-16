// Title: Convert a Number to a String!
// Rank: 8 kyu
// Language Version: Clang 8 / C18

// Instructions //
// We need a function that can transform a number into a string.
// What ways of achieving this do you know?
// In C, return a dynamically allocated string that will be freed by the test suite.
// Examples:
// number_to_string(123) // "123"
// number_to_string(999) // "999"
//
// Solution //


// Test Case //
#include <criterion/criterion.h>

const char* number_to_string(int number);
void tester(int number, const char* expected);

Test(Sample_Case, should_return_number_as_string) {
    tester(123, "123");
    tester(999, "999");
}