import os
import random
import json
import csv

# Function to generate a character
def generate_character():
    # Step 1: Choose a Class (You can expand this list as needed)
    classes = ['Warrior', 'Wizard', 'Thief', 'Cleric']
    character_class = random.choice(classes)

    # Step 2: Choose a Race (You can expand this list as needed)
    races = ['Human', 'Dwarf', 'Elf', 'Halfling']
    character_race = random.choice(races)

    # Step 3: Assign Attributes
    attributes = {'STR': random.randint(1, 10), 'DEX': random.randint(1, 10), 'INT': random.randint(1, 10)}

    # Step 4: Calculate Hit Points (HP)
    hp = 10 + attributes['STR']

    # Step 5: Calculate Effort (EFF)
    eff = attributes['STR'] + attributes['DEX']

    # Step 6: Calculate Armor Class (AC)
    ac = attributes['DEX']

    # Step 7: Choose Alignment (Optional)
    alignments = ['Good', 'Neutral', 'Evil']
    alignment = random.choice(alignments)

    # Step 8: Background and Personality
    background = 'A mysterious traveler'
    personality = 'Courageous and quick-witted'
    ideals = 'Help those in need'
    bonds = 'Protects a secret treasure'
    flaws = 'Impulsive and reckless'

    # Step 9: Name Your Character
    names = ['bob', 'sally', 'joe','alice']
    name = random.choice(names)

    # Step 10: Create Character Sheet
    character_sheet = {
        'Name': name,
        'Class': character_class,
        'Race' : character_race,
        'Attributes': attributes,
        'HP': hp,
        'EFF': eff,
        'AC': ac,
        'Alignment': alignment,
        'Background': background,
        'Personality': personality,
        'Ideals': ideals,
        'Bonds': bonds,
        'Flaws': flaws
    }

    return character_sheet

# Generate a list of characters
num_characters = 1  # Now it generates only one character per run
characters = [generate_character()]

# Create the "characters" directory if it doesn't exist one level above the script
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'characters')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Output character data to CSV, JSON, and text files in the "characters" directory
for character in characters:
    character_name = character['Name']
    
    # CSV
    with open(os.path.join(output_dir, f'{character_name}.csv'), 'w', newline='') as csvfile:
        fieldnames = character.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(character)

    # JSON
    with open(os.path.join(output_dir, f'{character_name}.json'), 'w') as jsonfile:
        json.dump(character, jsonfile, indent=4)

    # Text
    with open(os.path.join(output_dir, f'{character_name}.txt'), 'w') as txtfile:
        for key, value in character.items():
            txtfile.write(f"{key}: {value}\n")

print("Character data has been generated and saved in the 'characters'")