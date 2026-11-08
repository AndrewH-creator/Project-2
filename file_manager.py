
"""
Program: Progressive Load Workout Generator
Author: Andrew Hissong
Purpose: Saves and loads workout information using JSON files.
Resources: Python Crash Course, Chapters 10. No starter code used.
Date: November 7, 2026
"""

import json
from pathlib import Path


def save_data(data, filename):
    """Save structured Python data to a JSON file."""
    file_path = Path(filename)

    try:
        # Create the folder if it does not already exist.
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    except OSError as error:
        print(f"Could not save data: {error}")
        return False


def load_data(filename):
    """Load information from a JSON file."""
    file_path = Path(filename)

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []

    except json.JSONDecodeError:
        print(f"Could not read JSON data from: {filename}")
        return []

    except OSError as error:
        print(f"Could not load data: {error}")
        return []
