import time, heapq, math
from get_children import get_children

def compute_heuristic(current_state_int, goal_positions, heuristic_type='manhattan'):
    total_distance = 0
    current_state_str = str(current_state_int).zfill(9)

    for i in range(9):  
        current_index = int(current_state_str[i])  
        current_pos = goal_positions[current_index]  
        goal_pos = goal_positions[i]  
        if heuristic_type == 'manhattan':
            total_distance += abs(current_pos[0] - goal_pos[0]) + abs(current_pos[1] - goal_pos[1])
        elif heuristic_type == 'euclidean':
            total_distance += math.sqrt((current_pos[0] - goal_pos[0])**2 + (current_pos[1] - goal_pos[1])**2)
    return total_distance

def A(state, mode='manhattan'):
    goal_state = 12345678
    if state == goal_state:
        return [], 0, 0, 0, 0.0

    goal_positions = {
        0: (0, 0), 1: (0, 1), 2: (0, 2),
        3: (1, 0), 4: (1, 1), 5: (1, 2),
        6: (2, 0), 7: (2, 1), 8: (2, 2),
    }

    frontier = []
    visited = {}
    max_depth = 0
    no_of_expanded_nodes = 0
    start_time = time.time()

    initial_heuristic = compute_heuristic(state, goal_positions, mode)
    heapq.heappush(frontier, (initial_heuristic, 0, state, []))  # path as a list

    while frontier:
        cost, depth, current_state, path = heapq.heappop(frontier)

        if current_state in visited and visited[current_state] <= depth:
            continue

        visited[current_state] = depth
        max_depth = max(depth, max_depth)
        no_of_expanded_nodes += 1

        if current_state == goal_state:
            end_time = time.time()
            return path, depth, no_of_expanded_nodes, max_depth, end_time - start_time

        children_direction = get_children(current_state)
        for child, direction in children_direction:
            if child in visited and visited[child] <= depth + 1:
                continue

            h = compute_heuristic(child, goal_positions, mode)
            new_path = path + [direction]
            heapq.heappush(frontier, (depth + 1 + h, depth + 1, child, new_path))

    return [], 0, 0, 0, 0.0

def main():
    test_cases = [
        (806547231, 31),
        (641302758, 14),
        (158327064, 12),
        (328451670, 12),
        (35428617, 10),  # Removed the leading zero for Python integer format
        (725310648, 15)
    ]

    for initial_state, expected_moves in test_cases:
        path, cost, no_of_expanded_nodes, max_depth, elapsed_time = A(initial_state)
        
        print(f"Initial state: {initial_state}")
        print(f"Expected moves: {expected_moves}")
        print(f"Path to solution: {path}")
        print(f"Cost of path (number of moves): {cost}")
        print(f"Number of expanded nodes: {no_of_expanded_nodes}")
        print(f"Maximum search depth reached: {max_depth}")
        print(f"Running time (seconds): {elapsed_time:.4f}")
        print(f"Result matches expected: {cost == expected_moves}")
        print("-" * 40)

if __name__ == "__main__":
    main()
