
# Progressive Load Workout Generator

**Project Presentation:** https://youtu.be/tbIulM9wC9E

## Project Description

The Progressive Load Workout Generator is a Python application that creates workout plans based on a user's fitness goals and experience level. It also allows users to record completed workouts, track workout history, and receive recommendations for gradually increasing exercise weight.

This project was developed for Project 2 using concepts from Python Crash Course, Chapters 8–11.

## Features

- Generate workouts based on strength, endurance, or general fitness.
- Choose beginner, intermediate, or advanced experience levels.
- Use classes, objects, inheritance, and methods to organize exercises.
- Record completed workouts and workout durations.
- Track total workouts and total exercise time.
- Save and load workout information using JSON files.
- Recommend gradual weight increases after successfully completing exercise targets.
- Handle invalid input and file errors.
- Run automated tests using pytest.

## Technologies Used

- Python 3
- Visual Studio Code
- GitHub
- GitHub Actions
- pytest
- JSON

## Project Structure

```text
Progressive_Load_Workout_Generator/
|
|-- main.py
|-- exercise.py
|-- workout.py
|-- workout_generator.py
|-- progress_tracker.py
|-- file_manager.py
|-- requirements.txt
|-- .gitignore
|
|-- data/
|   |-- workouts.json
|   |-- progress.json
|
|-- tests/
|   |-- test_exercise.py
|   |-- test_workout.py
|   |-- test_generator.py
|   |-- test_file_manager.py
|   |-- test_progress_tracker.py
|
|-- .github/
    |-- workflows/
        |-- tests.yml
```

## How to Run the Program

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Install the required dependency:

```bash
pip install -r requirements.txt
```

5. Start the application:

```bash
python main.py
```

## How to Run Automated Tests

Run the following command:

```bash
python -m pytest -v
```

The project uses pytest to verify that its classes, functions, workout generation, file management, and progress tracking work correctly.

GitHub Actions automatically runs the tests when changes are pushed to the repository.

## Learning Objectives

This project demonstrates:

- Functions and modular programming.
- Classes, objects, attributes, and methods.
- Inheritance and object-oriented programming.
- Reading and writing JSON files.
- Exception handling with try and except.
- Automated testing with pytest.
- Version control using GitHub.
- Continuous integration using GitHub Actions.

## Author

Andrew Hissong

Cybersecurity Major  
Columbus State Community College
