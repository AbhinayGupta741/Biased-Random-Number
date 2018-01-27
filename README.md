# Biased-Random-Number

Write a custom random number generation algo which should be 73% biased to the higher number.
Like if I want a random number between 1 to 10 100times then it should give number more than 5 73times and less than 5 27times.

Algorithm-

1)Import time and math

2)Taking values of add,multi,mod for random number generation based on Linear Congruential Generator Algorithm

3)define random_number function

4)Take minimum and maximum range and find there mid value

5)create two list with there range of 73 and 27 respectively.

     a)below
     
     b)above
     
 and merge them into final list 
 
6)print random position from final list
