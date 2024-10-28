import time, heapq, math

from get_children import get_children

# Note: get_children returns all available states that can be reached by moving the zero tile, along with the direction of the move required to reach each state.
# The state is an integer representing the puzzle, for example, 123456780 or 170245683.

def compute_heuristic(current_state_int, goal_positions, heuristic_type='manhattan'):
    total_distance = 0
    
    current_state_str = str(current_state_int).zfill(9)  
    
    for i in range(0, 9):  
        current_index = int(current_state_str[i])  
        current_pos = goal_positions[current_index]  
        goal_pos = goal_positions[i]  
        if heuristic_type == 'manhattan':
            total_distance += abs(current_pos[0] - goal_pos[0]) + abs(current_pos[1] - goal_pos[1])
        elif heuristic_type == 'euclidean':
            total_distance += math.sqrt((current_pos[0] - goal_pos[0])**2 + (current_pos[1] - goal_pos[1])**2)

    return total_distance

def decrease_key(heap, old_value, new_value):
    index = heap.index(old_value)

    heap[index] = new_value

    if new_value < old_value:
        heapq._siftup(heap, index)
    else:
        heapq._siftdown(heap, 0, index)

def A(state, mode='manhattan'):

    goal_state = 12345678

    if state == goal_state:
        return [], 0, 0, 0, 0.0
    
    goal_positions = {
        0: (0, 0),
        1: (0, 1),
        2: (0, 2),
        3: (1, 0),
        4: (1, 1),
        5: (1, 2),
        6: (2, 0),
        7: (2, 1),
        8: (2, 2),
    }

    ########################################################
    # Implement the A* algorithm logic starting from below #
    ########################################################


    # outputs to return once implemented:
    # 1. Return the list of directions, e.g., ["up", "left", "down"]
    # 2. Return the cost of the path (integer representing depth to reach the goal)
    # 3. Return the number of expanded nodes
    # 4. Return the maximum search depth reached
    # 5. Return the running time in seconds

    frointer = []

    visited = set()

    max_depth = 0

    no_of_expanded_nodes = 0


    start_time = time.time()

    heapq.heappush(frointer, (0, 0, state, []))

    while frointer:

        cost, depth, current_state, path = heapq.heappop(frointer)
        visited.add(current_state)

        max_depth = max(depth, max_depth)
        no_of_expanded_nodes += 1

        if current_state == goal_state: 
            end_time = time.time()
            return path, depth, no_of_expanded_nodes, max_depth, end_time - start_time

        children_direction = get_children(current_state)

        for child, direction in children_direction:

            if child in visited:
                continue   
            
            # adding deacrese ket to optimize

            # if child in frointer:
                # decrease_key(chi)
            h = compute_heuristic(child, goal_positions, mode)
            new_path = path[:]
            new_path.append(direction)

            heapq.heappush(frointer, (depth+1+h, depth+1, child, new_path))

    return [], 0, 0, 0, 0.0


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
        path, cost, no_of_expanded_nodes, max_depth, elapsed_time = A(initial_state)
        
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
