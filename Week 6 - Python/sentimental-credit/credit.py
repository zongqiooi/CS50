# Get the number of credit card
while True:
    try:
        number = int(input("Number: "))
    except ValueError:
        number = -1
    if number > 0:
        break

# Checksum step 1: Multiply every other 2 digits and add all up
evenOrOdd = 0
totalEven = 0
temp = number

while temp > 0:
    evenOrOdd += 1
    # For even digits
    if evenOrOdd % 2 == 0:
        remainder = temp % 10
        digitDouble = remainder * 2
        if remainder < 5:
            totalEven += digitDouble
        else:
            # Add digit by digit instead when digitDouble is greater than 10
            while digitDouble > 0:
                totalEven += digitDouble % 10
                digitDouble = digitDouble // 10
    temp = temp // 10

# Checksum step 2: Add the sum in step 1 to the digits that are not multiplied by 2
evenOrOdd = 0
temp = number
total = totalEven

while temp > 0:
    evenOrOdd += 1
    # For odd digits
    if evenOrOdd % 2 == 1:
        remainder = temp % 10
        total += remainder
    temp = temp // 10

# For card length and starting digits
length = 0
starting = 0
temp = number

# Calculate the card length
while temp > 0:
    length += 1
    temp = temp // 10

if length == 15:
    # Calculate the first two starting digits
    for i in range(15):
        if i == 13:
            starting = number % 10
        elif i == 14:
            starting = ((number % 10) * 10) + starting
        number = number // 10

    # To determine whether it is a valid American Express card
    if starting == 34 or starting == 37:
        print("AMEX")
    else:
        print("INVALID")
elif length == 13:
    # Calculate the first starting digit
    for i in range(13):
        if i == 12:
            starting = number % 10
        number = number // 10

    # To determine whether it is a valid Visa card
    if starting == 4:
        # Checksum step 3: Check whether Visa card is valid or not
        if total % 10 == 0:
            print("VISA")
        else:
            print("INVALID")
elif length == 16:
    # Calculate the first two starting digits
    for i in range(16):
        if i == 14:
            starting = number % 10
        elif i == 15:
            starting = ((number % 10) * 10) + starting
        number = number // 10

    # To determine whether it is a valid Visa card or MasterCard
    if starting >= 40 and starting <= 49:
        # Checksum step 3: Check whether Visa card is valid or not
        if total % 10 == 0:
            print("VISA")
        else:
            print("INVALID")
    elif starting in [51, 52, 53, 54, 55]:
        print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")