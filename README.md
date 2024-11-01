# Langton's Ant

## Program Description
Langton's Ant is a cellular automata. An ant is placed in the center of an infinite grid, facing up.

Every turn:
- If the cell it is on is white, the ant turns clockwise, flips the
color of the cell to dark, and moves forward one step.
- If the cell it is on is dark, the ant turns counter clockwise, flips the color
  of the cell to white, and moves forward one step.
  
For this program we will be implementing Langton's Ant with a terminal UI.

Since the terminal cannot display an infinite grid, we will show as much of the
process as we can and exit the program once the ant moves out of screen.

This program automatically runs all the steps, with enough delay so that each
step is visible to the human eye.

## Programming Conventions

### General
- The language shall be Python
- The operating system shall be Linux
- Write functional style python
- Only mutate state at program borders (terminal state)
- Use type hints
- Provide full implementations
- Use descriptive names for variables, functions and classes
- Keep in mind the guidelines from `Code That Fits In Your Head`

### Testing
- Cover all functions with tests
- When testing, do not use mocks if possible
- Use the Python library `unittest`
- Do _not_ use comments for _Arrange_, _Act_ and _Asserts_
- Measure test coverage

### Project Structure
- `src/` for the modules
- `test/` for the tests
- `main.py` to run the program
- `.gitignore` ignores anything not related to the program.
- `cover` is a bash script that runs the tests and outputs a coverage report in the terminal
- `requirements.txt` Python dependencies
- `.venv` virtual environment
