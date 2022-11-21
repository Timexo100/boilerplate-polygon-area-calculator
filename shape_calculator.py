class Rectangle:
    def __init__(self, width, height):
        self.set_height(height)
        self.set_width(width)

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return (self.width * self.height)
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self): 
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        line = ""
        ch = '*'
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(self.height):
            line += "{}\n".format(self.width*ch)
        return line

    def get_amount_inside(self, shape):
        return self.get_area()//shape.get_area()

    def __str__(self):
        s = str(type(self)).split('.')[1].split('\'')[0]
        if s == "Rectangle":
            return "{}(width={}, height={})".format(s, self.width, self.height)
        return "{}(side={})".format(s, self.width)


class Square(Rectangle):
    def __init__(self, width):
        self.set_side(width)
    
    def set_side(self, side):
        self.width = side
        self.height = side