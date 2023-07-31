# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator

# For public execution and test
# https://replit.com/@ToniG4/boilerplate-polygon-area-calculator


class Rectangle :

    def __init__(self, width, height) :

        self._width = width
        self._height = height
    

    def __repr__(self) :

        class_name = type(self).__name__

        return f"{class_name}(width={self._width!r}, height={self._height!r})"
    

    def set_width(self, width) :

        self._width = width
    

    def set_height(self, height) :

        self._height = height
    

    def get_area(self) :

        return self._width * self._height
    

    def get_perimeter(self) :

        return 2 * self._width + 2 * self._height
    

    def get_diagonal(self) :

        return (self._width ** 2 + self._height ** 2) ** .5
    

    def get_picture(self) :

        if self._width > 50 or self._height > 50 : return "Too big for picture."

        picture = ""

        # Print 'height' lines of 'width' "*"
        h = 0
        while h < self._height :
            picture = picture + ( "*" * self._width ) + "\n"
            h += 1

        return picture
    

    def get_amount_inside(self, shape) :

        # Get the whole number the width and height of the shape is contained in the rectangle
        w = self._width // shape._width
        h = self._height // shape._height

        # Width and hight must be contained at least one time
        if w > 0 and h > 0 : return w * h
        else : return 0


class Square( Rectangle ) :

    def __init__(self, side) :

        super().__init__(side, side)


    def __repr__(self) :

        class_name = type(self).__name__

        return f"{class_name}(side={self._width})"
    

    def set_side(self, side) :

        self._width = side
        self._height = side
    

    def set_width(self, side) :

        self._width = side
        self._height = side
    

    def set_height(self, side) :

        self._width = side
        self._height = side


# Example execution and tests

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())


sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())


rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

sh = Rectangle(5, 3)
print(rect.get_amount_inside(sh))
