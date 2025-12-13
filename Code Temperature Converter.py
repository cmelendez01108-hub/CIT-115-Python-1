# Temperature Converter by Chris Melendez

print("Chris Melendez Temperature Converter:")

# Input
fTemp = float(input("Enter temperature: "))

sScale = input("Is the temp F for Fahrenheit or C for Celsius? ")

# Output
if sScale not in ('F', 'C'):
    print("You must enter a F or C")
else:
    if sScale == 'F':
        if fTemp > 212:
            print("Temperature cannot be > 212")
        else:
            fCelsius = (5.0 / 9.0) * (fTemp - 32)
            print("The Celsius equivalent is: %.1f" % fCelsius)
    elif sScale == 'C':
        if fTemp > 100:
            print("Temperature cannot be > 100")
        else:
            fFahrenheit = (9.0 / 5.0) * fTemp + 32
            print("The Fahrenheit equivalent is: %.1f" % fFahrenheit)

