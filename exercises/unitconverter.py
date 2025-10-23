from numbers import Number

def validate_positive_number(value) -> None:
        if not isinstance(value, Number):
            raise TypeError (f"Value needs to be a number not {type(value)}")
        
        if value < 0:
            raise ValueError(f"Value can't be negative, not {value}")

class UnitConverter:
    # | means or
    def __init__(self, value: int | float):
        self.value = value

    @property
    def value(self) -> float | int:
        return self._value
    
    @value.setter
    def value(self, new_value) -> None:
        validate_positive_number(new_value)
    
        self._value = new_value


unit_converter = UnitConverter(5)

# shortcut to get this output:
# unit_converter.value = 5
print(f"{unit_converter.value = }")

try:
    unit_converter.value = "5"
except TypeError as err:
    print(err)

try:
    unit_converter.value = -0.1
except ValueError as err:
    print(err)

print(unit_converter.value)