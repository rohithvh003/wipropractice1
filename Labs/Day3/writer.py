# Day3 Q2. Create a small Python package with:
# 1. A module containing a function write_numbers_to_file(filename)
# 2. The function should write numbers 1–100 into a file
# 3. Handle possible exceptions such as:
# File not found
# Permission denied

def write_numbers_to_file(filename):
    try:
        with open(filename, "w") as file:
            for i in range(1, 101):
                file.write(f"{i}\n")

        print("Numbers written successfully.")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")


# function call
write_numbers_to_file("F1.txt")

