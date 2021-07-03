We will start with graph and dp the two most dreaded topics and then come to 1D,2D arrays.
Graph : 
Binary tree
Binary search tree
Tree, nary tree
dag
matrix

Binary tree:
Representation:
	a) Nodes and children
	b) Array
1) Traversal, serialize = > 
	a) preorder  recursion, iterative
	b) inorder   recursion, iterative
	c) postorder recursion, iterative
	d) level or breadth-first
	e) vertical
	f) diagonal
	f) spiral
	g) boundary

	deserialize =>
	a) inorder, preorder
	b) inorder, postorder
	c) levelorder

2) Views
	a) bottom
	b) left
	c) right
	d) print all nodes as they become leaf
	e) connect

3) Computation
	a) LCA
	b) distance between 2 nodes
	c) max path sum
	d) max path sum leaf to leaf
	e) max path sum no adjacent nodes
	f) path sum
	g) path sum 2 
	f) path sum 3
	g) sum of only left nodes

4) convert a bt into:
	a) ll
	b) dll
	c) graph => compute all nodes present at k distance, time taken to burn a bt
	d) invert bt

5) Modify:
	a) reverse tree path. 
	b) 

6) two bt
	a) merge 2 bt
	b) bt is a subset of another bt
	c) 2 tree are isomorphic

7) Many bt
	a) given a number n, return all possible full bt with n nodes


BST
Checks:
	a) search
	b) insert
	c) delete
	d) isBst
Inorder gives sorted array
	a) 2 values swapped
	b) triplet with a value present
	c) range sum BST

sorted array to bst
no of unique bst from an array of 1...n

Graphs:
Representation
	a) Map
	b) Matrix
	c) Node with children

Traversal:
	a) DFS
	b) BFS
	c) LOT

Properties
	a) undirected cyclic?
	b) directed cyclic?
	c) strongly connected
	d) bipartite

Distance/ computation
	a) Prims
	b) Kruskal
	c) Djikstra's
	d) Floyd Warshall
	e) Bellman ford
	
Algorithms
	a) Flood fill
	b) min cash flow

DAG
	1) Topological sort
		a) alien dictionary
		b) course schedule I
		c) course schedule II


N-ary tree
	1) LCA
	2)  

Matrix: 
The questions can be solved by graph algos/ dp
	a) Rotten oranges
	b) no of islands
	c) longest increasing path when you can move only right and down
	d) longest increasing path when you cam move in all directions
	e) min cost path, you can travel down,right,lower diagonal
	f) max cost path, you can travel down,right,lower diagonal
	g) min steps to reach the end
	f) Unique paths
	g) Unique paths with obstacle


DP: 
RECURSIVE SOLUTION TO A DP PROBLEM IS LIKE SOLVING A N-ARY TREE
Characteristics of dp problem:
1) Overlapping subproblems
2) Optimal substructure property
Solve all dp problems via memoization
Approach of writing a base condition: there could be many base conditions 
Reverse conditons are difficult and error prone, write the condition while calling the recursive function
https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns
Patterns of DP questions:
1) Minimum/maximum path to reach a target
2) Distinct ways
3) Merging ways
4) DP on strings
5) Decision making(knapsack)/state machine
	a) Best time to buy and sell stock I
	b) Best time to buy and sell stocl II
	c) Best time to but and sell stock III
	d) Best time to buy and sell stock IV
	e) Best time to buy and sell stock with cooldown

	a) Maximum subarray

DP templates:
1) LIS variants
2) Partition subset
3) Partition into k equal subsets
4) LCS variants
5) Palindrome 
6) Coin change
7) MCM
8) Matrix/2D array
9) Hash+DP
10) State machine
11) DFS + DP
12) Minimax DP





Notes:
If the questions are on a circle then taking it as an array and doing d[-1] gives the first element so the harmony is maintained
eg: If there are numbers present in circle and you cant take adjacents
DP:
There are problems that require all subsets evaluation use LIS technique in that
If you want to traverse the whole array and modify some element but didnt want to include the modifying elements then travel from backwards
Like in the partition equal subset sum dp problem changes are getting made but it is not required to consider them so we traverse from backwards
IF it is a subset problem try to sort and then solve
PALINDROME:
2) Longest palindromic substring
3) Longest palindrmoic subsequence
1) no of palindromic substrings in a string

There are questions that requires to check all substring, eg: partition a string such that all substrings are palindrome and require min cut
if it is subset: LIS
if it is substring: Diagonal dp

for 3d matrix d[k][i][j] think if this as a 2d matrix of (i,j) then expanded in 3d by k 



BIts:
https://leetcode.com/discuss/general-discussion/1049269/Understanding-how-numbers-are-stored-in-the-computer-using-only-0-and-1.
https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate
http://graphics.stanford.edu/~seander/bithacks.html



Arrays:
1) All subarrays: O(n+2)
2) All subsets: bitmask(2^n)
3) Prefix sum
4) Maximum difference between 2 elements such that the larger element appears after the smaller number: O(n)


