
"""
Program: Progressive Load Workout Generator
Author: Andrew Hissong
Purpose: Provides the main menu and connects all workout features.
Resources: Python Crash Course, Chapters 8-10. No starter code used.
Date: November 7, 2026
"""

from workout_generator import generate_workout
from exercise import StrengthExercise
from progress_tracker import ProgressTracker
from file_manager import save_data, load_data


# Store workout information in the data folder.
WORKOUT_FILE = "data/workouts.json"
PROGRESS_FILE = "data/progress.json"


def display_menu():
    """Display the main menu."""
    print("\n=== PROGRESSIVE LOAD WORKOUT GENERATOR ===")
    print("1. Generate a workout")
    print("2. Record a completed workout")
    print("3. View workout progress")
    print("4. View saved workout history")
    print("5. Update exercise weight")
    print("6. Exit")


def generate_and_save_workout():
    """Ask the user for preferences and generate a workout."""
    print("\nChoose a fitness goal:")
    print("1. Strength")
    print("2. Endurance")
    print("3. General Fitness")

    goal_options = {
        "1": "strength",
        "2": "endurance",
        "3": "general fitness"
    }

    goal_choice = input("Enter your choice: ")

    if goal_choice not in goal_options:
        print("Invalid fitness goal.")
        return

    print("\nChoose your experience level:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")

    experience_options = {
        "1": "beginner",
        "2": "intermediate",
        "3": "advanced"
    }

    experience_choice = input("Enter your choice: ")

    if experience_choice not in experience_options:
        print("Invalid experience level.")
        return

    try:
        workout = generate_workout(
            goal_options[goal_choice],
            experience_options[experience_choice]
        )

        print("\n" + workout.display_workout())

        # Convert the workout into information JSON can store.
        workout_data = {
            "name": workout.name,
            "fitness_goal": workout.fitness_goal,
            "difficulty": workout.difficulty,
            "exercises": []
        }

        for exercise in workout.exercises:
            workout_data["exercises"].append({
                "name": exercise.name,
                "muscle_group": exercise.muscle_group,
                "sets": exercise.sets,
                "repetitions": exercise.repetitions,
                "details": exercise.describe_exercise()
            })

        saved_workouts = load_data(WORKOUT_FILE)

        if not isinstance(saved_workouts, list):
            saved_workouts = []

        saved_workouts.append(workout_data)

        if save_data(saved_workouts, WORKOUT_FILE):
            print("\nWorkout saved successfully.")

    except ValueError as error:
        print(f"Error: {error}")


def record_completed_workout(tracker):
    """Record a completed workout and save the progress."""
    print("\nRecord a completed workout.")

    workout_name = input("Workout name: ")

    try:
        duration = int(input("Duration in minutes: "))

        tracker.record_workout(workout_name, duration)

        if save_data(tracker.workout_history, PROGRESS_FILE):
            print("Workout progress saved successfully.")

    except ValueError as error:
        print(f"Invalid entry: {error}")


def view_progress(tracker):
    """Display the user's workout progress."""
    print("\n" + tracker.display_progress())


def view_saved_workouts():
    """Display previously generated workout plans."""
    saved_workouts = load_data(WORKOUT_FILE)

    if not saved_workouts:
        print("\nNo saved workouts found.")
        return

    print("\n=== SAVED WORKOUTS ===")

    for index, workout in enumerate(saved_workouts, start=1):
        print(f"\nWorkout {index}: {workout['name']}")
        print(f"Goal: {workout['fitness_goal']}")
        print(f"Difficulty: {workout['difficulty']}")

        for exercise in workout["exercises"]:
            print(f"- {exercise['details']}")


def update_exercise_weight():
    """Recommend a weight adjustment after a strength exercise."""
    print("\n=== PROGRESSIVE WEIGHT UPDATE ===")

    exercise_name = input("Enter the exercise name: ")

    try:
        current_weight = float(input("Enter the current weight in lbs: "))

        exercise = StrengthExercise(
            exercise_name,
            "Strength",
            3,
            10,
            current_weight
        )

        completed = input(
            "Did you successfully complete your target? (yes/no): "
        ).lower()

        if completed not in ["yes", "no"]:
            print("Please enter yes or no.")
            return

        recommended_weight = exercise.get_recommended_weight(
            completed == "yes"
        )

        print(f"\nExercise: {exercise_name}")
        print(f"Current weight: {current_weight} lbs")
        print(f"Recommended next weight: {recommended_weight} lbs")

    except ValueError as error:
        print(f"Invalid entry: {error}")



def main():
    """Run the main workout application."""
    tracker = ProgressTracker()

    # Load previous progress when the program starts.
    saved_progress = load_data(PROGRESS_FILE)

    if isinstance(saved_progress, list):
        tracker.workout_history = saved_progress

    while True:
        display_menu()
        choice = input("\nChoose an option: ")

        if choice == "1":
            generate_and_save_workout()

        elif choice == "2":
            record_completed_workout(tracker)

        elif choice == "3":
            view_progress(tracker)

        elif choice == "4":
            view_saved_workouts()

        elif choice == "5":
            update_exercise_weight()

        elif choice == "6":
            print("Thank you for using the workout generator!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
