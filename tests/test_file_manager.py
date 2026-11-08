
"""
Program: Progressive Load Workout Generator
Author: Andrew Hissong
Purpose: Tests JSON saving and loading functions.
Resources: Python Crash Course, Chapters 10-11. No starter code used.
Date: November 7, 2026
"""

import json

from file_manager import save_data, load_data


def test_save_data(tmp_path):
    """Verify that information can be saved to a JSON file."""
    filename = tmp_path / "workouts.json"
    workout_data = [{"name": "Upper Body", "duration": 30}]

    result = save_data(workout_data, filename)

    assert result is True
    assert filename.exists()


def test_load_data(tmp_path):
    """Verify that saved JSON information can be loaded."""
    filename = tmp_path / "workouts.json"
    workout_data = [{"name": "Leg Day", "duration": 45}]

    with filename.open("w", encoding="utf-8") as file:
        json.dump(workout_data, file)

    loaded_data = load_data(filename)

    assert loaded_data == workout_data


def test_load_missing_file(tmp_path):
    """Verify that a missing file returns an empty list."""
    filename = tmp_path / "missing.json"

    result = load_data(filename)

    assert result == []


def test_load_invalid_json(tmp_path):
    """Verify that invalid JSON returns an empty list."""
    filename = tmp_path / "invalid.json"

    filename.write_text("{invalid json", encoding="utf-8")

    result = load_data(filename)

    assert result == []
