#!/usr/bin/python3
"""
inherits from class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """defines class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size - sets width and height as size"""
        self.width = value
        self.height = value

    def __str__(self):
        """prints [Square] (<id>) <x>/<y> - <size>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                self.__class__.__name__, self.id, self.x, self.y,
                self.size)

    def update(self, *args, **kwargs):
        """args and kwargs"""
        if args:
            for cnt, arg in enumerate(args):
                if cnt == 0:
                    self.id = arg
                elif cnt == 1:
                    self.size = arg
                elif cnt == 2:
                    self.x = arg
                else:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic 
