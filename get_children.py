def get_children(state):
    state = str(state).zfill(9)  
    zero_index = state.index("0") 
    children = []

    if zero_index not in {2, 5, 8}:  
        new_state = state[:zero_index] + state[zero_index + 1] + state[zero_index] + state[zero_index + 2:]
        children.append((int(new_state), "right"))

    if zero_index not in {6, 7, 8}: 
        new_state = state[:zero_index] + state[zero_index + 3] + state[zero_index + 1:zero_index + 3] + state[zero_index] + state[zero_index + 4:]
        children.append((int(new_state), "down"))

    if zero_index not in {0, 3, 6}:  
        new_state = state[:zero_index - 1] + state[zero_index] + state[zero_index - 1] + state[zero_index + 1:]
        children.append((int(new_state), "left"))

    if zero_index not in {0, 1, 2}:  
        new_state = state[:zero_index - 3] + state[zero_index] + state[zero_index - 2:zero_index] + state[zero_index - 3] + state[zero_index + 1:]
        children.append((int(new_state), 'up'))

    return children
    
