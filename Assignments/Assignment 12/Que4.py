#Python Program to Form a New String where the First Character and the Last Character have been Exchanged.
s = "python"
if len(s) > 1:
    new_s = s[-1] + s[1:-1] + s[0]
else:
    new_s = s
print(new_s)
