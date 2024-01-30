import pdb  # Python Debugger


def add(num1, num2):
    pdb.set_trace()  # Breakpoint
    return num1 + num2


print(add(12, "abc"))

# Note:
# pdb.set_trace() is a Python function that is part of the Python Debugger (PDB) module.
# It allows you to set a breakpoint in your Python code, which means that when the code execution
# reaches that point, it will pause, and you can interactively inspect the program's state,
# step through the code, and perform debugging operations.

# Here's how pdb.set_trace() works:
# 1) Import the PDB module: You need to import the pdb module at the beginning of your script or
# in the Python shell.

# 2) Set a breakpoint: Place pdb.set_trace() at the location in your code where you want to start
# debugging. Typically, you would place it where you suspect a problem or want to inspect the
# program's state.

# 3) Run your script: When you execute your Python script, it will run until it encounters
# # pdb.set_trace(). At this point, it will pause, and you'll be dropped into an interactive debugger session.
#
# 4) Use the debugger: Once you're in the debugger session, you can use various commands to inspect
# variables, step through code, and understand the program's behavior.

# 5) Exit the debugger: When you're done debugging, you can type 'q' and press Enter to exit the
# debugger and continue the program's execution.

# Some common debugger commands include:
# n (next): Execute the current line of code and move to the next line.
# c (continue): Continue executing the program until the next breakpoint.
# s (step): Step into the current function or method call.
# q (quit): Exit the debugger and terminate the program.
# p variable_name (print value): Prints the value of a variable.
# l (list): Display the code around the current position.
# h (help): Get help on available debugger commands.
