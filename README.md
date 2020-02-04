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