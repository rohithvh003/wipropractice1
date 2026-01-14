# 4. Create another module that imports this function and reads the file content safely
from writer import write_numbers_to_file

def read_file_safely(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found while reading")
    except PermissionError:
        print("Permission denied while reading")
    except Exception as e:
        print("Unexpected error:", e)


# Example usage
filename = "F1.txt"

write_numbers_to_file(filename)   # write numbers to file
read_file_safely(filename)        # read numbers safely
