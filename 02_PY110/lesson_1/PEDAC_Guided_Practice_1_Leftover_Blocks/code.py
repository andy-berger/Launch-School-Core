def calculate_leftover_blocks(available_blocks):
    blocks_remaining = available_blocks
    current_layer = 0

    required_blocks = (current_layer + 1) ** 2

    while blocks_remaining >= required_blocks:
        blocks_remaining -= required_blocks
        current_layer += 1
        required_blocks = (current_layer + 1) ** 2

    return blocks_remaining

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True