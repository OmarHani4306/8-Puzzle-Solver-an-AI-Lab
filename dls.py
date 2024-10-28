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
    stack = [state]  # Stack now only contains the state
    parent_map = {state: (None, None)}  # Map to store parent states and directions
    cost_map = {state: 0}  # Cost map to track the cost of reaching each state
    max_depth_reached = 0
    nodes_expanded = 0

    while stack:
        current_state = stack.pop()
        current_cost = cost_map[current_state]  # Get cost from the cost_map
        
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

                # Check if the child is unvisited or if the previous cost is greater than the current cost
                if child not in cost_map or cost_map[child] > current_cost + 1:
                    parent_map[child] = (current_state, direction)
                    cost_map[child] = current_cost + 1
                    stack.append(child)
        
    return None
