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

def sort_columns(table:list):
    if not table:
        print("No data in table to sort.")
        return table
    
    header = table[0]
    
    # Show column options
    print("Available columns:")
    for i, column in enumerate(header):
        print(f"{i}. {column}")
        
    # Get column index
    try:
        column_index = int(input("Enter the column index to sort by: "))
        if not 0 <= column_index < len(header):
            print("Invalid column index.")
            return table
    except ValueError:
        print("Column index must be a number.")
        return table   
    
    # Sort rows (excluding header)
    try:
        sorted_rows = sorted(table[1:], key=lambda r: r[column_index])
    except:
        print("Error while sorting. Column values may not be comparable.")
        return table

    print("\nTable successfully sorted!")
    return [header] + sorted_rows

def distr_column(table:list):
    """Create a new table listing unique values from a column and their counts."""
    if not table:
        print("No data in table.")
        return table
    
    header = table[0]

    # Show user the columns
    print("Available columns:")
    for i, column in enumerate(header):
        print(f"{i}. {column}")
        
    # Ask for column index
    try:
        column_index = int(input("Enter the column index to analyze: "))
        if not 0 <= column_index < len(header):
            print("Invalid column index.")
            return table
    except ValueError:
        print("Column index must be a number.")
        return table
    
    # Count occurrences
    counts = {}
    for row in table[1:]:
        value = row[column_index]
        counts[value] = counts.get(value, 0) + 1

    # Build new table with two columns: value, count
    new_table = [["value", "count"]]
    for value, total in counts.items():
        new_table.append([value, total])

    print("\nDistribution table created!")
    return new_table

def select_column_value(table: list):
    """Return a new table containing only rows where column == value."""
    if not table:
        print("No data in table to filter.")
        return table

    header = table[0]

    # Show available columns
    print("Available columns:")
    for i, column in enumerate(header):
        print(f"{i}. {column}")

    # Select column index
    try:
        column_index = int(input("Enter the column index: "))
        if not 0 <= column_index < len(header):
            print("Invalid column index.")
            return table
    except ValueError:
        print("Column index must be a number.")
        return table

    # Select value to match
    value = input("Enter the value to filter by: ")

    # Build new filtered table
    new_table = [header]  # keep header
    for row in table[1:]:
        if row[column_index] == value:
            new_table.append(row)

    print("\nRows successfully filtered!")
    return new_table

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