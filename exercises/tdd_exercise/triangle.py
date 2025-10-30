from numbers import Number

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, value):
        if not isinstance(value, Number):
            raise TypeError("must be a number")
        
        if value <= 0:
            raise ValueError("base must be larger then 0")
        self._base = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, Number):
            raise TypeError("must be a number")
        if value <= 0:
            raise ValueError("base must be larger then 0")
        self._height = value

    @property
    def area(self):
         return (self.base * self.height)*.5

    def __eq__(self, other):
        return self.height == other.height and self.base == other.base
        
    def __lt__(self, other):
         return self.area<other.area
    
    def __gt__(self, other):
         return self.area>other.area
    
    def __repr__(self):
         return f"Triangle(base = {self.base}, height = {self.height})"