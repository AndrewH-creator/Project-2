
"""
Program: Progressive Load Workout Generator
Author: Andrew Hissong
Purpose: Tracks completed workouts and exercise progress.
Resources: Python Crash Course, Chapters 8-9. No starter code used.
Date: November 7, 2026
"""


class ProgressTracker:
    """Store and manage a user's workout history."""

    def __init__(self):
        """Initialize an empty workout history."""
        self.workout_history = []

    def record_workout(self, workout_name, duration, notes=""):
        """Record a completed workout."""
        if duration <= 0:
            raise ValueError("Workout duration must be greater than zero.")

        workout_record = {
            "workout_name": workout_name,
            "duration": duration,
            "notes": notes
        }

        self.workout_history.append(workout_record)

    def get_total_workouts(self):
        """Return the total number of recorded workouts."""
        return len(self.workout_history)

    def get_total_minutes(self):
        """Calculate the total time spent working out."""
        total_minutes = 0

        for workout in self.workout_history:
            total_minutes += workout["duration"]

        return total_minutes

    def display_progress(self):
        """Return a summary of the user's workout history."""
        if not self.workout_history:
            return "No workouts have been recorded yet."

        summary = ["WORKOUT PROGRESS"]

        for workout in self.workout_history:
            summary.append(
                f"{workout['workout_name']} - "
                f"{workout['duration']} minutes"
            )

            if workout["notes"]:
                summary.append(f"Notes: {workout['notes']}")

        summary.append(
            f"Total workouts: {self.get_total_workouts()}"
        )
        summary.append(
            f"Total minutes: {self.get_total_minutes()}"
        )

        return "\n".join(summary)
