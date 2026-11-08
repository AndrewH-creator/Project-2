
"""
Program: Progressive Load Workout Generator
Author: Andrew Hissong
Purpose: Generates workout routines based on fitness goals and experience.
Resources: Python Crash Course, Chapters 8-9. No starter code used.
Date: November 7, 2026
"""

from exercise import StrengthExercise, CardioExercise
from workout import Workout


def generate_workout(fitness_goal, experience_level):
    """Generate a workout based on the user's goal and experience level."""

    workout = Workout(
        "Personalized Workout",
        fitness_goal,
        experience_level
    )

    # Choose workout details based on experience.
    if experience_level.lower() == "beginner":
        sets = 2
        repetitions = 10
        weight = 10
    elif experience_level.lower() == "intermediate":
        sets = 3
        repetitions = 12
        weight = 20
    elif experience_level.lower() == "advanced":
        sets = 4
        repetitions = 8
        weight = 30
    else:
        raise ValueError(
            "Experience level must be beginner, intermediate, or advanced."
        )

    # Add exercises based on the user's fitness goal.
    if fitness_goal.lower() == "strength":
        workout.add_exercise(
            StrengthExercise("Squats", "Legs", sets, repetitions, weight)
        )
        workout.add_exercise(
            StrengthExercise("Push-ups", "Chest", sets, repetitions, 0)
        )
        workout.add_exercise(
            StrengthExercise("Dumbbell Rows", "Back", sets, repetitions, weight)
        )

    elif fitness_goal.lower() == "endurance":
        workout.add_exercise(
            CardioExercise("Walking", "Full Body", 1, 0, 20)
        )
        workout.add_exercise(
            CardioExercise("Cycling", "Legs", 1, 0, 15)
        )
        workout.add_exercise(
            CardioExercise("Jogging", "Full Body", 1, 0, 10)
        )

    elif fitness_goal.lower() == "general fitness":
        workout.add_exercise(
            StrengthExercise("Bodyweight Squats", "Legs", sets, repetitions, 0)
        )
        workout.add_exercise(
            StrengthExercise("Push-ups", "Chest", sets, repetitions, 0)
        )
        workout.add_exercise(
            CardioExercise("Walking", "Full Body", 1, 0, 15)
        )

    else:
        raise ValueError(
            "Fitness goal must be strength, endurance, or general fitness."
        )

    return workout
