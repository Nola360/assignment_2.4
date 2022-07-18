#Akinola Daramola Jr
#Programming Exercise  2.4
#Due Date 6/12/2022


#items
item1 = int(input("What is the price of item 1?"))
item2 = int(input("What is the price of item 2?"))
item3 = int(input("What is the price of item 3?"))
item4 = int(input("What is the price of item 4?"))
item5 = int(input("What is the price of item 5?"))

#Calculating subtotal of all items
subtotal = item1 + item2 + item3 + item4 + item5
print("Subtotal: " + "$" + str(subtotal))

#Given sales tax
salesTax = .07
print("Sales Tax: " + str(salesTax) + "%")
taxesOwed = subtotal * salesTax

#Sum of subtotal & sales
total = subtotal + taxesOwed
print("Total: " + "$" + str(total))

