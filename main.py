print("Command options: read filename, save filename, or exit")
comand_prompt = input("Enter a command: ").lower()

if comand_prompt == 'read filename':
    filename = input("Enter the filename: ")
    
    try:
        with open(filename, 'r') as file:
            file_content = file.read()
            print(file_content)
    except FileNotFoundError:
        print(f"Error: File {filename} was not found!")
    except Exception as e:
        print(f"There was an error reading the file. Please try again!")
        
elif comand_prompt == 'save filename':
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
        
elif comand_prompt == 'exit':
    print("Exiting program... ")
    exit()
    print("Program has exited!")
    
else:
    print("Command not recognized! Try again")