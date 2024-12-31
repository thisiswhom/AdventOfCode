def triangle_checker(side_a, side_b, side_c):
    """
    takes in three integers and confirms if they would make a triangle
    """
    if side_a + side_b > side_c and side_b + side_c > side_a and side_c + side_a > side_b:
        return True
    else:
        return False


def create_file_path(file_name):
    """
    This function creates the absolute path of the values file.

    This is to enable me to not worry about pushing my username/file structure gitHub
    Possible side benefit is others can run this on their system without worrying
    about differences in their environment and mine
    """
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(current_dir, file_name)
    return file


def intake_values(file):
    """Opens a file then makes each line a string in list."""
    input_file = open(f"{file}")
    list_of_values = [line.strip() for line in input_file.readlines()]
    return list_of_values

def extract_numbers(s):
    numbers = list(map(int, s.split()))
    return numbers

def reorder_triangle_list_vertically(data):
    """
    Reorders the input list of strings into vertical triangles.
    Each column becomes a group of triangles from consecutive rows.
    """
    parsed_data = [list(map(int, line.split())) for line in data]
    columns = list(zip(*parsed_data))
    triangles = []
    for col in columns:
        for i in range(0, len(col), 3):
            if i + 2 < len(col):
                triangles.append([col[i], col[i + 1], col[i + 2]])

    return triangles



def main():
    file = create_file_path("values")
    list_of_values = intake_values(file)
    number_of_real_triangles_part_1 = 0
    for index in list_of_values:
        numbers = extract_numbers(index)
        if triangle_checker(numbers[0], numbers[1], numbers[2]):
            number_of_real_triangles_part_1 += 1
    print(f'For part 1: The number of real triangles are {number_of_real_triangles_part_1}')
    number_of_real_triangles_part_2 = 0
    reordered_list = reorder_triangle_list_vertically(list_of_values)
    for triangle_set in reordered_list:
        if triangle_checker(triangle_set[0], triangle_set[1], triangle_set[2]):
            number_of_real_triangles_part_2 += 1
    print(f'For part 2: The number of real triangles are {number_of_real_triangles_part_2}')




if __name__ == "__main__":
    main()