import time
from get_children import get_children
from extract_path import extract_path

def dfs(state):
    goal_state = 12345678  # Goal configuration

    if state == goal_state:
        return [], 0, 0, 0, 0.0  # Return immediately if already solved

    start = time.time()

    # Use a stack-like structure: LIFO behavior by popping from the end
    stack = [[[state, "", 0]]]  
    visited = set()  # Track visited states to avoid cycles
    max_depth = 0  # Initialize max depth

    while stack:  # While there are states to explore
        current_path = stack.pop()  # Pop from the end (LIFO)
        current_state = current_path[-1][0]
        current_cost = current_path[-1][-1]  # Current path cost represents depth

        # Update the max depth reached so far
        max_depth = max(max_depth, current_cost)

        visited.add(current_state)  # Mark as visited

        # Generate possible moves (children)
        children_direction = get_children(current_state)

        for child, direction in children_direction:
            if child == goal_state:  # Check if goal state is found
                end = time.time()
                running_time = end - start

                path = extract_path(current_path + [[child, direction, current_cost + 1]])
                nodes_expanded = len(visited)

                return path, current_cost + 1, nodes_expanded, max_depth + 1, running_time

            if child in visited:  # Skip if already visited
                continue

            # Add the new path to the stack
            new_path = current_path + [[child, direction, current_cost + 1]]
            stack.append(new_path)  # Push to the end for LIFO behavior

    # If no solution is found
    return [], 0, 0, max_depth, 0.0
