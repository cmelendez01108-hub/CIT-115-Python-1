# Code Compound Intrest Loops

# Function to get correct number
def get_number(sPrompt, AllowZero, AllowNeg):
    while True:
        try:
            fValue = float(input(sPrompt))

            if not AllowNeg and fValue < 0:
                print("Value cannot be negative.\n")
                continue

            if not AllowZero and fValue == 0:
                print("Value cannot be zero.\n")
                continue

            return fValue
        except:
            print("Input must be a number.\n")


# Input
fDeposit = get_number("Enter Deposit: ", False, False)
fRatePct = get_number("Enter Interest Rate Percentage: ", False, False)
iMonths = int(get_number("Enter Number of Months: ", False, False))
fGoal = get_number("Enter Goal Amount: ", True, False)

# Change rate to decimal
fMonthlyRate = (fRatePct / 100.0) / 12.0

# Compound given for # of months
print("\nMonthly Balances:")
fBalance = fDeposit

for iMonth in range(1, iMonths + 1):
    fInterest = fBalance * fMonthlyRate
    fBalance = fBalance + fInterest
    print("Month " + str(iMonth) + ": $" + format(fBalance, ",.2f"))

# Months to reach the goal
fProjected = fDeposit
iGoalMonths = 0

while fProjected < fGoal:
    fInterest = fProjected * fMonthlyRate
    fProjected = fProjected + fInterest
    iGoalMonths = iGoalMonths + 1

print("\nMonths to Reach Goal: " + str(iGoalMonths))
