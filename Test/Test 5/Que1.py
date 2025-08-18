D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter the amount: "))
count_notes = {}

for note in D:
    if amount >= note:
        count_notes[note] = amount // note
        amount = amount % note

print("Minimum notes needed are:")
total_notes = 0
for note, count in count_notes.items():
    print(f"{note} : {count}")
    total_notes += count

print("Total number of notes =", total_notes)
