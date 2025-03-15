# 🧩 8-Puzzle Solver Using Informed & Uninformed Search  

## 📌 Overview  
This project implements an **AI agent** to solve the **8-puzzle** using **uninformed and informed search algorithms**. The goal is to find the optimal sequence of moves to transition an initial board state to the **goal state (0,1,2,3,4,5,6,7,8)**.  

## 🎯 Algorithms Implemented  
✅ **Uninformed Search:**  
- **Breadth-First Search (BFS)**  
- **Depth-First Search (DFS)**  
- **Iterative Deepening Depth-First Search (IDDFS)**  

✅ **Informed Search (A\*) with Heuristics:**  
- **Manhattan Distance**  
- **Euclidean Distance**  

## ⚙️ Implementation Details  
- **State Representation:** The puzzle board is stored as a 2D array. The blank tile is represented by **0**.  
- **Valid Moves:** The blank tile can move **Up, Down, Left, Right**.  
- **Cost Calculation:** Each move has a uniform cost of **1**.  
- **Performance Comparison:**  
  - **Nodes Expanded**  
  - **Search Depth**  
  - **Path Cost**  
  - **Execution Time**  
  - **Heuristic Effectiveness (for A\*)**  

## 📄 Output & Visualization  
- **Step-by-step trace of moves** leading to the goal state.  
- **Comparison of algorithms based on performance metrics**.  
- **Bonus:** Best visualization receives extra credit.  
