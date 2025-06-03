# Task List Manager in Python

A command-line tool to manage a list of tasks. Users can show the list, add new tasks, remove tasks, and clear the entire list. Tasks are managed in memory and are not saved between sessions in this version.

## How to Run
1. Ensure you have Python installed.
2. Download `task list manager.py`.
3. Run the program from the terminal using the command: `python "task list manager.py"`
4. Select options from the menu to manage your tasks.

## What I Learned / Concepts Demonstrated
* Using global lists (`task_list`) to store data.
* Defining functions for each action (`show_list`, `add_list`, `remove_list`, `clear_list`, `ask_continue`) to make the code modular.
* Menu-driven interaction based on user input.
* `while` loop for the program's main flow.
* `if/elif/else` statements to execute chosen actions.
* Basic list operations like `append()`, `remove()`, and `clear()`.
* Checking if an element exists in a list (`if task in task_list`).

## Possible Issues / Learnings
* In the `clear_list()` function: `if input(...) == "yes" or "y":` the condition `or "y"` will always evaluate to true because the string "y" itself is truthy. This should be rewritten as `answer = input(...).lower()` followed by `if answer == "yes" or answer == "y":` for correct functionality.

## Future Improvements
* Implement file handling to save the task list to a file so it is persistent.
* Add the ability to mark tasks as completed instead of just removing them.
* Add functionality to edit existing tasks.
