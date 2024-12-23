import re


class Rectangular_Prism_Present():
    def __init__(self, length, width, height):
        """Takes the three different edges and calculates the three sets of rectangles

        Having it do calculations in the __init__ may break convention however it made the
        creation and use of the methods simpler"""
        self.length = length
        self.width = width
        self.height = height
        self.lxw = length * width
        self.lxh = length * height
        self.hxw = height * width

    def surface_area(self):
        """Uses the three equal and opposite faces and returns the surface area"""
        total_area = (2 * self.lxw) + (2 * self.lxh) + (2 * self.hxw)
        return total_area

    def smallest_side(self):
        """Uses the three equal and opposite faces and returns the smallest"""
        small_side = min(self.lxw, self.lxh, self.hxw)
        return small_side

    def wrapping_paper_needed(self):
        """Uses the previously calculated values to return the amount of wrapping paper needed"""
        return self.surface_area() + self.smallest_side()

    def ribbon_wrap(self):
        """finds the two smallest sides and returns the perimeter they would make"""
        sides_in_order = [self.length, self.width, self.height]
        sides_in_order.sort()
        smallest_perimeter = (sides_in_order[0] *2) + (sides_in_order[1] *2)
        return smallest_perimeter

    def ribbon_bow(self):
        return self.length * self.width * self.height

    def ribbon_needed(self):
        return self.ribbon_bow() + self.ribbon_wrap()



def intake_presents(file):
    """Opens a file then makes each line a string in list."""
    input_file = open(f"{file}")
    list_of_presents = input_file.readlines()
    return list_of_presents

def convert_present_string_to_ints(string):
    """takes in a string with numbers seperated with x's and returns the numbers"""
    dimensions = [int(number) for number in re.findall(r'\d+', string)]
    return dimensions

def create_file_path(file_name):
    """This function creates the absolute path of the values file.

    This is to enable me to not worry about pushing my username/file structure github
    Possible side benefit is others can run this on their system without worrying
    about differences in their enviroment and mine"""
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    total_paper_needed = 0
    file = os.path.join(current_dir, file_name)
    return file

def main():
    """Takes in the values file and prints out the number of feet of wrapping paper needed"""

    file = create_file_path("values")
    present_list = intake_presents(file)
    total_paper_needed = 0
    total_ribbon_needed = 0
    for line in present_list:
        verticies = convert_present_string_to_ints(line)
        current_present = Rectangular_Prism_Present(verticies[0], verticies[1], verticies[2])
        total_paper_needed += current_present.wrapping_paper_needed()
        total_ribbon_needed += current_present.ribbon_needed()
    print(f"""{total_paper_needed} feet of wrapping paper needed\n{total_ribbon_needed} feet of ribbon needed""")


if __name__ == "__main__":
    main()
