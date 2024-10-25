import json
import time
from A import A

def run_tests(test_cases, output_file):
    results = []

    for initial_state in test_cases:
        # Run the A* algorithm
        path, cost, no_of_expanded_nodes, max_depth, elapsed_time = A(initial_state)

        # Prepare the result for this test case
        result = {
            "initial_state": initial_state,
            "path_to_solution": path,
            "cost_of_path": cost,
            "number_of_expanded_nodes": no_of_expanded_nodes,
            "maximum_search_depth_reached": max_depth,
            "running_time_seconds": elapsed_time
        }

        # Add the result to the list
        results.append(result)

    # Write the results to the output JSON file
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

    print(f"Results saved to {output_file}")

def main():
    # Define the test cases
    test_cases = [
        120345678,  # Example test case 1
        806547231,  # Example test case 2
        123804765,  # Example test case 3
        # Add more test cases as needed
    ]

    # Define the output file
    output_file = "results.json"

    # Run the tests and output the results to the JSON file
    run_tests(test_cases, output_file)

if __name__ == "__main__":
    main()
