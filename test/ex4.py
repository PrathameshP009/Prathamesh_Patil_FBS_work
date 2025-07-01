print("Enter details for Room 1:")
interior_area1 = float(input("  Interior wall area (sq.m): "))
exterior_area1 = float(input("  Exterior wall area (sq.m): "))
interior_cost1 = float(input("  Cost per sq.m for interior painting: "))
exterior_cost1 = float(input("  Cost per sq.m for exterior painting: "))

print("\nEnter details for Room 2:")
interior_area2 = float(input("  Interior wall area (sq.m): "))
exterior_area2 = float(input("  Exterior wall area (sq.m): "))
interior_cost2 = float(input("  Cost per sq.m for interior painting: "))
exterior_cost2 = float(input("  Cost per sq.m for exterior painting: "))

interior_total = (interior_area1 * interior_cost1) + (interior_area2 * interior_cost2)
exterior_total = (exterior_area1 * exterior_cost1) + (exterior_area2 * exterior_cost2)
total_cost = interior_total + exterior_total

print(f"\nTotal interior painting cost: ₹{interior_total:.2f}")
print(f"Total exterior painting cost: ₹{exterior_total:.2f}")
print(f"Total cost to paint both rooms: ₹{total_cost:.2f}")
