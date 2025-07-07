import math
radius = 20
length = 50
breadth = 40
cost_per_meter = 35
rounds = 5

semicircle_perimeter = math.pi * radius

rectangle_perimeter = 2 * (length + breadth)

total_perimeter = semicircle_perimeter + rectangle_perimeter

total_wire_length = total_perimeter * rounds

total_cost = total_wire_length * cost_per_meter

print("Total cost of fencing is ₹", round(total_cost,2))