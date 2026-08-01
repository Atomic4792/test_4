from string import ascii_uppercase
from utils import DataSource, TextDataSource,JsonDataSource

def conditional(operand_1: int, operator: str, operand_2: int) -> bool:
    if "==" in operator:
        return operand_1 == operand_2
    elif ">=" in operator:
        return operand_1 >= operand_2
    elif "<=" in operator:
        return operand_1 <= operand_2
    elif "!=" in operator:
        return operand_1 != operand_2
    elif ">" in operator:
        return operand_1 > operand_2
    else:
        return operand_1 < operand_2

def value(x: int, data: dict) -> int:
    if x in data:
        return data[x]
    return int(x)

def run(raw_data: DataSource) -> list:
    commands = raw_data.parse_file()
    print_list = []
    characters = ascii_uppercase
    data = {i: 0 for i in ascii_uppercase}
    row = 0
    while True:
        if row == len(commands):
            break
        parts = commands[row].split(" ")
        if parts[0] =="MOV":
            data[parts[1]] = value(parts[2], data)
        elif parts[0] =="ADD":
            data[parts[1]] += value(parts[2], data)
        elif parts[0] =="MUL":
            data[parts[1]] *= value(parts[2], data)
        elif parts[0] =="SUB":
            data[parts[1]] -= value(parts[2], data)
        elif parts[0] =="PRINT":
            print_list.append(value(parts[1], data))
        elif parts[0] == "JUMP":
            row = commands.index(f"{parts[1]}:")
        elif "IF" in parts:
            if conditional(value(parts[1], data), parts[2], value(parts[3], data)):
                row = commands.index(f"{parts[5]}:")
        if "END" in parts:
            break
        row += 1
    return print_list

if __name__ == "__main__":
    raw_data = JsonDataSource("data.json")
    print(run(raw_data))