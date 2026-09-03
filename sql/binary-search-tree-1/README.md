# Binary Tree Nodes

**Difficulty:** Medium
**Category:** sql
**Language:** db2
**Link:** https://www.hackerrank.com/challenges/binary-search-tree-1/problem

---

You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

![image](images/01-1443818507-5095ab9853-1.png)

Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

Root: If node is root node.
Leaf: If node is leaf node.
Inner: If node is neither root nor leaf node.

Sample Input

![image](images/02-1443818467-30644673f6-2.png)

Sample Output

```
1 Leaf
2 Inner
3 Leaf
5 Root
6 Leaf
8 Inner
9 Leaf
```

Explanation

The Binary Tree below illustrates the sample:

![image](images/03-1443773633-f9e6fd314e-simply_sql_bst.png)
