#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number = 0;

    // Get the number of credit card
    do
    {
        number = get_long("Number: ");
    }
    while (number < 0);

    // Checksum step 1: Multiply every other 2 digits and add all up
    int evenOrOdd = 0;
    int totalEven = 0;
    int remainder = 0;
    int digitDouble = 0;
    long temp = number;

    while (temp > 0)
    {
        evenOrOdd += 1;

        // For even digits
        if (evenOrOdd % 2 == 0)
        {
            remainder = temp % 10;
            digitDouble = remainder * 2;

            if (remainder < 5)
            {
                totalEven += digitDouble;
            }
            else
            {
                // Add digit by digit instead when digitDouble is greater than 10
                while (digitDouble > 0)
                {
                    totalEven += digitDouble % 10;
                    digitDouble = digitDouble / 10;
                }
            }
        }

        temp = temp / 10;
    }

    // Checksum step 2: Add the sum in step 1 to the digits that are not multiplied by 2
    int total = totalEven;
    temp = number;
    evenOrOdd = 0;

    while (temp > 0)
    {
        evenOrOdd += 1;

        // For odd digits
        if (evenOrOdd % 2 == 1)
        {
            remainder = temp % 10;
            total += remainder;
        }

        temp = temp / 10;
    }

    // For card length and starting digits
    int length = 0;
    int starting = 0;
    temp = number;

    // Calculate the card length
    while (temp > 0)
    {
        length += 1;
        temp = temp / 10;
    }

    if (length == 15)
    {
        // Calculate the first two starting digits
        for (int i = 0; i < 15; i++)
        {
            if (i == 13)
            {
                starting = number % 10;
            }
            else if (i == 14)
            {
                starting = ((number % 10) * 10) + starting;
            }

            number = number / 10;
        }

        // To determine whether it is a valid American Express card
        if (starting == 34 || starting == 37)
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else if (length == 13)
    {
        // Calculate the first starting digit
        for (int i = 0; i < 13; i++)
        {
            if (i == 12)
            {
                starting = number % 10;
            }

            number = number / 10;
        }

        // To determine whether it is a valid Visa card
        if (starting == 4)
        {
            // Checksum step 3: Check whether Visa card is valid or not
            if (total % 10 == 0)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
    }
    else if (length == 16)
    {
        // Calculate the first two starting digits
        for (int i = 0; i < 16; i++)
        {
            if (i == 14)
            {
                starting = number % 10;
            }
            else if (i == 15)
            {
                starting = ((number % 10) * 10) + starting;
            }

            number = number / 10;
        }

        // To determine whether it is a valid Visa card or MasterCard
        if (starting >= 40 && starting <= 49)
        {
            // Checksum step 3: Check whether Visa card is valid or not
            if (total % 10 == 0)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (starting == 51 || starting == 52 || starting == 53 || starting == 54 || starting == 55)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}