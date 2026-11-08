
"""
Program: Progressive Load Workout Generator
Author: Andrew Hissong
Purpose: Tests workout progress tracking features.
Resources: Python Crash Course, Chapters 10-11. No starter code used.
Date: November 7, 2026
"""

import pytest
from progress_tracker import ProgressTracker


def test_progress_tracker_starts_empty():
    """Verify that a new tracker has no workout history."""
    tracker = ProgressTracker()

    assert tracker.get_total_workouts() == 0
    assert tracker.get_total_minutes() == 0


def test_record_workout():
    """Verify that a completed workout is recorded."""
    tracker = ProgressTracker()

    tracker.record_workout("Strength Workout", 45, "Good workout")

    assert tracker.get_total_workouts() == 1


def test_total_workouts():
    """Verify that the tracker counts multiple workouts."""
    tracker = ProgressTracker()

    tracker.record_workout("Strength Workout", 45)
    tracker.record_workout("Cardio Workout", 30)

    assert tracker.get_total_workouts() == 2


def test_total_minutes():
    """Verify that workout durations are added together."""
    tracker = ProgressTracker()

    tracker.record_workout("Strength Workout", 45)
    tracker.record_workout("Cardio Workout", 30)

    assert tracker.get_total_minutes() == 75


def test_display_progress():
    """Verify that workout progress displays the correct information."""
    tracker = ProgressTracker()
    tracker.record_workout("Strength Workout", 45, "Good workout")

    result = tracker.display_progress()

    assert "WORKOUT PROGRESS" in result
    assert "Strength Workout" in result
    assert "45 minutes" in result
    assert "Good workout" in result


def test_invalid_workout_duration():
    """Verify that zero or negative durations raise an error."""
    tracker = ProgressTracker()

    with pytest.raises(ValueError):
        tracker.record_workout("Strength Workout", 0)

    with pytest.raises(ValueError):
        tracker.record_workout("Strength Workout", -10)
