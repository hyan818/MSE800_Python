"""
Make this a function:
Input values: num_for_loops, lines, filename
Output value: num_while_loops
(NB: "Output" doesn't mean "stuff we print")
"""


def main():
    """
    Main function. Read file. Count required attributes
    :return:
    """

    filename = input("Enter program filename: ")
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    count_for_statements(filename, lines)
    count_while_statements(filename, lines)
    count_if_statements(filename, lines)


def count_for_statements(filename, lines):
    """Count how many for statements in the file."""
    num_for_loops = 0

    for line in lines:
        if line.strip().startswith("for"):
            num_for_loops += 1

    print(f"Program {filename} contain {num_for_loops} for loops")


def count_while_statements(filename, lines):
    """Count how many while statements in the file."""
    num_while_loops = 0
    for line in lines:
        if line.strip().startswith("while"):
            num_while_loops += 1

    print(f"Program {filename} contain {num_while_loops} for loops")


def count_if_statements(filename, lines):
    """Count how many if statements in the file."""
    num_if_loops = 0
    for line in lines:
        if line.strip().startswith("if"):
            num_if_loops += 1

    print(f"Program {filename} contain {num_if_loops} for loops")
