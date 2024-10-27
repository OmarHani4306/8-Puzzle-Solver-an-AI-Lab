import time
from get_children import get_children
from extract_path import extract_path

def dls(state, limit):
    goal_state = 12345678  # Goal configuration

    if state == goal_state:
        return [], 0, 0, 0, 0.0  # Return immediately if already solved

    start = time.time()

    # Stack stores paths, each with [state, direction, cost]
    stack = [[[state, "", 0]]]  
    visited = set()  # Track visited states to avoid cycles

    while stack:  # While there are states to explore
        current_path = stack.pop()  # Pop the most recent path (LIFO)
        current_state = current_path[-1][0]
        current_cost = current_path[-1][2]  # Track current cost

        visited.add(current_state)  # Mark the current state as visited

        # Skip paths that exceed the depth limit
        if current_cost + 1 > limit:
                continue  
        
        # Generate all valid children (next moves)
        children_direction = get_children(current_state)

        for child, direction in children_direction:

            if child == goal_state:  # If goal state is found
                end = time.time()
                running_time = end - start

                path = extract_path(current_path + [[child, direction, current_cost + 1]])
                nodes_expanded = len(visited)

                return path, current_cost + 1, nodes_expanded, current_cost + 1, running_time


            # Add the new path to the stack with incremented cost
            new_path = current_path + [[child, direction, current_cost + 1]]
            stack.append(new_path)  # Push to the stack for LIFO behavior

    # If no solution is found within the limit
    return None
