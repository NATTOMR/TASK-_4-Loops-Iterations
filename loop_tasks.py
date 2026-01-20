"""
Loop Demonstration Project
Author: Intern Training Project
Purpose: Demonstrate Python loops, conditions, and real-world use cases
"""

# --------------------------------------------------
# 1. FOR LOOP: Print numbers from 1 to 100
# --------------------------------------------------
print("1. Printing numbers from 1 to 100:")
for number in range(1, 101):
    print(number, end=" ")
print("\n")


# --------------------------------------------------
# 2. WHILE LOOP: Countdown Timer
# --------------------------------------------------
print("2. Countdown Timer:")
countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1

print("🚀 Countdown complete!\n")


# --------------------------------------------------
# 3. BREAK and CONTINUE Example
# --------------------------------------------------
print("3. Break and Continue Example:")

for num in range(1, 11):
    if num == 5:
        print("Skipping number 5 (continue)")
        continue
    if num == 9:
        print("Stopping loop at 9 (break)")
        break
    print(num)

print()


# --------------------------------------------------
# 4. Iterating Over String Characters
# --------------------------------------------------
print("4. Iterating over string characters:")

word = "Python"
for char in word:
    print(char)

print()


# --------------------------------------------------
# 5. Multiplication Table Generator
# --------------------------------------------------
print("5. Multiplication Table (1 to 5):")

for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)

print()


# --------------------------------------------------
# 6. Using range() with Steps
# --------------------------------------------------
print("6. Even numbers from 0 to 20:")

for even in range(0, 21, 2):
    print(even)

print()


# --------------------------------------------------
# 7. Combining Loops with Conditions
# --------------------------------------------------
print("7. Checking pass/fail status:")

scores = [85, 42, 90, 67, 30]

for score in scores:
    if score >= 50:
        print(f"Score {score}: Pass")
    else:
        print(f"Score {score}: Fail")

print()


# --------------------------------------------------
# 8. Real-World Example: Shopping Cart Total
# --------------------------------------------------
print("8. Real-world example: Shopping cart total")

prices = [12.99, 5.49, 3.50, 20.00]
total = 0

for price in prices:
    total += price

print(f"Total bill amount: ${total:.2f}")

print("\n--- End of Loop Demonstration Project ---")
