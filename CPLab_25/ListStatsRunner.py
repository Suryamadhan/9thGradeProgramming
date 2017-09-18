"""========================================================
Lab_24.1        List Stats
---------
 * In this lab you will write a program that determines
 * how many groups of a specified size exists in a list.
 * For example, in the list  [1,1,1,2,2,2,3,3,3,4,5,6,7],
 * there are 7 groups with at least one, 3 groups with at
 * least 2, and 3 groups with at least 3.
 * A group is a series of same values. for example, 1 1 1
 * is a group of 3, but it also is a group of 1 and 2.
 * To count as a group, all values must be the same.
=========================================================="""

from ListStats import *
test = ListStats("3 3 3 3 3 9 4 4 4 5 5 5 5 6 6 7 7 7 8 8 8 8 8 8 8 8")
print("\n")
print(test)
print("Size 1 count == ", test.getNumGroupsOfSize(1))
print("Size 2 count == ", test.getNumGroupsOfSize(2))
print("Size 3 count == ", test.getNumGroupsOfSize(3))
print("Size 4 count == ", test.getNumGroupsOfSize(4))
print("Size 5 count == ", test.getNumGroupsOfSize(5))
print("Size 5 count == ", test.getNumGroupsOfSize(6))

test.setList("1 2 3 4 5 6 7 8 9")
print("\n")
print(test)
print("Size 1 count == ", test.getNumGroupsOfSize(1))
print("Size 2 count == ", test.getNumGroupsOfSize(2))
print("Size 3 count == ", test.getNumGroupsOfSize(3))
print("Size 4 count == ", test.getNumGroupsOfSize(4))
print("Size 5 count == ", test.getNumGroupsOfSize(5))
print("Size 5 count == ", test.getNumGroupsOfSize(6))

