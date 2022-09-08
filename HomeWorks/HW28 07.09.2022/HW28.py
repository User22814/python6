# Task 1
import math


class Circle:
    def __init__(self, radius: float):
        self.r = radius

    def __str__(self):
        return '{}'.format(self.r)

    def __eq__(self, other):
        return self.r == other.r

    def __gt__(self, other):
        return self.r > other.r

    def __ge__(self, other):
        return self.r >= other.r

    def __lt__(self, other):
        return self.r < other.r

    def __le__(self, other):
        return self.r <= other.r

    def __add__(self, other):
        return self.r + other.r

    def __sub__(self, other):
        return self.r - other.r

    def __iadd__(self, other):
        self.r += other.r
        return self

    def __isub__(self, other):
        self.r -= other.r
        return self


# a = Circle(5)
# b = Circle(3)
# a += b
# print(a)

# Task 2
class Complex:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return '{} + {}i'.format(self.x, self.y)

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.y * other.x + self.x * other.y)

    def __truediv__(self, other):
        left = (self.x * other.x + self.y * other.y) / (other.x ** 2 + other.y ** 2)
        right = (self.y * other.x - self.x * other.y) / (other.x ** 2 + other.y ** 2)
        return Complex(left, right)


# a1 = Complex(1, 2)
# a2 = Complex(3, 4)
# print(a1 / a2)

# Task 3
class Airplane:
    def __init__(self, type_plane: str, passengers_number: int):
        self.plane_type = type_plane
        self.passengers_number = passengers_number

    def __str__(self):
        return 'Type: {}, Passengers number: {}'.format(self.plane_type, self.passengers_number)

    def __eq__(self, other):
        return self.plane_type == other.plane_type

    def __add__(self, other):
        return self.passengers_number + other.passengers_number

    def __sub__(self, other):
        return self.passengers_number - other.passengers_number

    def __iadd__(self, other):
        self.passengers_number += other.passengers_number
        return self

    def __isub__(self, other):
        self.passengers_number -= other.passengers_number
        return self

    def __gt__(self, other):
        return self.passengers_number > other.passengers_number

    def __ge__(self, other):
        return self.passengers_number >= other.passengers_number

    def __lt__(self, other):
        return self.passengers_number < other.passengers_number

    def __le__(self, other):
        return self.passengers_number <= other.passengers_number


# plane1 = Airplane('Boeing 737', 85)
# plane2 = Airplane('Boeing 707', 75)
# print(plane1 == plane2)


# Task 4
class Flat:
    def __init__(self, square: float, price: float):
        self.square = square
        self.price = price

    def __str__(self):
        return 'Square: {}, Price: {}'.format(self.square, self.price)

    def __eq__(self, other):
        return self.square == other.square

    def __ne__(self, other):
        return self.square != other.square

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price


# a1 = Flat(66.9, 5500)
# a2 = Flat(73.5, 6800)
# print(a1 > a2)

# Task 5
class Figure:
    def __init__(self, figure_type: str):
        self.figure_type = figure_type

    def __str__(self):
        return 'Type: {}'.format(self.figure_type)


class Rectangle(Figure):
    def __init__(self, figure_type: str, side_length1: float, side_length2: float):
        super().__init__(figure_type)
        self.side1 = side_length1
        self.side2 = side_length2

    def get_square(self) -> int:
        return int(self.side1 * self.side2)

    def __int__(self):
        return self.get_square()


class CircleTask5(Figure):
    def __init__(self, figure_type: str, radius: float):
        super().__init__(figure_type)
        self.r = radius

    def get_square(self) -> int:
        return int(math.pi * self.r ** 2)

    def __int__(self):
        return self.get_square()


class Triangle(Figure):
    def __init__(self, figure_type: str, cathetus1: float, cathetus2: float):
        super().__init__(figure_type)
        self.cathetus1 = cathetus1
        self.cathetus2 = cathetus2

    def get_square(self) -> int:
        return int(0.5 * self.cathetus1 * self.cathetus2)

    def __int__(self):
        return self.get_square()


