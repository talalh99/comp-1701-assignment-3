import module

def main()-> None:

    current_table = []
    print("Command options: read 'filename', save 'filename', or exit")
    command_prompt = input("Enter a command: ").lower()

    if 'read' in command_prompt:
        module.current_table = read_file()
    elif 'save' in command_prompt:
        module.save_to_file()
    elif command_prompt == 'exit':
        module.exit_program()
    elif command_prompt == 'count':
        module.count(current_table)
    elif command_prompt == 'column':
        module.print_columns(current_table)
    
    else:
        print("Command not recognized! Try again")

main()