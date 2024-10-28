import time
from get_children import get_children
from extract_path import extract_path

def dfs(state):
    goal_state = 12345678  # Goal configuration
    if state == goal_state:
        return [], 0, 0, 0, 0.0  # Return immediately if already solved

    start = time.time()
    stack = [[[state, "", 0]]]  # Initialize stack for LIFO behavior
    visited = set()  # Track visited states to avoid cycles
    max_depth_reached = 0
    nodes_expanded = 0

    while stack:
        current_path = stack.pop()
        current_state = current_path[-1][0]
        current_cost = current_path[-1][2]

        # Update the maximum depth reached
        max_depth_reached = max(max_depth_reached, current_cost)
        nodes_expanded += 1

        # Mark the current state as visited
        visited.add(current_state)

        # Generate possible moves (children)
        children_direction = get_children(current_state)

        for child, direction in children_direction:
            if child == goal_state:  # Check if the goal state is found
                end = time.time()
                running_time = end - start

                # Extract the path to the goal state
                path = extract_path(current_path + [[child, direction, current_cost + 1]])
                return path, current_cost + 1, nodes_expanded, max(max_depth_reached, current_cost + 1), running_time

            if child in visited:  # Skip if the child state has already been visited
                continue
            
            # Add the new path to the stack for further exploration
            new_path = current_path + [[child, direction, current_cost + 1]]
            stack.append(new_path)

    return None
