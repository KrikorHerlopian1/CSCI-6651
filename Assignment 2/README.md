A generic converter where the first parameter is “base” (2 <= base <= 16) ,
and then other parameters (flexible amount) are decimal integers. 

Based on the base, the other integers should be converted.
Parameters are integers and not a string / other objects

Input: 2, 5, 10, 3;     Return value: ['base=2', '101', '1010', '11']
Input: 8, 5, 10;        Return value: ['base=8', '5', '12']
Input: 17, 5, 10;       Return value: ['Wrong base']
Input: 16, 15, 40, 3.5; Return value: ['base=16', 'F', '28', 'NA']


The lists returned will only contain strings.Wrong base is returned as a list with one element.
The code is capable to convert any number between 2 and 16. Base 17 is invalid and out of range.