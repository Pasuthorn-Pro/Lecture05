def format_strings(*args):
    formatted_string = "".join(args)
    return formatted_string.upper()

result = format_strings("Concatenate", "these", "strings", "please")
print(result)