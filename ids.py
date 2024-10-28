from dls import dls
# Note: get_children returns all available states that can be reached by moving the zero tile, along with the direction of the move required to reach each state.
# The state is an integer representing the puzzle, for example, 123456780 or 170245683.

def ids(state):
    goal_state = 12345678

    if state == goal_state:
        return [], 0, 0, 0, 0.0

    #########################################################
    # Implement the ids algorithm logic starting from below #
    #########################################################
    limit = 0
    while True:
        result = dls(state, limit)
        if result is not None:  # If a solution is found
            return result
        limit += 1  

    # outputs to return once implemented:
    # 1. Return the list of directions, e.g., ["up", "left", "down"]
    # 2. Return the cost of the path (integer representing depth to reach the goal)
    # 3. Return the number of expanded nodes
    # 4. Return the maximum search depth reached
    # 5. Return the running time in seconds

