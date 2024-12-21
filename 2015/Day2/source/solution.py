

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



def intake_presents(file):
    """Opens a file then makes each line a string in list."""
    input_file = open(f"{file}")
    list_of_presents = input_file.readlines()
    return list_of_presents

def convert_present_string_to_ints(string):
    pass