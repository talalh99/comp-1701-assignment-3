import module

def main()-> None:

    current_table = []
    print("Command options: read 'filename', save 'filename', column, print_columns, sort_columns, distr_column, select_column_value, count, or exit")
    command_prompt = input("Enter a command: ").lower()

    if 'read' in command_prompt:
        module.read_file()
    elif 'save' in command_prompt:
        module.save_to_file()
    elif command_prompt == 'exit':
        module.exit_program()
    elif command_prompt == 'count':
        module.count(current_table)
    elif command_prompt == 'print_column':
        module.print_columns(current_table)
    elif command_prompt == 'sort_columns':
        module.sort_columns(current_table)
    elif command_prompt == 'distr_column':
        module.distr_column(current_table)
    elif command_prompt == 'select_column_value':
        module.select_column_value(current_table)
    else:
        print("Command not recognized! Try again")

main()