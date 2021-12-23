"""Relational operator checker."""

__author__ = "730484862"

left_var: int = int(input("Left-hand side: "))
right_var: int = int(input("Right-hand side: "))

left_right_greater_than: bool = left_var < right_var
left_right_less_than_or_equal_to: bool = left_var >= right_var
left_right_equal_to: bool = left_var == right_var
left_right_not_equal: bool = left_var != right_var

print(str(left_var) + " < " + str(right_var) + " is " + str(left_right_greater_than))
print(str(left_var) + " >= " + str(right_var) + " is " + str(left_right_less_than_or_equal_to))
print(str(left_var) + " == " + str(right_var) + " is " + str(left_right_equal_to))
print(str(left_var) + " != " + str(right_var) + " is " + str(left_right_not_equal))
