# Print the Elements of a Linked List

**Difficulty:** Easy
**Category:** data-structures
**Language:** python3
**Link:** https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

---

|
PrepareData StructuresLinked ListsPrint the Elements of a Linked List
Exit Full Screen View
Problem	Submissions	Leaderboard	Discussions	Editorial

This challenge is part of a MyCodeSchool tutorial track and is accompanied by a video lesson.

This exercise focuses on traversing a linked list. You are given a pointer to the  node of a linked list. The task is to print the  of each node, one per line. If the head pointer is , indicating the list is empty, nothing should be printed.

Function Description

Complete the  function with the following parameter(s):

: a reference to the head of the list

Print

For each node, print its  value on a new line (console.log in Javascript).

Input Format

The first line of input contains , the number of elements in the linked list.
The next  lines contain one element each, the  values for each node.

Note: Do not read any input from stdin/console. Complete the printLinkedList function in the editor below.

Constraints

, where  is the  element of the linked list.

Sample Input

STDIN   Function
-----   --------
2       n = 2
16      first data value = 16
13      second data value = 13


Sample Output

16
13


Explanation

There are two elements in the linked list. They are represented as 16 -> 13 -> NULL. So, the  function should print 16 and 13 each on a new line.

Change Theme
Language
Python 3
More
1
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
#!/bin/python3
# Complete the printLinkedList function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next
        
if __name__ == '__main__':
Line: 29 Col: 1
Submit Code
Run Code
Upload Code as File
Test against custom input
Test case 0
Test case 1
Test case 2
Test case 3
Test case 4
Test case 5
Test case 6
Test case 7
Test case 8
Loading testcase ...
