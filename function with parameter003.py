def print_all(*args):
    for index, args in enumerate(args):
        print(f"Argument {index + 1}: {args}")

#Example
print_all("python", 3.8, True, [1,2,3], {"key": "value"})