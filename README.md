🎓 School Management System & 🎮 Color Guessing Game

This repository contains two Python mini-projects:

    School Management System (SMS) – A console-based system for managing users (students and staff) and courses.

    Color Guessing Game – A simple interactive guessing game where the player must guess the correct color.

📁 Project 1: School Management System
📌 Features:

    Add Students and Staff with auto-generated IDs.

    Add Courses with descriptions and types.

    View all Users (Students or Staff) and Courses.

    Assign Courses to Students or Staff.

    Search Users by ID.

🧠 How it works:

    Uses Python random for ID generation.

    Data is stored in-memory using lists (list_of_User, list_of_courses).

    tabulate is used for pretty-printed tables in the terminal.

📦 Requirements:

    Python 3

    tabulate module (Install via pip install tabulate)

▶️ How to run:

python school_management_system.py

🎮 Project 2: Color Guessing Game
🎯 Objective:

Guess the correct color from a predefined list within 5 attempts.
🔄 Game Flow:

    A color is randomly selected.

    Player inputs guesses.

    Tracks wins, losses, and game count.

    Optional scoreboard display after a game.

🎨 Color Options:

    RED

    BLUE

    GREEN

    PINK

    YELLOW

    BLACK

▶️ How to run:

python color_game.py

📝 Note:

    Both scripts are currently combined in one file. For best practice, consider splitting them into two separate files:

        school_management_system.py

        color_guessing_game.py

🚀 Future Improvements:

    Add file/database storage for persistence.

    Add user authentication to the management system.

    Improve UI with a GUI framework (like Tkinter or PyQt).

    Add color hints and difficulty levels to the color game.
