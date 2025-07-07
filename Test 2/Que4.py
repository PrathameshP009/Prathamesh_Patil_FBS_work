length = float(input("Enter the length of the wall (in meters): "))
height = float(input("Enter the height of the wall (in meters): "))
cost_per_sq_meter = float(input("Enter the cost of painting per square meter: "))

total_area = 4 * (length * height)
total_cost = total_area * cost_per_sq_meter

print("Total cost of painting the walls is Rs.",total_cost)