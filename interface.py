from difflib import get_close_matches
from string import ascii_uppercase


def suggest_correction(word: str, valid_list: list, error_msg: str) -> str | None:
    """Helper function to handle validation, suggestions, and user prompts."""
    matches = get_close_matches(word, valid_list, n=1)
    if matches:
        prompt = (
            input(f"{error_msg}, perhaps you mean {matches[0]}? y/n: ").strip().lower()
        )
        if prompt == "y":
            return matches[0]
    print(f"{error_msg}. Please try again.")
    return None


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

    valid_cmds = ["PRINT", "MOV", "ADD", "SUB", "MUL", "JUMP", "IF"]
    valid_variables = list(ascii_uppercase)
    valid_locations = []

    while (
        user_input := input("Enter command or type 'wq' to go back: ").strip()
    ) not in ("wq", "WQ", "wQ", "Wq"):


        if " " not in user_input:
            if ":" not in user_input and user_input.upper()!= "END":
                print("Invalid command, please try again")
            elif user_input in valid_locations:
                print(f"{user_input} is already defined, please try again")
            else:
                cmd_counter += 1
                valid_locations.append(user_input)
                commands[cmd_counter] = user_input
            continue


        parsed_input = user_input.split()
        if len(parsed_input) not in (2, 3, 6):
            print("Invalid command structure, please try again")
            continue


        cmd = parsed_input[0]
        if cmd not in valid_cmds:
            cmd = suggest_correction(cmd.upper(), valid_cmds, "Command not valid")
            if not cmd:
                continue
            parsed_input[0] = cmd

        if len(parsed_input) == 3 and parsed_input[0] in ("MOV", "ADD", "MUL", "SUB"):
            if parsed_input[1] not in valid_variables:
                var = suggest_correction(
                    parsed_input[1].upper(), valid_variables, f"{parsed_input[1]} is not valid"
                )
                if not var:
                    continue
                parsed_input[1] = var

            if (
                not parsed_input[2].isnumeric()
                and parsed_input[2] not in valid_variables
            ):
                val = suggest_correction(
                    parsed_input[2].upper(),
                    valid_variables,
                    f"{parsed_input[2]} is not a valid argument",
                )
                if not val:
                    continue
                parsed_input[2] = val

        
        elif len(parsed_input) == 2:
            if parsed_input[0] == "JUMP":
                if parsed_input[1].isnumeric():
                    print(
                        f"{parsed_input[1]} is not a valid location. Please try again"
                    )
                    continue
            elif parsed_input[0] == "PRINT":
                if (
                    not parsed_input[1].isnumeric()
                    and parsed_input[1] not in valid_variables
                ):
                    var = suggest_correction(
                        parsed_input[1].upper(),
                        valid_variables,
                        f"{parsed_input[1]} is not a valid variable",
                    )
                    if not var:
                        continue
                    parsed_input[1] = var

        
        elif len(parsed_input) == 6 and parsed_input[0] == "IF":
            if parsed_input[4] != "JUMP":
                if suggested_arg := suggest_correction(parsed_input[4].upper(), valid_cmds, f"{parsed_input[4]} is not a valid argument"):
                    parsed_input[4] = suggested_arg
                else:
                    continue
            valid_operands = True
            for i in (1, 3):
                if (
                    not parsed_input[i].isnumeric()
                    and parsed_input[i] not in valid_variables
                ):
                    var = suggest_correction(
                        parsed_input[i].upper(),
                        valid_variables,
                        f"{parsed_input[i]} is not a valid operand",
                    )
                    if not var:
                        valid_operands = False
                        break
                    parsed_input[i] = var

            if not valid_operands:
                continue
            if ":" in parsed_input[5]:
                if suggested_location := suggest_correction(parsed_input[5], valid_locations, f"{parsed_input[5]} is not a valid location"):
                    parsed_input[5] = suggested_location[:-1]

                else:
                    continue

    
        cmd_counter += 1
        command = " ".join(parsed_input)
        print(command)
        commands[cmd_counter] = command

    if commands:
        file_name = input("Please enter file name to save commands: ")
        return (file_name, commands)

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
