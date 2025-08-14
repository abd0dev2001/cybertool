def print_other_options():
    title = "OTHER OPTIONS"
    width = 43

    print(f"\n{'-' * 6} {title} {'-' * (width - len(title) - 7)}")

    print(f"| ($): Go Back{' ' * (width - len('($): Go Back') - 4)}|")
    print(f"| (!): Exit Tool{' ' * (width - len('(!): Exit Tool') - 4)}|\n")

    print("-" * width)