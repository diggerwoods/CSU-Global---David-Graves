# First-Fit Memory Allocation Simulation
def first_fit(memory_blocks, processes):
    # Initialize allocation list with -1 (indicating no allocation)
    allocation = [-1] * len(processes)
# Iterate through each process
    for i in range(len(processes)):
        for j in range(len(memory_blocks)):
            # Check if the memory block can accommodate the process
            if memory_blocks[j] >= processes[i]:
                # Allocate the block to the process
                allocation[i] = j
                memory_blocks[j] -= processes[i]
                break  # Move to the next process after allocation
    return allocation
# Example usage
if __name__ == "__main__":
    # Memory blocks and their sizes
    memory_blocks = [100, 300, 250, 500, 400]
    # Processes and their memory requirements
    processes = [110, 250, 480, 75, 300]
print("Initial Memory Blocks:", memory_blocks)
print("Processes:", processes)
# Perform First-Fit allocation
allocation = first_fit(memory_blocks, processes)
# Display results
print("\nProcess Allocation Results:")
for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"Process {i + 1} (Size: {processes[i]}) -> Block {allocation[i] + 1}")
        else:
            print(f"Process {i + 1} (Size: {processes[i]}) -> Not Allocated")
print("\nRemaining Memory Blocks:", memory_blocks)
