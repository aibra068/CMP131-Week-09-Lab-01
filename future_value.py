# name: amaney Ibrahim
#Course number: CMP-131
#Week number: 9
#Lab number: 1
# assignement: future value program
# date: 11/19/26

# Function to calculate future value
def futureValue(present_value, interest_rate, months):
    future_value = present_value * (1 + interest_rate) ** months
    return future_value


# Main function
def main():
    print("============ ~ Future Value Calculator ~ ============")
    print("-----------------------------------------------------")

    present_value = float(input("Enter the present value: $"))
    interest_rate = float(input("Enter the monthly interest rate (%): "))
    months = int(input("Enter the number of months: "))

    if present_value < 0 or interest_rate < 0 or months <= 0:
        print("Error: Please enter valid positive values.")
    else:
        decimal_rate = interest_rate / 100

        future_value = futureValue(present_value, decimal_rate, months)

        print()
        print("============ ~ Savings Account Summary ~ ============")
        print("-----------------------------------------------------")
        print(f"Present Value: ${present_value:.2f}")
        print(f"Monthly Interest Rate: {interest_rate}%")
        print(f"Number of Months: {months}")
        print(f"Future Value: ${future_value:.2f}")


main()
