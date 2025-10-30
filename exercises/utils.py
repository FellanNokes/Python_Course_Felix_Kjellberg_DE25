from numbers import Number

def validate_number(value):
    if not isinstance(value, Number):
                raise TypeError(f"value must be number not {type(value)}")

def validate_positive_number(value) -> None:
        validate_number(value)
        if value < 0:
            raise ValueError(f"Value can't be negative, not {value}")