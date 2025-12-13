import math

# Get input from user
def getFloatInput(sPrompt):
    while True:
        try:
            fValue = float(input(sPrompt + ": "))
            if fValue <= 0:
                print("Error: Value must be a positive, non-zero number.")
            else:
                return fValue
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

# Calculate gallons of paint needed
def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    return int(math.ceil(fSquareFeet / fFeetPerGallon))

# Calculate labor hours
def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    return fLaborHoursPerGallon * iTotalGallons

# Calculate labor cost
def getLaborCost(fLaborHours, fLaborChargePerHour):
    return fLaborHours * fLaborChargePerHour

# Calculate paint cost
def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice

# Sales tax rate for each state
def getSalesTax(sState):
    sState = sState.upper()
    if sState == "CT":
        return 0.06
    elif sState == "MA":
        return 0.0625
    elif sState == "ME":
        return 0.085
    elif sState == "NH":
        return 0.0
    elif sState == "RI":
        return 0.07
    elif sState == "VT":
        return 0.06
    else:
        return 0.0

def showCostEstimate(sCustomerLastName, sState, iTotalGallons, fLaborHours, fPaintCost, fLaborCost, fTotalCost, fSalesTaxAmount):
    sFileName = sCustomerLastName + "_PaintJobOutput.txt"
    
    sOutput = "\nPaint Job Estimate for " + sCustomerLastName + "\n"
    sOutput += "State: " + sState + "\n"
    sOutput += "-----------------------------------\n"
    sOutput += "Total Gallons of Paint Needed: " + str(iTotalGallons) + "\n"
    sOutput += "Total Labor Hours: %.2f\n" % fLaborHours
    sOutput += "Paint Cost: $" + "%.2f" % fPaintCost + "\n"
    sOutput += "Labor Cost: $" + "%.2f" % fLaborCost + "\n"
    sOutput += "Sales Tax: $" + "%.2f" % fSalesTaxAmount + "\n"
    sOutput += "Total Cost: $" + "%.2f" % fTotalCost + "\n"

    print(sOutput)
    
    # Save to file
    outputFile = open(sFileName, "w")
    outputFile.write(sOutput)
    outputFile.close()
    
    print("Output file created: " + sFileName)

def main():
    # User Input
    fSquareFeet = getFloatInput("Enter Square Feet of the Wall")
    fPaintPrice = getFloatInput("Enter Paint Price")
    fFeetPerGallon = getFloatInput("Enter Feet per Gallon of Paint")
    fLaborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon")
    fLaborChargePerHour = getFloatInput("Enter Painting Labor Charge per Hour")
    
    # State and customer info
    sState = input("Enter the state of the job: ")
    sCustomerLastName = input("Enter the customer's last name: ")
    
    # For calculations
    iTotalGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fSalesTaxRate = getSalesTax(sState)
    fSalesTaxAmount = (fPaintCost + fLaborCost) * fSalesTaxRate
    fTotalCost = fPaintCost + fLaborCost + fSalesTaxAmount
    
    # Show and save output
    showCostEstimate(sCustomerLastName, sState, iTotalGallons, fLaborHours, fPaintCost, fLaborCost, fTotalCost, fSalesTaxAmount)

# Run program
if __name__ == "__main__":
    main()
