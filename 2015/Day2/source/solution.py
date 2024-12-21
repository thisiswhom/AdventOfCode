

class Rectangular_Prism_Present():
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.lxw = length * width
        self.lxh = length * height
        self.hxw = height * width

    def surface_area(self):
        total_area = (2 * self.lxw) + (2 * self.lxh) + (2 * self.hxw)
        return total_area
