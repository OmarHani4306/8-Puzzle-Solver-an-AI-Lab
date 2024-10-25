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
            h = compute_heuristic(child, goal_positions, mode)
            new_path = path[:]
            new_path.append(direction)

            heapq.heappush(frointer, (1+h, depth+1, child, new_path))

    return [], 0, 0, 0, 0.0