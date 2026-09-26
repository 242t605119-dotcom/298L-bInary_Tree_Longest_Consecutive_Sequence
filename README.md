# LeetCode 298 - Binary Tree Longest Consecutive Sequence

## Problem Statement

Given the root of a binary tree, return the length of the longest consecutive sequence path.

A consecutive sequence means each child node has a value exactly one greater than its parent.

## Example

### Input

```text
root = [1,null,3,2,4,null,null,null,5]
```

### Output

```text
3
```

### Explanation

The longest consecutive path is:

```text
3 → 4 → 5
```

So the answer is `3`.

## Approach

Use Depth First Search (DFS).

For every node:

* Check whether its value is one greater than its parent.
* If yes, increase the current length.
* Otherwise, start a new sequence.
* Check both left and right subtrees and keep the maximum length.

## Algorithm

1. Start DFS from the root.
2. Compare each node with its parent.
3. Increase the length if the values are consecutive.
4. Otherwise, reset the length to `1`.
5. Continue for both subtrees.
6. Return the maximum length found.

## Time Complexity

**O(n)**

## Space Complexity

**O(h)**

where `h` is the height of the tree.

## Author

T. Nandhini
