# **Task Timer Manager**
#### **Video Demo:** *https://youtu.be/TTFBuNM8XKk*
#### **Description:**
Task Timer Manager is a productivity-oriented Python application built using **CustomTkinter**. It allows users to create tasks with timers, track remaining time, and accumulate bonus time when tasks are completed early. This project was created as the final submission for **CS50x**, demonstrating GUI development, state management, and Python programming concepts.

---

## **Important Notice**
**This application must be run locally on your personal computer.**
It will **not** work in GitHub Codespaces or CS50’s online environment, because CustomTkinter and GUI applications cannot run inside those systems.

To use this project, you must download the files and execute them on your own device.

---

# **Overview**
Task Timer Manager is designed to improve personal organization and productivity. The application includes:

- A **Main Timer** that counts down the active task’s duration
- A **Bonus Timer** for extra time gained when tasks finish early
- A dark-themed, modern interface built with CustomTkinter
- Dynamic task creation inside a scrollable frame
- Visual cues for task states: active, completed, or idle

This project showcases the integration of GUI development within Python in a clean, structured format.

---

# **Motivation & Purpose**
The goal behind this project was to build a real, practical productivity tool while applying topics learned throughout CS50, including:

- Python module structure
- GUI development using CustomTkinter
- Event-driven programming
- Dynamic interface updates
- Managing application state
- User input handling

The “bonus time” mechanic adds a small gamification element that rewards efficiency.

---

# **How the Application Works**

## Creating a Task
Each new task contains:
- A name field
- A duration field (in minutes)
- A **Start** button
- A **✓ Complete** button
- An **X Remove** button

Tasks are displayed vertically in a scrollable list.

## Starting a Task
When the user clicks **Start**:
1. The Main Timer is set based on the entered duration
2. A countdown begins immediately
3. The task changes color (`#444422`) to indicate it’s active
4. The remaining time appears in the large top timer

## Completing a Task
- If time runs out, the task is automatically marked complete
- If completed manually before time ends:
  - Remaining time is added to the **Bonus Timer**
  - The task becomes green (`#224422`)

## Bonus Timer
The Bonus Timer:
- Accumulates leftover time
- Can be started or paused manually
- Displays its total time at the top of the application

---

# **Project Structure**
project/
│
├── project.py # Main GUI application
├── README.md # Documentation file
├── requirements.txt # Project dependencies
└── test_project.py # Test file required for CS50

# **Installation & Execution**

### 1. Install dependencies in requirements.txt

### 2. Run the application:
The graphical interface will open in a new window.

### Reminder:
> This project **will not run** in GitHub Codespaces.
> It must be executed on your own computer (Windows, macOS, or Linux).

---

# 🛠️ **Design Choices**

###  CustomTkinter
Chosen for its modern appearance, native dark mode, and cleaner widget styling compared to standard Tkinter.

### Modular Functions
Features such as task creation, timer updates, bonus logic, and UI changes are separated into functions to increase clarity and maintainability.

### Non-Blocking Event Loop
Using:
```python
app.after(1000, update_timers)
keeps the interface responsive while updating timers once per second.

### What I Learned
- Developing this project strengthened my understanding of:
- GUI development in Python
- Organizing code for readability and modularity
- Managing dynamic user input
- Handling multiple timers and states simultaneously
- Building real-world functionality instead of console-only programs

### Conclusion
- Task Timer Manager is a useful productivity tool combining time tracking and a simple reward system through bonus accumulation. It represents a practical application of programming skills learned during the CS50 course.
- Future improvements may include:
- Saving tasks and bonus history
- Sound notifications
- Data persistence with a database
- User statistics
- Improved task organization
