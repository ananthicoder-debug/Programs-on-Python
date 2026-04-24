def remove_duplicates(input_string):
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

def convert_case(new_string):
    return new_string.lower(), new_string.upper()

input_string = input("Enter a string: ")
unique_string = remove_duplicates(input_string)
lower_case, upper_case = convert_case(unique_string)

print("String with duplicates removed:", unique_string)
print("Lowercase:", lower_case)
print("Uppercase:", upper_case)
