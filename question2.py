
# Write a program that displays the following menu:
# 1. Calculate cube volume.
# 2. Calculate cylinder volume.
# 3. Calculate cone volume
# 4. Exit
print("Menu:")
print("1. Calculate cube volume.")
print("2. Calculate cylinder volume.")
print("3. Calculate cone volume.")
print("4. Exit.")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    side = float(input("Enter the side length of the cube: "))
    volume = side ** 3
    print(f"The volume of the cube is: {volume}")
elif choice == 2:
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    volume = 3.14159 * radius ** 2 * height
    print(f"The volume of the cylinder is: {volume}")
elif choice == 3:
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    volume = (1 / 3) * 3.14159 * radius ** 2 * height
    print(f"The volume of the cone is: {volume}")
elif choice == 4:
    print("Exiting the program.")
else:
    print("Invalid choice. Please enter a number between 1 and 4.")