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

