# Project 44: Savings Group Ledger

import array

# --- 1. Integers ---
contributions = [200, 500, 300, 700, 400]
total = sum(contributions)
average = total / len(contributions)
minimum = min(contributions)
maximum = max(contributions)

# --- 2. Strings ---
summary = f"Total contributions = {total}, Average = {average:.2f}"
details = f"Minimum = {minimum}, Maximum = {maximum}"
print(summary)
print(details)

# --- 3. Booleans ---
threshold = 450
status = "Above Standard" if average >= threshold else "Below Standard"
print(f"Status: {status}")

# --- 4. Lists ---
print("\n--- List Operations ---")
contributions.append(600)     # add new
contributions.remove(200)     # remove one
contributions.sort()          # sort
print("Updated contributions list:", contributions)

# --- 5. Arrays ---
print("\n--- Array Operations ---")
arr = array.array('i', contributions)
print("Array contents:", arr)
print("Sum of array:", sum(arr))
print("Compare list vs array sums:", sum(contributions) == sum(arr))

# --- 6. Dictionaries ---
print("\n--- Dictionary Operations ---")
ledger = [
    {"id": 1, "name": "Alice", "value": 300},
    {"id": 2, "name": "Bob", "value": 500},
    {"id": 3, "name": "Charlie", "value": 400}
]

# Add new record
ledger.append({"id": 4, "name": "David", "value": 600})

# Update record
ledger[1]["value"] = 550   # Update Bob’s contribution

# Delete record
ledger = [record for record in ledger if record["id"] != 3]

# Compute total values
total_values = sum(record["value"] for record in ledger)

print("Updated ledger:", ledger)
print("Total value in ledger:", total_values)
