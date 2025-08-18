total_days = int(input("Enter the total number of days: "))

years = total_days // 365
remaining_days = total_days % 365
weeks = remaining_days // 7
days = remaining_days % 7

print("\nEquivalent time is:")
print("Years:", years)
print("Weeks:", weeks)
print("Days:", days)