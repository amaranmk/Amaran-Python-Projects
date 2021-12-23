"""Interesting operator calculator."""

__author__ = "730484862"

left_var: int = int(input("Left-hand side: "))
right_var: int = int(input("Right-hand side: "))

left_right_exponent: int = left_var ** right_var
left_right_division: float = left_var / right_var
left_right_int_division: int = left_var // right_var
left_right_remainder: int = left_var % right_var

print(str(left_var) + " ** " + str(right_var) + " is " + str(left_right_exponent))
print(str(left_var) + " / " + str(right_var) + " is " + str(left_right_division))
print(str(left_var) + " // " + str(right_var) + " is " + str(left_right_int_division))
print(str(left_var) + " % " + str(right_var) + " is " + str(left_right_remainder))
