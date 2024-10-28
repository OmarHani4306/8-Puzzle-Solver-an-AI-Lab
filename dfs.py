import time
from get_children import get_children
from extract_path import extract_path

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


def dfs(state):
    goal_state = 12345678  # Goal configuration
    if state == goal_state:
        return [], 0, 0, 0, 0.0  # Return immediately if already solved

    start = time.time()
    stack = [[state, 0]]  # Stack only holds the state and depth
    visited = set()  # Track visited states to avoid cycles
    parent_map = {state: (None, None)}  # Track parent and direction for path reconstruction
    max_depth_reached = 0
    nodes_expanded = 0
    forienter = set()  

    while stack:
        current_state, current_cost = stack.pop()

        # Update the maximum depth reached
        max_depth_reached = max(max_depth_reached, current_cost)
        nodes_expanded += 1

        # Mark the current state as visited
        visited.add(current_state)

        # Generate possible moves (children)
        children_direction = get_children(current_state)

        for child, direction in children_direction:
            if child in visited or child in forienter:
                continue

            # Record the parent and direction for reconstructing the path later
            parent_map[child] = (current_state, direction)

            if child == goal_state:  # Check if the goal state is found
                end = time.time()
                running_time = end - start

                # Reconstruct the path from the goal to the start using parent_map
                path = extract_path(child, parent_map)
                return path, current_cost + 1, nodes_expanded, max(max_depth_reached, current_cost + 1), running_time

            # Add child to stack for further exploration, only state and cost
            forienter.add(child)
            stack.append([child, current_cost + 1])

    return None

    while stack:  
        current_path  = stack.pop()
        current_state = current_path[-1][0]
        current_cost  = current_path[-1][-1]

<<<<<<< HEAD
def main():
    test_cases = [
        # (806547231, 31),
        (123405678, 40188),
        # (120345678, 2),
        # (641302758, 14),
        # (158327064, 12),
        # (328451670, 12),
        # (35428617, 10),  # Removed the leading zero for Python integer format
        # (725310648, 15)
    ]

    for initial_state, expected_moves in test_cases:
        path, cost, no_of_expanded_nodes, max_depth, elapsed_time = dfs(initial_state)
        
        print(f"Initial state: {initial_state}")
        print(f"Expected moves: {expected_moves}")
        print(f"Path to solution: {path}")
        print(f"Cost of path (number of moves): {cost}")
        print(f"Number of expanded nodes: {no_of_expanded_nodes}")
        print(f"Maximum search depth reached: {max_depth}")
        print(f"Running time (seconds): {elapsed_time:.10f}")
        print(f"Result matches expected: {cost == expected_moves}")
        print("-" * 40)

if __name__ == "__main__":
    main()
=======
        visited.add(current_state)

        children_direction = get_children(current_state)

        for child, direction in children_direction:
            if child == goal_state:
                end = time.time()
                
                running_time = end - start

                path = extract_path(current_path + [[child, direction, current_cost + 1]])
                nodes_expanded = len(visited)
                
                return path, current_cost + 1, nodes_expanded, current_cost + 1, running_time        

            if child in visited or child in forienter:
                continue
            
            new_path = current_path + [[child, direction, current_cost + 1]] 
            
            forienter.add(child)
            stack.append(new_path)
    
    return None
>>>>>>> GUI-Modification
