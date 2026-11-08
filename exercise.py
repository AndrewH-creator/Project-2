
"""
Program: Progressive Load Workout Generator
Author: Andrew Hissong
Purpose: Defines exercise objects used to build workout plans.
Resources: Python Crash Course, Chapters 8-9. No starter code used.
Date: November 7, 2026
"""


class Exercise:
    """Represent a basic exercise in a workout program."""

    def __init__(self, name, muscle_group, sets, repetitions):
        """Initialize an exercise with its basic information."""
        self.name = name
        self.muscle_group = muscle_group
        self.sets = sets
        self.repetitions = repetitions

    def describe_exercise(self):
        """Return a description of the exercise."""
        return (
            f"{self.name}: {self.sets} sets of "
            f"{self.repetitions} repetitions "
            f"({self.muscle_group})"
        )


class StrengthExercise(Exercise):
    """Represent a strength exercise."""

    def __init__(self, name, muscle_group, sets, repetitions, weight):
        """Initialize a strength exercise with a weight."""
        super().__init__(name, muscle_group, sets, repetitions)
        self.weight = weight

    def describe_exercise(self):
        """Return exercise details including the weight."""
        return (
            f"{self.name}: {self.sets} sets of "
            f"{self.repetitions} repetitions at "
            f"{self.weight} lbs ({self.muscle_group})"
        )


class CardioExercise(Exercise):
    """Represent a cardio exercise."""

    def __init__(self, name, muscle_group, sets, repetitions, duration):
        """Initialize a cardio exercise with a duration."""
        super().__init__(name, muscle_group, sets, repetitions)
        self.duration = duration

    def describe_exercise(self):
        """Return exercise details including the duration."""
        return (
            f"{self.name}: {self.duration} minutes "
            f"of cardio ({self.muscle_group})"
        )
