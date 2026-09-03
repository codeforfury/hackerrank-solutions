# Print the Elements of a Linked List

**Difficulty:** Easy
**Category:** data-structures
**Language:** python3
**Link:** https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

---

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

```
STDIN   Function
-----   --------
2       n = 2
16      first data value = 16
13      second data value = 13
```

Sample Output

```
16
13
```

Explanation

There are two elements in the linked list. They are represented as 16 -> 13 -> NULL. So, the  function should print 16 and 13 each on a new line.
