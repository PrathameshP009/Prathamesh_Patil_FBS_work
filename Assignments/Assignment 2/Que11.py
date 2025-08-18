amount = int(input("Enter the amount: "))

notes = [100, 50, 20, 10, 5, 2, 1]

note_count = {}

remaining_amount = amount

for note in notes:
    count = remaining_amount // note
    remaining_amount = remaining_amount % note
    note_count[note] = count

print("\nMinimum number of notes needed:")

total_notes = 0
for note in notes:
    if note_count[note] > 0:
        print(f"{note} : {note_count[note]}")
        total_notes += note_count[note]

print("Total notes:",total_notes)