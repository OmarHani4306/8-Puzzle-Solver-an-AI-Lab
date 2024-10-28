import time
from get_children import get_children
from extract_path import extract_path

def dls(state, limit):
    goal_state=12345678
    if state == goal_state:
        return [], 0, 0, 0, 0.0  # Return immediately if already solved

    
    start = time.time()
    stack = [[[state, "", 0]]]  # Initialize stack for LIFO behavior
    max_depth_reached = 0
    nodes_expanded = 0

    while stack:
        current_path = stack.pop()
        current_state = current_path[-1][0]
        current_cost = current_path[-1][-1]

        # Update the maximum depth reached
        max_depth_reached = max(max_depth_reached, current_cost)
        nodes_expanded += 1

        if current_cost < limit:  # Explore nodes up to the limit
            children_direction = get_children(current_state)

            for child, direction in children_direction:
                if child == goal_state:  # Check if the goal state is found
                    end = time.time()
                    running_time = end - start

                    # Extract the path to the goal state
                    path = extract_path(current_path + [[child, direction, current_cost + 1]])
                    return path, current_cost + 1, nodes_expanded, max(max_depth_reached, current_cost + 1), running_time

                # Add the new child path to the stack for further exploration
                new_path = current_path + [[child, direction, current_cost + 1]]
                stack.append(new_path)  # Allow revisiting nodes at different depths

    return None