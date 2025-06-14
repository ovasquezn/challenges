def hex_string_to_RGB(hex_string): 
    r = int(hex_string[1:3], 16)
    g = int(hex_string[3:5], 16)
    b = int(hex_string[5:7], 16)
    
    return {'r': r, 'g': g, 'b': b}

# Example usage
print(hex_string_to_RGB("#FF9933"))  # {'r': 255, 'g': 87, 'b': 51}