"""Examples of optional parameters and Union Type parameters."""

from typing import Union


def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting function."""
    result: str = "Hello, "
    if isinstance(name, str):
        return result + name
    elif isinstance(name, float):
        return result + "alien from sector " + str(name)
    else:
        return result + "Comp " + str(name)


# Calling hello with no arguements leads to use of default value
print(hello())
# Calling hello with one arguemnt overrides the default value
print(hello("John"))
print(hello(110))
print(hello(3.14))