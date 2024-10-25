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
                
                return path, current_cost, nodes_expanded, current_cost, running_time     

            if child in visited or child in forienter:
                continue
            
            new_path = current_path + [[child, direction, current_cost + 1]] 
            
            forienter.add(child)
            queue.append(new_path)
    
    return None
