import json
from A import A
import A_normal 
import a_star_opt

test_cases = [
    (806547231, 31),
    (641302758, 14),
    (158327064, 12),
    (328451670, 12),
    (35428617, 10),
    (725310648, 15)
]

def run_test(file, initial_state):
    if file == "A":
        return A(initial_state)
    elif file == "A_normal":
        return A_normal.A(initial_state)
    elif file == "A_fib_heap":
        return a_star_opt.A(initial_state)

results = []

for initial_state, expected_moves in test_cases:
    result = {
        "initial_state": initial_state,
        "expected_moves": expected_moves,
        "A": run_test("A", initial_state),
        "A_normal": run_test("A_normal", initial_state),
        "A_fib_heap": run_test("A_fib_heap", initial_state)
    }
    results.append(result)

# Save the results to a JSON file
with open("comparison_results.json", "w") as json_file:
    json.dump(results, json_file, indent=4)
