import tkinter as tk
import time
from bfs import bfs
from dfs import dfs
from ids import ids
from A import A
from check_game import check_game

def display_message(message, error=False):
    message_label.config(text=message, fg="red" if error else "green")

def update_puzzle_display(puzzle_state):
    for i in range(3):
        for j in range(3):
            tile_value = puzzle_state[i * 3 + j]
            tile_labels[i][j].config(
                text=tile_value if tile_value != '0' else "", 
                bg="white" if tile_value != '0' else "skyblue"
            )

def animate_solution(path, puzzle, algorithm_name):
    puzzle_list = [list(puzzle[i:i + 3]) for i in range(0, 9, 3)]
    display_message("")
    display_final_results([], 0, 0, 0, 0.0, algorithm_name)
    if not path:
        display_message("No moves needed. The puzzle is already in the solved state.")
        update_puzzle_display(puzzle)
        return
    for move in path:
        zero_index = puzzle.index('0')
        zero_row, zero_col = divmod(zero_index, 3)
        if move == "up" and zero_row > 0:
            puzzle_list[zero_row][zero_col], puzzle_list[zero_row - 1][zero_col] = puzzle_list[zero_row - 1][zero_col], puzzle_list[zero_row][zero_col]
        elif move == "down" and zero_row < 2:
            puzzle_list[zero_row][zero_col], puzzle_list[zero_row + 1][zero_col] = puzzle_list[zero_row + 1][zero_col], puzzle_list[zero_row][zero_col]
        elif move == "left" and zero_col > 0:
            puzzle_list[zero_row][zero_col], puzzle_list[zero_row][zero_col - 1] = puzzle_list[zero_row][zero_col - 1], puzzle_list[zero_row][zero_col]
        elif move == "right" and zero_col < 2:
            puzzle_list[zero_row][zero_col], puzzle_list[zero_row][zero_col + 1] = puzzle_list[zero_row][zero_col + 1], puzzle_list[zero_row][zero_col]
        puzzle = ''.join(sum(puzzle_list, []))
        update_puzzle_display(puzzle)
        root.update()
        time.sleep(1)

def run_algorithm(algorithm):
    puzzle_input = ''
    for row in entry_widgets:
        for entry in row:
            value = entry.get()
            if value not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
                display_message("Please enter valid numbers (0-8) in all tiles.", error=True)
                return
            puzzle_input += value
    puzzle = int(puzzle_input)
    if not check_game(puzzle):
        display_final_results([], 0, 0, 0, 0.0)
        display_message("The puzzle is not solvable.", error=True)
        return
    try:
        if algorithm == "DFS":
            path, cost_of_path, nodes_expanded, search_depth, running_time = dfs(puzzle)
        elif algorithm == "BFS":
            path, cost_of_path, nodes_expanded, search_depth, running_time = bfs(puzzle)
        elif algorithm == "IDS":
            path, cost_of_path, nodes_expanded, search_depth, running_time = ids(puzzle)
        elif algorithm == "A* Manhattan":
            path, cost_of_path, nodes_expanded, search_depth, running_time = A(puzzle, "manhattan")
        elif algorithm == "A* Euclidean":
            path, cost_of_path, nodes_expanded, search_depth, running_time = A(puzzle, "euclidean")
        else:
            display_message("Unknown algorithm selected.", error=True)
            return

        if algorithm not in ["DFS", "IDS"]:
            animate_solution(path, puzzle_input, algorithm)  
        else:
            final_state = puzzle_input
            for move in path:
                zero_index = final_state.index('0')
                zero_row, zero_col = divmod(zero_index, 3)
                final_state_list = [list(final_state[i:i + 3]) for i in range(0, 9, 3)]
                if move == "up" and zero_row > 0:
                    final_state_list[zero_row][zero_col], final_state_list[zero_row - 1][zero_col] = final_state_list[zero_row - 1][zero_col], final_state_list[zero_row][zero_col]
                elif move == "down" and zero_row < 2:
                    final_state_list[zero_row][zero_col], final_state_list[zero_row + 1][zero_col] = final_state_list[zero_row + 1][zero_col], final_state_list[zero_row][zero_col]
                elif move == "left" and zero_col > 0:
                    final_state_list[zero_row][zero_col], final_state_list[zero_row][zero_col - 1] = final_state_list[zero_row][zero_col - 1], final_state_list[zero_row][zero_col]
                elif move == "right" and zero_col < 2:
                    final_state_list[zero_row][zero_col], final_state_list[zero_row][zero_col + 1] = final_state_list[zero_row][zero_col + 1], final_state_list[zero_row][zero_col]
                final_state = ''.join(sum(final_state_list, []))
            update_puzzle_display(final_state)

        display_final_results(path, search_depth, cost_of_path, nodes_expanded, running_time, algorithm)
    except Exception as e:
        display_message(f"Error: {str(e)}", error=True)


def display_final_results(path, search_depth, cost_of_path, nodes_expanded, running_time, algorithm_name):
    results_text = f"""
    Algorithm: {algorithm_name}
    Path : {', '.join(path)}
    Cost of Path : {cost_of_path}
    Search depth : {search_depth}
    Number of Nodes Expanded: {nodes_expanded}
    Running Time : {running_time:.9f} seconds
    """
    results_label.config(text=results_text)

root = tk.Tk()
root.title("8-Puzzle Solver Game")

puzzle_display = tk.Frame(root)
puzzle_display.pack(pady=20)

tile_labels = [[tk.Label(puzzle_display, width=4, height=2, font=("Comic Sans MS", 30), relief="solid", bg="white")
                for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        tile_labels[i][j].grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

entry_widgets = []
for i in range(3):
    row_entries = []
    for j in range(3):
        entry = tk.Entry(input_frame, width=4, font=("Comic Sans MS", 24), justify='center', relief="solid")
        entry.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
        row_entries.append(entry)
    entry_widgets.append(row_entries)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

algorithm_buttons = [("DFS", "DFS"), ("BFS", "BFS"), ("IDS", "IDS"), 
                     ("A* (Manhattan)", "A* Manhattan"), ("A* (Euclidean)", "A* Euclidean")]    

for index, (text, algorithm) in enumerate(algorithm_buttons):
    button = tk.Button(button_frame, text=text, command=lambda alg=algorithm: run_algorithm(alg), width=15, height=1, font=("Comic Sans MS", 12, "bold"))
    button.grid(row=0, column=index, padx=5)

message_label = tk.Label(root, text="", font=("Comic Sans MS", 12), padx=10, pady=10)
message_label.pack(pady=10)

results_label = tk.Label(root, text="", font=("Comic Sans MS", 12), justify="left", padx=10, pady=10)
results_label.pack(pady=5)

root.mainloop()