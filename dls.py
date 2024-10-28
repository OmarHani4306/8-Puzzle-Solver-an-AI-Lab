import time
from get_children import get_children
from extract_path import extract_path

def dls(state, limit):
    goal_state = 12345678  # Goal configuration

    if state == goal_state:
        return [], 0, 0, 0, 0.0  # Return immediately if already solved

    start = time.time()

    stack = [[[state, "", 0]]]  # LIFO stack
    visited = set()  # Track visited states
    max_depth = 0  # Initialize max depth

    while stack:
        current_path = stack.pop()
        current_state = current_path[-1][0]
        current_cost = current_path[-1][2]

        max_depth = max(max_depth, current_cost)  # Track max depth reached
        visited.add(current_state)

        if current_cost + 1 > limit:  # Depth limit check
            continue

        children_direction = get_children(current_state)

        for child, direction in children_direction:
            if child == goal_state:
                end = time.time()
                running_time = end - start

                path = extract_path(current_path + [[child, direction, current_cost + 1]])
                nodes_expanded = len(visited)

                return path, current_cost + 1, nodes_expanded,  max(max_depth, current_cost + 1), running_time

            # Add the child path to the stack for further exploration
            new_path = current_path + [[child, direction, current_cost + 1]]
            stack.append(new_path)

    # If no solution is found
    return None
