# Traverse A Tree

In the introduction, we have gone through the concept of a tree and a binary tree.

In this chapter, we will focus on the traversal methods used in a binary tree. Understanding these traversal methods will definitely help you have a better understanding of the tree structure and have a solid foundation for the further study.

The goal of this chapter is to:

    Understand the difference between different tree traversal methods;
    Be able to solve preorder, inorder and postorder traversal recursively;
    Be able to solve preorder, inorder and postorder traversal iteratively;
    Be able to do level traversal using BFS.

## Pre-order Traversal

Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree.

## In-order Traversal

In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.

Typically, for binary search tree, we can retrieve all the data in sorted order using in-order traversal.

## Post-order Traversal

Post-order traversal is to traverse the left subtree first. Then traverse the right subtree. Finally, visit the root.

It is worth noting that when you delete nodes in a tree, deletion process will be in post-order. That is to say, when you delete a node, you will delete its left child and its right child before you delete the node itself.

Also, post-order is widely used in mathematical expressions. It is easier to write a program to parse a post-order expression.

## Recursive or Iterative

Try to practice the three different traversal methods in our after-article exercise. You might want to implement the methods recursively or iteratively. Implement both recursion and iteration solutions and compare the differences between them.

## Problems 
1. 