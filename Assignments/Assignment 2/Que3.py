feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

total_meters = (feet * 0.3048) + (inches * 0.0254)

meters = int(total_meters)
centimeters = (total_meters - meters) * 100

# Display result
print("\nEquivalent distance is:")
print(meters, "meters and", round(centimeters, 2),"centimeters")