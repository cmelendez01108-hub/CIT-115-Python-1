# Code Compound Intrest
# principal "Principal Investment (PV)"
# rate "Interest Rate (R)"
# time  "Number of Periods (t)"
# compoundings  "number of times compounding occurs (m)"



#INPUT
principal = float(input("Enter the starting principal : "))
rate = float(input("Enter the annual interest Rate : "))
time = float(input("How many times per year is this intrest compounded? "))
compoundings = int(input("Compounding (m): "))

# Convert rate to decimal
decimal_rate = rate / 100

# Calculate future value using the formula:
FV = principal * (1 + rate/compoundings) ** (compoundings * time)
future_value = principal * (1 + decimal_rate / compoundings) ** (compoundings * time)


#OUTPUT
future_value = principal * (1 + decimal_rate / compoundings) ** (compoundings * time)
print(f"Future Value (FV): ${future_value:.2f}")



