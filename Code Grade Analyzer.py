#INPUT
sName = input("Enter the person's name: ")


#INPUT 4 Test_Scores
iTest1 = input("Enter Test Score 1: ")
iTest2 = input("Enter Test Score 2: ")
iTest3 = input("Enter Test Score 3: ")
iTest4 = input("Enter Test Score 4: ")

iTest1 = int(iTest1)
iTest2 = int(iTest2)
iTest3 = int(iTest3)
iTest4 = int(iTest4)

# if else and elif statemets
if iTest1 == str(int(iTest1)):
    if iTest2 == str(int(iTest2)):
        if iTest3 == str(int(iTest3)):
            if iTest4 == str(int(iTest4)):
                print("\nAll test scores entered successfully!")
                print(iTest1, iTest2, iTest3, iTest4)
            else:
                print("Only whole numbers should be entered for test scores.")
        else:
            print("Only whole numbers should be entered for test scores.")
    else:
        print("Only whole numbers should be entered for test scores.")
else:
    print("Only whole numbers should be entered for test scores.")

sDropLowest = input("Drop the lowest grade? (Y/N): ")

if sDropLowest == "Y":
    print("Dropping the lowest grade.")
elif sDropLowest == "y":
    print("Dropping the lowest grade.")
elif sDropLowest == "N":
    print("Keeping all grades.")
elif sDropLowest == "n":
    print("Keeping all grades.")
else:
    print("Please enter Y or N.")


if iTest1 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit
else:
    if iTest2 < 0:
        print("Test scores must be greater than 0.")
        raise SystemExit
    else:
        if iTest3 < 0:
            print("Test scores must be greater than 0.")
            raise SystemExit
        else:
            if iTest4 < 0:
                print("Test scores must be greater than 0.")
                raise SystemExit

if sDropLowest != "Y":
    if sDropLowest != "N":
        print("Enter Y or N to Drop the Lowest Grade.")
        raise SystemExit

fAverage = 0.0

if sDropLowest == "Y":
    lowest = iTest1
    if iTest2 < lowest:
        lowest = iTest2
    if iTest3 < lowest:
        lowest = iTest3
    if iTest4 < lowest:
        lowest = iTest4

    fAverage = (iTest1 + iTest2 + iTest3 + iTest4 - lowest) / 3
else:
    fAverage = (iTest1 + iTest2 + iTest3 + iTest4) / 4

iWhole_Num = int(fAverage)
iDecimal = int((fAverage - iWhole_Num) * 100 + 0.5)  

if iDecimal < 10:
    iDecimal = "0" + str(iDecimal)
else:
    iDecimal = str(iDecimal)

print("Average score: " + str(iWhole_Num) + "." + iDecimal)


if fAverage >= 97.0:
    sGrade = "A+"
elif fAverage >= 94.0:
    sGrade = "A"
elif fAverage >= 90.0:
    sGrade = "A-"
elif fAverage >= 87.0:
    sGrade = "B+"
elif fAverage >= 84.0:
    sGrade = "B"
elif fAverage >= 80.0:
    sGrade = "B-"
elif fAverage >= 77.0:
    sGrade = "C+"
elif fAverage >= 74.0:
    sGrade = "C"
elif fAverage >= 70.0:
    sGrade = "C-"
elif fAverage >= 67.0:
    sGrade = "D+"
elif fAverage >= 64.0:
    sGrade = "D"
elif fAverage >= 60.0:
    sGrade = "D-"
else:
    sGrade = "F"

# Output

print("\n--- Grade Analyzer Results ---")
print("Name: %s" % sName)
print("Average: %.1f" % fAverage)
print("Letter Grade: %s" % sGrade)


