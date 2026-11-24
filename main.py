
print("=" * 35)
print("       PYTHON MINI TOOLKIT")
print("=" * 35)

name = input("Enter your name: ")

print(f"\nWelcome, {name}!")
print("Your Python journey starts here.")

print("\nAvailable tools:")
print("1. Calculator")
print("2. Multiplication Table")
print("3. Exit")

choice = input("\nChoose an option: ")

if choice == "1":
    print("Calculator coming soon!")

elif choice == "2":
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

elif choice == "3":
    print("Goodbye!")

else:
    print("Invalid option.")