class Trapeze(Figure):
    def __init__(self, figure_type: str, side1: float, side2: float, height: float):
        super().__init__(figure_type)
        self.side1 = side1
        self.side2 = side2
        self.height = height

    def get_square(self) -> int:
        return int((self.side1 + self.side2) / 2 * self.height)

    def __int__(self):
        return self.get_square()


# a1 = Trapeze('trapeze', 5, 4, 2)
# a2 = CircleTask5('circle', 10)
# print(int(a1))


# Task 7
class Shape:
    def __init__(self, coordinate_x: float, coordinate_y: float):
        self.x = coordinate_x
        self.y = coordinate_y


class Square(Shape):
    def __init__(self, coordinate_x: float, coordinate_y: float, length_side: float):
        super().__init__(coordinate_x, coordinate_y)
        self.side = length_side

    def show(self):
        return f"INFO: X = {self.x}, Y = {self.y}, Length side = {self.side}"

    def save(self):
        file = open("square.txt", "w")
        file.write(f"INFO: Type: Square, X = {self.x}, Y = {self.y}, Length side = {self.side}")
        file.close()

    def load(self, filename: str):
        file = open(filename, "r")
        figure_info = file.read()
        file.close()
        return figure_info


class RectangleTask7(Shape):
    def __init__(self, coordinate_x: float, coordinate_y: float, length_side1: float, length_side2: float):
        super().__init__(coordinate_x, coordinate_y)
        self.side1 = length_side1
        self.side2 = length_side2

    def show(self):
        return f"INFO: X = {self.x}, Y = {self.y}, Length side 1 = {self.side1}, Length side 2 = {self.side2}"

    def save(self):
        file = open("square.txt", "w")
        file.write(
            f"INFO: Type: Square, X = {self.x}, Y = {self.y}, Length side 1 = {self.side1}, Length side 2 = {self.side2}")
        file.close()

    def load(self, filename: str):
        file = open(filename, "r")
        figure_info = file.read()
        file.close()
        return figure_info


class CircleTask7(Shape):
    def __init__(self, coordinate_x: float, coordinate_y: float, radius: float):
        super().__init__(coordinate_x, coordinate_y)
        self.r = radius

    def show(self):
        return f"INFO: X = {self.x}, Y = {self.y}, Radius = {self.r}"

    def save(self):
        file = open("square.txt", "w")
        file.write(f"INFO: Type: Square, X = {self.x}, Y = {self.y}, Radius = {self.r}")
        file.close()

    def load(self, filename: str):
        file = open(filename, "r")
        figure_info = file.read()
        file.close()
        return figure_info


class Ellipse(Shape):
    def __init__(self, coordinate_x: float, coordinate_y: float, length_side1: float, length_side2: float):
        super().__init__(coordinate_x, coordinate_y)
        self.side1 = length_side1
        self.side2 = length_side2

    def show(self):
        return f"INFO: X = {self.x}, Y = {self.y}, Length side 1 = {self.side1}, Length side 2 = {self.side2}"

    def save(self):
        file = open("square.txt", "w")
        file.write(
            f"INFO: Type: Square, X = {self.x}, Y = {self.y}, Length side 1 = {self.side1}, Length side 2 = {self.side2}")
        file.close()

    def load(self, filename: str):
        file = open(filename, "r")
        figure_info = file.read()
        file.close()
        return figure_info


list_figure = []
for i in range(0, 5):
    tmp = Square(3+i, 5+i, 10+i)
    list_figure.append(tmp)

for i in range(0, 5):
    tmp = RectangleTask7(1 + i, 3 + i, 9 + i, 7 + i)
    list_figure.append(tmp)

for i in range(0, 5):
    tmp = CircleTask7(2 + i, 4 + i, 5 + i)
    list_figure.append(tmp)

for i in range(0, 5):
    tmp = Ellipse(2 + i, 4 + i, 7 + i, 8 + i)
    list_figure.append(tmp)

for i in list_figure:
    i.save()

list_figure2 = [0 for i in range(len(list_figure))]

for i in range(len(list_figure)):
    list_figure2[i] = list_figure[i]

list_figure.clear()

for i in list_figure2:
    print(i.show())
