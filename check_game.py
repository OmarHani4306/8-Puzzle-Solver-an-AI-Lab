def check_game(state):
    state = str(state).zfill(9)  
    zero_index = state.index("0") 
    state = state[:zero_index] + state[zero_index + 1:] 

    count_inversion = sum(1 for i in range(len(state)) for j in range(i + 1, len(state)) if state[i] > state[j])

    return count_inversion % 2 == 0
        