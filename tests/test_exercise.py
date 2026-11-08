
"""
Program: Progressive Load Workout Generator
Author: Andrew Hissong
Purpose: Tests exercise classes and inheritance.
Resources: Python Crash Course, Chapter 11. No starter code used.
Date: November 7, 2026
"""

from exercise import Exercise, StrengthExercise, CardioExercise


def test_exercise_creation():
    """Verify that an exercise stores the correct information."""
    exercise = Exercise("Push-ups", "Chest", 3, 10)

    assert exercise.name == "Push-ups"
    assert exercise.muscle_group == "Chest"
    assert exercise.sets == 3
    assert exercise.repetitions == 10


def test_exercise_description():
    """Verify that an exercise returns the correct description."""
    exercise = Exercise("Push-ups", "Chest", 3, 10)

    assert exercise.describe_exercise() == (
        "Push-ups: 3 sets of 10 repetitions (Chest)"
    )


def test_strength_exercise_inheritance():
    """Verify that strength exercises inherit from Exercise."""
    exercise = StrengthExercise(
        "Squats", "Legs", 3, 10, 50
    )

    assert isinstance(exercise, Exercise)
    assert exercise.weight == 50
    assert "50 lbs" in exercise.describe_exercise()


def test_cardio_exercise_inheritance():
    """Verify that cardio exercises inherit from Exercise."""
    exercise = CardioExercise(
        "Walking", "Full Body", 1, 0, 20
    )

    assert isinstance(exercise, Exercise)
    assert exercise.duration == 20
    assert "20 minutes" in exercise.describe_exercise()
