"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730484862"


class Simpy:
    """Allows us to work with numerical data in a more natural way."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Construct a list of floats."""
        self.values = values

    def __str__(self) -> str:
        """Produce a str representation of a list of floats."""
        return f"Simpy({self.values})"

    def fill(self, fvalue: float, numint: int) -> None:
        """Fills the list with a specific number of repeating values."""
        result: list[float] = []
        i: int = 0
        while i < numint:
            result.append(fvalue)
            i += 1
        self.values = result

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills the list with a range of values."""
        result: list[float] = [start]
        prev_value: float = start
        if step != 0.0:
            while stop != prev_value + step:
                result.append(prev_value + step)
                prev_value += step
        elif step == 0.0:
            raise IndexError
        self.values = result

    def sum(self) -> float:
        """Returns sum of all items in the list."""
        result: float = sum(self.values)
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload the addition operator."""
        result: list[float] = []
        i: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item + rhs)
        elif len(self.values) == len(rhs.values):
            while i < len(self.values):
                result.append(self.values[i] + rhs.values[i])
                i += 1
        else:
            raise IndexError
        return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload the power operator."""
        result: list[float] = []
        i: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item ** rhs)
        elif len(self.values) == len(rhs.values):
            while i < len(self.values):
                result.append(self.values[i] ** rhs.values[i])
                i += 1
        else:
            raise IndexError
        return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload the equal to operator."""
        result: list[bool] = []
        i: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
        elif len(self.values) == len(rhs.values):
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        else:
            raise IndexError
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload the greater than to operator."""
        result: list[bool] = []
        i: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
        elif len(self.values) == len(rhs.values):
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        else:
            raise IndexError
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload the subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: list[float] = []
            i: int = 0
            while i < len(rhs):
                if rhs[i]:
                    result.append(self.values[i])
                i += 1
            return Simpy(result)
