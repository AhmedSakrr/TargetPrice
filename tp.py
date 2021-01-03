o = float(input("Enter Original Buy/Sell Price: " ))
c = float(input("Enter Comission Percentage: "))
t = float(input("Enter Target Profit Percentage: "))
LorS = int(input("Long or Short? (1 for long, 0 for short): "))

c = c / 100
t = t / 100

breakEven = (o * (c+1)) / (1-c)
targetPriceLong = (o*(1+t+c))/(1-c)
targetPriceShort = (o*(1-c-t))/(1+c)

print("")

if LorS == 1:
	print "Break Even Price = ", breakEven
	print "Target Price = ", targetPriceLong

if LorS == 0:
	print "Break Even Price = ", o - (breakEven - o)
	print "Target Price = ", targetPriceShort

print("")

# George Smith 2021
