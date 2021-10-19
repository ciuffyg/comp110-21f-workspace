"""Demonstrations of dictionary capabilities."""

__author__ = "730394262"

# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary by its key
schools.pop("Duke")

# Test for the existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("no key 'Duke' in schools")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200
 
print(schools)

# Demonstraton of dictionary literals

# empty dictionary literal
schools = {}
print(schools)

# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19400,
    "Dukie": 6717,
    "NCSU": 26150
}

print(schools)

# What happns when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")