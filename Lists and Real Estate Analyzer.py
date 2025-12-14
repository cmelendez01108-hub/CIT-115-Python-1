# List and Real Estate Analyzer

# Function input from the user
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:  
                print("Error: Enter a positive number greater than zero.")
            else:
                return value  
        except ValueError:  
            print("Error: Invalid input. Please enter a numeric value.")

# Function calculates the median
def getMedian(values):
    values_sorted = sorted(values)
    n = len(values_sorted)
    mid = n // 2

    if n % 2 == 1:  
        return float(values_sorted[mid])
    else:  
        return (values_sorted[mid - 1] + values_sorted[mid]) / 2

# Main function
def main():
    sales = []  
    total = 0.0

    while True:
        fSalesPrice = getFloatInput("Enter property sales value: ")
        sales.append(fSalesPrice)  
        total += fSalesPrice
        print("Sale entered: $" + format(fSalesPrice, ",.2f"))

        # Ask user if they want to continue
        while True:
            another = input("Enter another value Y or N: ").strip().upper()
            if another in ['Y', 'N']:
                break
            else:
                print("Error: Please enter Y or N.")

        if another == 'N':
            break  # Exit the loop

    # Sort sales list for median and min/max
    sales.sort()

    # Show all sales in order
    print("\nAll Sales in Sorted Order:")
    for sale in sales:
        print("$" + format(sale, ",.2f"))

    # Calculate analytics
    minimum = min(sales)
    maximum = max(sales)
    average = total / len(sales)
    median = getMedian(sales)
    commission = total * 0.03

    # Display analytics
    print("\nSales Analytics:")
    print("Minimum Sale: $" + format(minimum, ",.2f"))
    print("Maximum Sale: $" + format(maximum, ",.2f"))
    print("Total Sales: $" + format(total, ",.2f"))
    print("Average Sale: $" + format(average, ",.2f"))
    print("Median Sale: $" + format(median, ",.2f"))
    print("Commission (3%): $" + format(commission, ",.2f"))

# Run program
if __name__ == "__main__":
    main()
