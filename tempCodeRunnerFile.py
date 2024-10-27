import tracemalloc

# Start tracking memory allocations
tracemalloc.start()

# Code to measure memory usage
my_list = [1, 2, 3, 4, 5]

# Get current and peak memory usage
current, peak = tracemalloc.get_traced_memory()

print(f"Current memory usage: {current / 1024:.2f} KB")
print(f"Peak memory usage: {peak / 1024:.2f} KB")

# Stop tracking memory
tracemalloc.stop()