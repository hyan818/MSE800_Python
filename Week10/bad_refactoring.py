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

    count_statements(filename, lines, "for")
    count_statements(filename, lines, "while")
    count_statements(filename, lines, "if")


def count_statements(filename, lines, statement):
    """Count how many statements in the file."""
    num_for_loops = sum(bool(line.strip().startswith(statement)) for line in lines)
    print(f"Program {filename} contain {num_for_loops} {statement} loops")
