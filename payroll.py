name = str(input("Enter employee's name:"))
hours = eval(input("Enter number of hours worked in a week:"))
payrate = eval(input("Enter hourly pay rate:"))
fedtax = eval(input("Enter federal tax withholding rate:"))
sttax = eval(input("Enter state tax withholding rate:"))

gpay = payrate * hours
fedpay = gpay * fedtax
stpay = gpay * sttax
netpay = fedpay + stpay

print("Employee's name: ",name)
print("hours worked: ",hours)
print("Pay rate: $",payrate)
print("Gross pay: $",gpay)
print("Deductions: ")
print(" Federal withholding: $",fedpay)
print(" State withholding: $",stpay)
print("Total deductions: $",netpay)
print("Net pay: $", gpay - netpay)