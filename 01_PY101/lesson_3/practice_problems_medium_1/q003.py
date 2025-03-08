def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element) # adds new_element to the end of the list, mutates buffer
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element] # merges the list with the new list [new_element], doesn't mutate buffer and creates a new list instead
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer