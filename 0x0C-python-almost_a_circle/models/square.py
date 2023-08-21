#!/usr/bin/python3
""" Rec class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class reps a square and (inherits) from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes new Square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter meth for size."""
        return self.width

    @size.setter
    def size(self, val):
        """Setter for size."""
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """
        Updates the attr of d Square instance.
        """
        if args:
            attr_lisst = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attr_lisst):
                    setattr(self, attr_lisst[i], arg)
                else:
                    break
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dict rep of a Rec.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
