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
    for index, existing_file_name in enumerate(list(existing_files.keys())):
        print(f"{index +1}. {existing_file_name}")
    while True:
        print("\n\n")
        file_name = input("Enter file name or 'wq' to go back: ").lower()
        if file_name != 'wq':
            if file_name in existing_files:
                for index, cmd in enumerate(existing_files[file_name]):
                    print(f"{index +1}. {cmd}")
                return file_name
            continue
        return None
                    
    
def command_ouput(cmd_result:list, selected_file: str) -> None:
def command_ouput(cmd_result:list, selected_file: str) -> None:
    print("\n\n")
    print(f"Selected file: {selected_file}")
    print(f"Result: {cmd_result}")
