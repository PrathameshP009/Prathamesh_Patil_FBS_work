#Python Program to replace every blank space with hyphen in a string.
s = "space to hyphen"
new_s = ""
for char in s:
    if char == " ":
        new_s += "-"
    else:
        new_s += char
print(new_s)
