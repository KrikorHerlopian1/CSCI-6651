# CSCI-6651

A module named randStr.py that has 3 functions.
Each function has an optional second parameter to set a particular seed.

1) randWord accepts a string and will return a random word from that string (return value is string).
2) strMixer will randomly change words inside the string and returns a string
-- If the string is only one word, then it will mix the letters of the word and return the mixed word as a string
3) randIntForWord accepts a word and then returns a random integer between 0 and 100,000; the same word should return the same random integer.

The 3 functions are imported in the main file and called each of them 5 times (with and without seed).

If the module is called directly, the following message is printed: 
"Sorry, but this module can only be imported!"

