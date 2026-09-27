with open("input.txt", "r") as file:
    data = file.readlines()

print("Number of lines:", len(data))

first_two_lines = data[:2]

with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

print("First two lines written to output.txt")
