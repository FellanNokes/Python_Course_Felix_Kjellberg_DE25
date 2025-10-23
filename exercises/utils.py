from numbers import Number

def validate_positive_number(value) -> None:
        if not isinstance(value, Number):
            raise TypeError (f"Value needs to be a number not {type(value)}")
        
        if value < 0:
            raise ValueError(f"Value can't be negative, not {value}")