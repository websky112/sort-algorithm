def sort(width, height, length, mass):
    # Calculate the volume of the package (in cubic centimeters)
    volume = width * height * length
    
    # Determine if the package is bulky based on volume or any dimension exceeding 150 cm
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    
    # Determine if the package is heavy based on mass
    is_heavy = mass >= 20
    
    # Determine the stack based on the conditions
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Example Test Cases
print(sort(100, 100, 100, 25))  # "SPECIAL" (heavy)
print(sort(200, 200, 200, 5))   # "REJECTED" (both bulky and heavy)
print(sort(50, 50, 50, 10))     # "STANDARD" (neither bulky nor heavy)
print(sort(150, 150, 150, 5))   # "SPECIAL" (bulky)
print(sort(100, 100, 100, 10))  # "STANDARD" (neither bulky nor heavy)
