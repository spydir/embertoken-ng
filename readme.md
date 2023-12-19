# Dungeon Master's Loot Generator Script

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Description

The Dungeon Master's Loot Generator Script is a Python script that allows dungeon masters to simulate the discovery of loot from treasure chests in a tabletop role-playing game. It randomly selects loot categories and generates items based on a d100 dice roll from CSV loot tables.

## Features

- Random selection of loot categories (Ancient, Epic, Cursed, Bizarre, Shabby).
- CSV files for loot tables with customizable item data.
- Simulated d100 dice roll for item generation.
- User-friendly output displaying the discovered item.

## Requirements

- Python 3.6 or higher
- [pandas](https://pandas.pydata.org/) library (for CSV handling)
- [numpy](https://numpy.org/) library (for random number generation)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/dungeon-loot-generator.git
   ```

2. Navigate to the project directory:


```
cd dungeon-loot-generator
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```