import time, heapq, math

from get_children import get_children

# Note: get_children returns all available states that can be reached by moving the zero tile, along with the direction of the move required to reach each state.
# The state is an integer representing the puzzle, for example, 123456780 or 170245683.

def compute_heuristic(current_state_int, goal_positions, heuristic_type='manhattan'):
    total_distance = 0
    
    # Convert the current state to a string and pad with zeros
    current_state_str = str(current_state_int).zfill(9)  # Ensure it has 9 digits
    
    for i in range(0, 9):  # Exclude the empty tile (0)
        current_index = int(current_state_str[i])  # Find the index of the tile
        current_pos = goal_positions[current_index]  # Calculate its position
        goal_pos = goal_positions[i]  # Get the goal position from pre-computed dict
        
        if heuristic_type == 'manhattan':
            # Manhattan distance: sum of absolute differences
            total_distance += abs(current_pos[0] - goal_pos[0]) + abs(current_pos[1] - goal_pos[1])
        elif heuristic_type == 'euclidean':
            # Euclidean distance: sqrt of sum of squared differences
            total_distance += math.sqrt((current_pos[0] - goal_pos[0])**2 + (current_pos[1] - goal_pos[1])**2)

    return total_distance

def A(state):

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

    # cost, depth, current_state, path, h = 0, 0, state, [], 0

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
            h = compute_heuristic(child, goal_positions, 'manhattan')
            new_path = path[:]
            new_path.append(direction)

            heapq.heappush(frointer, (1+h, depth+1, child, new_path))

    return [], 0, 0, 0, 0.0

def main():
    # Example initial state of the puzzle (as an integer)
    initial_state = 120345678  # Change this to test different scenarios
    
    # Run the A* algorithm
    path, cost, no_of_expanded_nodes, max_depth, elapsed_time = A(initial_state)

    # Output the results
    print("Path to solution:", path)
    print("Cost of path (number of moves):", cost)
    print("Number of expanded nodes:", no_of_expanded_nodes)
    print("Maximum search depth reached:", max_depth)
    print("Running time (seconds):", elapsed_time)

if __name__ == "__main__":
    main()