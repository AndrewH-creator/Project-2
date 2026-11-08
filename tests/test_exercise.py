
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



def test_recommend_weight_increase():
    """Verify that successful training recommends more weight."""
    exercise = StrengthExercise("Squats", "Legs", 3, 10, 20)

    recommended = exercise.get_recommended_weight(True)

    assert recommended == 25


def test_keep_current_weight():
    """Verify that unsuccessful training keeps the same weight."""
    exercise = StrengthExercise("Squats", "Legs", 3, 10, 20)

    recommended = exercise.get_recommended_weight(False)

    assert recommended == 20


def test_custom_weight_increment():
    """Verify that a custom weight increase works."""
    exercise = StrengthExercise("Squats", "Legs", 3, 10, 20)

    recommended = exercise.get_recommended_weight(True, 10)

    assert recommended == 30


def test_invalid_weight_increment():
    """Verify that zero or negative increments raise an error."""
    exercise = StrengthExercise("Squats", "Legs", 3, 10, 20)

    import pytest

    with pytest.raises(ValueError):
        exercise.get_recommended_weight(True, 0)

