
"""
Program: Progressive Load Workout Generator
Author: Andrew Hissong
Purpose: Tests workout creation and exercise management.
Resources: Python Crash Course, Chapter 11. No starter code used.
Date: November 7, 2026
"""

from exercise import StrengthExercise
from workout import Workout


def test_workout_creation():
    """Verify that a workout is initialized correctly."""
    workout = Workout("Upper Body", "Strength", "Beginner")

    assert workout.name == "Upper Body"
    assert workout.fitness_goal == "Strength"
    assert workout.difficulty == "Beginner"
    assert workout.exercises == []


def test_add_exercise():
    """Verify that an exercise can be added to a workout."""
    workout = Workout("Leg Day", "Strength", "Beginner")
    exercise = StrengthExercise("Squats", "Legs", 2, 10, 20)

    workout.add_exercise(exercise)

    assert workout.get_total_exercises() == 1
    assert workout.exercises[0].name == "Squats"


def test_remove_exercise():
    """Verify that an exercise can be removed by name."""
    workout = Workout("Leg Day", "Strength", "Beginner")
    exercise = StrengthExercise("Squats", "Legs", 2, 10, 20)

    workout.add_exercise(exercise)

    result = workout.remove_exercise("Squats")

    assert result is True
    assert workout.get_total_exercises() == 0


def test_remove_missing_exercise():
    """Verify that removing a missing exercise returns False."""
    workout = Workout("Leg Day", "Strength", "Beginner")

    result = workout.remove_exercise("Squats")

    assert result is False


def test_display_workout():
    """Verify that workout details include its exercises."""
    workout = Workout("Leg Day", "Strength", "Beginner")
    exercise = StrengthExercise("Squats", "Legs", 2, 10, 20)

    workout.add_exercise(exercise)

    description = workout.display_workout()

    assert "Leg Day" in description
    assert "Strength" in description
    assert "Squats" in description
