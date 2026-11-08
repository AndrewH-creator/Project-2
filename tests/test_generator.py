
"""
Program: Progressive Load Workout Generator
Author: Andrew Hissong
Purpose: Tests workout generation and input validation.
Resources: Python Crash Course, Chapter 11. No starter code used.
Date: November 7, 2026
"""

import pytest

from workout_generator import generate_workout


def test_generate_strength_workout():
    """Verify that a strength workout contains the expected exercises."""
    workout = generate_workout("strength", "beginner")

    assert workout.fitness_goal == "strength"
    assert workout.difficulty == "beginner"
    assert workout.get_total_exercises() == 3


def test_generate_endurance_workout():
    """Verify that an endurance workout contains cardio exercises."""
    workout = generate_workout("endurance", "beginner")

    assert workout.get_total_exercises() == 3

    for exercise in workout.exercises:
        assert exercise.duration > 0


def test_generate_general_fitness_workout():
    """Verify that a general fitness workout is generated."""
    workout = generate_workout("general fitness", "intermediate")

    assert workout.fitness_goal == "general fitness"
    assert workout.difficulty == "intermediate"
    assert workout.get_total_exercises() == 3


def test_invalid_fitness_goal():
    """Verify that an invalid fitness goal raises an error."""
    with pytest.raises(ValueError):
        generate_workout("weight loss", "beginner")


def test_invalid_experience_level():
    """Verify that an invalid experience level raises an error."""
    with pytest.raises(ValueError):
        generate_workout("strength", "expert")
