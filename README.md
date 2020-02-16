# LeetCode_py
DP: 39

01/26/2020
518 - Coin Change 2
377 - Combination Sum 4
Same idea, find out how many ways to reach the target using previous
record. See 518


01/27/2020
213 - House Robber 2


01/29/2020
33 - Search in Rotated Sorted Array
153 - Find Minimum in Rotated Sorted Array
Same idea, split array in 2 half, there's always one half is sorted
find target based on binary search

01/30/2020
48 - RotateImage
153 - SpiralMatrix
Rotate matrix clockwise by 90 degree. first flip the matrix, the exchange symmetrically
153 is straight forward


01/31/2020
75 - SortColors
167 - TwoSum2
DCP 
75 is a two pointer question, using p1 p2 points to start and end
if current item is 0, then swap with start,
if current item is 2, swap with end.
167 is same idea

02/01/2020
16 -3SumClosest
344 - ReverseString
16 is similar to yesterday's question:
for each element at index i in the list, go through the i+1th to last element in the list. Find out what is the closest.

02/04/2020
18 - 4Sum
19 - RemoveNthFromList
18 is using recursive way to solve k-1 sum, the base case is 2 sum algorithm, very clever. 
19 is similar to fast and slow pointer problem, but here N is the distance between 2 pointers.

02/09/2020
287 - FindDuplicateNumbers
142 - LinkedListCycle2
Both problem can be solved using two pointers and Floyd Cycle detection algorithm.
First, find out if there are cycles, by using fast and slow pointers, name this the meet point
Then from start to cycle's starting point, and from meet point to cycle's starting point, they must have same distances

02/16/2020
22 - Generate Parentheses
17 - LetterCombinationsOfPhoneNumbers
Backtracking: Choice, Constraints, and Goal
Q22 Use recursive function, choice is either add a '(' or ')', constraints are:
1. ( is more than ) 
2. ) is more than (
goal is when length of the result == 2*length of limit. 
Q17 Same thing. Choice is the corresponding letters of each digit, e.g. 2 corresponds
to a, b, c. Constraints are these letters that we are allowed to choose from. Goal is 
when the length of our combination == length of digits
