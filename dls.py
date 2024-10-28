import time
from get_children import get_children

def extract_path(goal_state, parent_map):
    path = []
    current_state = goal_state
    
    # Backtrack from goal to start using parent_map
    while parent_map[current_state][0] is not None:
        parent, direction = parent_map[current_state]
        path.append(direction)
        current_state = parent
    
    # Reverse path to get it from start to goal
    path.reverse()
    return path


def dls(state, limit):
    goal_state = 12345678
    if state == goal_state:
        return [], 0, 0, 0, 0.0  # Return immediately if already solved
    
    start = time.time()
    stack = [(state, 0)]  # Stack contains only the state and current depth
    parent_map = {state: (None, None)}  # Map to store parent states and directions
    max_depth_reached = 0
    nodes_expanded = 0

    while stack:
        current_state, current_cost = stack.pop()
        
        max_depth_reached = max(max_depth_reached, current_cost)
        nodes_expanded += 1

        if current_cost < limit:
            children_direction = get_children(current_state)

            for child, direction in children_direction:
                if child == goal_state:
                    end = time.time()
                    running_time = end - start

                    # Extract the path using the parent map
                    parent_map[child] = (current_state, direction)
                    path = extract_path(child, parent_map)
                    return path, current_cost + 1, nodes_expanded, max(max_depth_reached, current_cost + 1), running_time

                if child not in parent_map:  # Track unvisited states only
                    parent_map[child] = (current_state, direction)
                    stack.append((child, current_cost + 1))

    return None