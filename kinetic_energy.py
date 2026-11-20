# name: amaney Ibrahim
#Course number: CMP-131
#Week number: 9
#Lab number: 1
# assignement: kinetic energy program
# date: 11/19/26

# Function to calculate kinetic energy
def kineticEnergy(mass, velocity):
    energy = 0.5 * mass * velocity ** 2
    return energy


# Main function
def main():
    print("============ ~ Kinetic Energy Calculator ~ ============")
    print("-------------------------------------------------------")

    mass = float(input("Enter the mass in kilograms: "))
    velocity = float(input("Enter the velocity in meters per second: "))

    if mass < 0 or velocity < 0:
        print("Error: Mass and velocity cannot be negative.")
    else:
        energy = kineticEnergy(mass, velocity)

        print()
        print("============ ~ Kinetic Energy Summary ~ ============")
        print("----------------------------------------------------")
        print(f"Mass: {mass} kg")
        print(f"Velocity: {velocity} m/s")
        print(f"Kinetic Energy: {energy:.2f} joules")


main()
