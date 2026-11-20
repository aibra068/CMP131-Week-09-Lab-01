# name: amaney Ibrahim
#Course number: CMP-131
#Week number: 9
#Lab number: 1
# assignement: celsius temperature table program
# date: 11/19/26

# Function to convert Fahrenheit to Celsius
def celsius(fahrenheit):
    temperature = (5 / 9) * (fahrenheit - 32)
    return temperature


# Main function
def main():
    print("============ ~ Fahrenheit to Celsius Temperature Table ~ ============")
    print("---------------------------------------------------------------------")
    print("Fahrenheit       Celsius")
    print("------------------------")

    for fahrenheit in range(0, 21):
        temperature = celsius(fahrenheit)
        print(f"{fahrenheit:<16}{temperature:.2f}")


main()
