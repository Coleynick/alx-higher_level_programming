#!/usr/bin/python3
""" Rec Class """


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, (inherits) from Base.
    Attributes:
        _width (int): Private width attr.
        _height (int): Private height att.
        _x (int): Private x attr.
        _y (int): Private y attr.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle instance.
        Args:
            width (int): rec width.
            height: rectangle Height.
            x, y (int, opt): x, y-coordinate of the rectangle's position.
                Defaults to 0.
            id (int, opt): Unique identifier for the obj.
                Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for d width att."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for d width att."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for d height attr."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for d height attr."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for d x attr."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for d x attr."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for d y attr."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for d y attr."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns d area val of the Rec instance. """
        return self.__width * self.__height

    def display(self):
        """ Update the Rec using # chars """
        for i in range(self.__height):
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """ Update d Rec attrs with args in order """
        if args and len(args) > 0:
            attr_lisst = ["id", "width", "height", "x", "y"]
            for i, val in enumerate(args):
                if i < len(attr_lisst):
                    setattr(self, attr_lisst[i], val)
        else:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)

    def __str__(self):
        """ Return str rep of d Rec """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
