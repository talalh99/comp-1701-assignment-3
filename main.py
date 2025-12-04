print("Command options: read 'filename', save 'filename', or exit")
comand_prompt = input("Enter a command: ").lower()

if 'read' in command_prompt:
    read_file()
elif 'save' in command_prompt:
    save_to_file()
elif command_prompt == 'exit':
    exit_program()
else:
    print("Command not recognized! Try again")