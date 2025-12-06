def read_file():
    """Read and display the contents of a file specified by the user."""
    filename = input("Enter the filename: ")
    
    try:
        with open(filename, 'r') as file:
            file_content = file.read()
            print(file_content)
    except FileNotFoundError:
        print(f"Error: File {filename} was not found!")
    except Exception as e:
        print(f"There was an error reading the file. Please try again!")

## count() prints the amount of rows in the current table
def count(table:list) -> str:
    num_of_rows = str(len(table)-1) + " rows in the table."
    return num_of_rows

## print_columns() prints the names of each column within the current table
def print_columns(table:list):
    names = ''
    print("Columns\n-------")
    if table == []:
        names = 'No data found.'
        return names
    i = 0
    while i < len(table[0]):
        print(table[0][i])
        i+=1
    print("-------")

# To use the function:
# read_file()

def save_to_file():
    """Read a file, append new text, and save it."""
    filename = input("Enter the filename: ")
    
    try:
        with open(filename, 'r') as file:
            file_content = file.read()
            print(file_content)
            
            new_text = input("Enter the new text to enter: ")
            updated_content = file_content + "\n" + new_text
            
        with open(filename, 'w') as file:
            file.write(updated_content)
            print("File has been updated and saved!")
    except Exception as e:
        print(f"There was an error saving file: {filename}")

# To use the function:
# save_to_file()
        
def exit_program():
    """Exit the program gracefully."""
    print("Exiting program... ")
    exit()
    print("Program has exited!")  # This line will never execute