from calculator.parser import evaluate_expression


def start_cli() -> None:
    """Start a simple CLI for the calculator."""
    print("=== Simple Python Calculator ===")
    print("Enter expressions like: 3 + 4")
    print("Type 'quit' to exit.\n")

    while True:
        expr = input(">> ").strip()

        if expr.lower() == "quit":
            print("Goodbye!")
            break

        try:
            result = evaluate_expression(expr)
            print("= ", result)
        except Exception as e:
            print("Error:", e)