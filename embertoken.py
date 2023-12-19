import random
import os
import csv

# Step 1: Randomly select a loot category
loot_categories = ['Ancient', 'Epic', 'Cursed', 'Bizarre', 'Shabby']
selected_category = random.choice(loot_categories)

# Step 2: Open the CSV file associated with the selected category
csv_filename = f"loot_tables/loot_table_{selected_category.lower()}.csv"

# Check if the CSV file exists
if os.path.exists(csv_filename):
    # Step 3: Define CSV column names
    columns = ["Table", "Description", "roll", "Alpha", "coin", "Item", "other wearables", "Ring", "Amulet", "Food", "Armor", "Int"]

    # Step 4: Generate a random d100 dice roll
    d100_roll = random.randint(1, 100)

    # Step 5: Search the CSV for a matching roll value
    discovered_item = None

    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if int(row['roll']) == d100_roll:
                discovered_item = row['Item']
                break

    # Step 6: Print the results
    print(f"Treasure Category: {selected_category}")
    print(f"Simulated Dice Roll (d100): {d100_roll}")
    if discovered_item:
        print(f"Discovered Item: {discovered_item}")
    else:
        print("No matching item found for the roll.")
else:
    print(f"CSV file for '{selected_category}' category not found.")

