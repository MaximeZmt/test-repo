from calculator.operations import OPERATIONS


def evaluate_expression(expr: str) -> float:
    """Evaluate a simple expression like '3 + 5'."""
    tokens = expr.split()
    if len(tokens) != 3:
        raise ValueError("Invalid expression format. Use: number operator number")

    a_str, op, b_str = tokens

    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        raise ValueError("Both operands must be numbers")

    if op not in OPERATIONS:
        raise ValueError(f"Invalid operator: {op}")

    return OPERATIONS[op](a, b)
