a1= 20
a2= 11
a3= 50
a4 = 82
a5= 25
amt = 100
fair = 100
if(a1<12):
    fair += amt - amt*0.3
elif(a1>59):
    fair += amt*0.5
else:
    fair += amt
print("a1 =",fair)
if(a2<12):
    fair += amt - amt*0.3
elif(a2>59):
    fair += amt*0.5
else:
    fair += amt
print("a2 =",fair)
if(a3<12):
    fair += amt - amt*0.3
elif(a3>59):
    fair += amt*0.5
else:
    fair += amt
print("a3 =",fair)
if(a4<12):
    fair += amt - amt*0.3
elif(a4>59):
    fair += amt*0.5
else:
    fair += amt
print("a4 = ",fair)
if(a5<12):
    fair += amt - amt*0.3
elif(a5>59):
    fair += amt*0.5
else:
    fair += amt
print("a5 = ",fair)