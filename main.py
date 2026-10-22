principal=float(input("Enter Principal : "))
rate=float(input("Enter Rate : "))
time=float(input("Enter Time : "))
si=(principal*rate*time)/100
print(si)
print("The simple interest of principal" + str(principal) + "at the rate of" + str(rate) + "within" + str(time) + "months will be" + str(si))
print("The simple interest of principal {0} at the rate of {1} within {2} months will be {3}".format(principal, rate, time, si))
print(f"The simple interest of principle {principal} at the rate of {rate} within {time} months will be {si}")