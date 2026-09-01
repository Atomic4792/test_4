from difflib import get_close_matches


def add_cmd_ui() -> tuple | None:
    commands = {}
    cmd_counter = 0
    print("""
PRINT [value]: prints the value
MOV [variable] [value]: assigns the value to the variable
ADD [variable] [value]: adds the value to the variable
SUB [variable] [value]: subtracts the value from the variable
MUL [variable] [value]: multiplies the variable by the value
[location]:: names a line of code, so it can be jumped to from elsewhere
JUMP [location]: jumps to the location specified
IF [condition] JUMP [location]: if the condition is true, jump to the location specified
END: finish execution\n""")
    while (
        command := input("Enter command or type 'wq' to go back: ").strip().lower()
    ) != "wq":
        cmd_counter += 1
        commands[cmd_counter] = command

    if commands:
        file_name = input("please enter file name to save commands: ")
        return (file_name, commands)
    else:
        return None


def lookup_cmd_file(existing_files: dict) -> str | None:
    print(f"\n\n{'File Name':<20}Created On")
    for name, file_data in existing_files.items():
        print(f"{name:<20}{file_data['created_on']}")

    while (
        file_name := input("\n\nEnter file name or 'wq' to go back: ").strip().lower()
    ) != "wq":
        if not file_name:
            continue

        if file_name not in existing_files:
            matches = get_close_matches(file_name, existing_files.keys(), n=1)
            if (
                not matches
                or input(
                    f"{file_name} not found, perhaps you mean {matches[0]}? (y/n): "
                ).lower()
                != "y"
            ):
                print("File not found, please try again.")
                continue
            file_name = matches[0]

        for index, cmd in enumerate(existing_files[file_name]["file_content"], start=1):
            print(f"{index}. {cmd}")
        return file_name

    return None


def command_ouput(cmd_result: list, selected_file: str) -> None:
    print("\n\n")
    print(f"Selected file: {selected_file}")
    print(f"Result: {cmd_result}")
