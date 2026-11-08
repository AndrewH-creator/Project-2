
"""
Program: Progressive Load Workout Generator
Author: Andrew Hissong
Purpose: Creates and manages workout plans containing exercises.
Resources: Python Crash Course, Chapters 8-9. No starter code used.
Date: November 7, 2026
"""


class Workout:
    """Represent a workout containing multiple exercises."""

    def __init__(self, name, fitness_goal, difficulty):
        """Initialize a workout with its basic information."""
        self.name = name
        self.fitness_goal = fitness_goal
        self.difficulty = difficulty
        self.exercises = []

    def add_exercise(self, exercise):
        """Add an exercise object to the workout."""
        self.exercises.append(exercise)

    def remove_exercise(self, exercise_name):
        """Remove an exercise by its name."""
        for exercise in self.exercises:
            if exercise.name.lower() == exercise_name.lower():
                self.exercises.remove(exercise)
                return True

        return False

    def get_total_exercises(self):
        """Return the number of exercises in the workout."""
        return len(self.exercises)

    def display_workout(self):
        """Return a formatted description of the workout."""
        workout_details = [
            f"Workout: {self.name}",
            f"Goal: {self.fitness_goal}",
            f"Difficulty: {self.difficulty}",
            "",
            "Exercises:"
        ]

        for exercise in self.exercises:
            workout_details.append(exercise.describe_exercise())

        return "\n".join(workout_details)
