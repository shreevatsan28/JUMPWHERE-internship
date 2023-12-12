def convert_to_positive_coordinates(coordinates):
    if not coordinates:
        return []

    
    min_x = min(coord[0] for coord in coordinates)
    min_y = min(coord[1] for coord in coordinates)

    
    new_coordinates = [(coord[0] - min_x, coord[1] - min_y) for coord in coordinates]

    return new_coordinates

input_coordinates = [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
output_coordinates = convert_to_positive_coordinates(input_coordinates)
print(output_coordinates)
