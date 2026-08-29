from difflib import get_close_matches

def add_cmd_ui() -> tuple | None:
    commands = {}
    cmd_counter = 0
    while True:
        command = input("Enter command or type 'wq' to go back: ")
        if command.lower() != "wq":
            cmd_counter += 1
            commands[cmd_counter] = command
        else:
            break
    if commands:
        file_name = input("please enter file name to save commands: ")
        return (file_name, commands)
    else:
        return None
    
def lookup_cmd_file(existing_files: dict) -> str | None:
    print("\n\n")
    print(f"{'File Name':<20}Created On")
    for existing_file_name in existing_files:
        print(f"{existing_file_name:<20}{existing_files[existing_file_name]['created_on']}")
    while True:
        print("\n")
        file_name = input("Enter file name or 'wq' to go back: ").lower()
        if file_name != 'wq':
            if file_name in existing_files:
                for index, cmd in enumerate(existing_files[file_name]["file_content"]):
                    print(f"{index +1}. {cmd}")
                return file_name
            file_name_suggestion = get_close_matches(file_name, list(existing_files.keys()), n=1)
            if file_name_suggestion:
                feedback = input(f"{file_name} not found, perhaps you mean {file_name_suggestion[0]}? y/n: ").lower()
                if feedback == 'y':
                    return file_name_suggestion[0]
            else:
                print("File not found, please try again")
            continue
        return None
                    
    
def command_ouput(cmd_result:list, selected_file: str) -> None:
    print("\n\n")
    print(f"Selected file: {selected_file}")
    print(f"Result: {cmd_result}")
