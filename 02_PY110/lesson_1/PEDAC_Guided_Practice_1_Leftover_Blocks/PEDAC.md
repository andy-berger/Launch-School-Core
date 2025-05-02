# Problem
Build a structure using layers of cubes. The top layer is a single block. Upper layer blocks need support from four blocks in a lower layer. A lower layer block can support more than one block in an upper layer. Gaps between blocks are not allowed.
Calculate the number of blocks left over after building the tallest possible valid structure.

Input: Number of available blocks
Output: Number of blocks left over after building the talltest possible valid structure

Questions:
- Is there a limit on how many upper layers of blocks a lower layer block can support?
- Is there a general upper limit on the tallest possible structure?
- Is there a limit of how many cubes a layer can consist of?

# Examples (Test cases)
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

# Data structures
Perhaps nested lists where each sublist represents a layer?

# Algorithm
Layers from top to bottom:
1 -> needs 1 block
2 -> needs 2^2 = 4 blocks
3 -> needs 3^3 = 9 blocks
4 -> needs 4^4 = 16 blocks
etc.

# Code
See file code.py