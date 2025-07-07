price1 = float(input("Enter price of product 1: "))
price2 = float(input("Enter price of product 2: "))
price3 = float(input("Enter price of product 3: "))
price4 = float(input("Enter price of product 4: "))
price5 = float(input("Enter price of product 5: "))

total_price = price1 + price2 + price3 + price4 + price5

GST = total_price * 0.18

total_bill = total_price + GST
print("Total bill after adding 18% GST is: ₹", round(total_bill,2))