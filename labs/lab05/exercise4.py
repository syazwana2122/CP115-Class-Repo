Item_Name = input("Enter item name: ")
Item_Price = float(input("Enter item price: "))

Quantity = 3
Tax_Rate = 0.06

Sub_Total = Item_Price * Quantity
Tax = Sub_Total * Tax_Rate
Total = Sub_Total + Tax

print("Item Name:", Item_Name)
print("Item Price:", Item_Price)
print("Quantity:", Quantity)
print("Sub Total:", Sub_Total)
print("Tax(6%):", Tax)
print("Total:", Total)