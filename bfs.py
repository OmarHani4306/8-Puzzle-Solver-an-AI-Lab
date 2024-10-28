import time

from get_children import get_children
from extract_path import extract_path

def bfs(state):
    goal_state = 12345678  

    if state == goal_state:
        return [], 0, 0, 0, 0.0 
    
    start = time.time()

    queue     = [[[state, "", 0]]]  
    visited   = set()  
    forienter = set()  

    while queue:  
        current_path  = queue.pop(0)
        current_state = current_path[-1][0]
        current_cost  = current_path[-1][-1]

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
            queue.append(new_path)
    
    return None

def main():
    test_cases = [
        # (806547231, 31),
        (123405678, 40188),
        # (641302758, 14),
        # (158327064, 12),
        # (328451670, 12),
        # (35428617, 10),  # Removed the leading zero for Python integer format
        # (725310648, 15)
    ]

    for initial_state, expected_moves in test_cases:
        path, cost, no_of_expanded_nodes, max_depth, elapsed_time = bfs(initial_state)
        
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
