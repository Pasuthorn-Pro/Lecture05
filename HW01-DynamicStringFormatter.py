def format_strings(*args):
    if len(args) == 1 and ' ' in args[0]:
        # Replace spaces with hyphens in a single argument with spaces
        formatted_string = args[0].replace(' ', '-')
    else:
        # Join all arguments with no additional formatting
        formatted_string = ''.join(args).upper()
    
    return formatted_string

if __name__ == '__main__':
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result)  # Output: "HELLOWORLDTHISISATEST"

    result = format_strings("Python", "is", "fun")
    print(result)  # Output: "PYTHONISFUN"

    result = format_strings("Hello world")
    print(result)  # Output: "HELLO-WORLD"
