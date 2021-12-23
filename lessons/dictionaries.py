"""Deomstrations of dictionary capabilities."""

# Declaring the tpye of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()
# We can do the first 2 in one line

# Set a key-value pairing in the dicitionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students ")  # We can use single quotes or double quotes. 

# Remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {}  # Same as dict()
print(schools)

# alternatively, intiialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}  # Can also make a new line after comma after each value
print(schools)

# What happens when a key does not exist?
print(schools["UNCC"])