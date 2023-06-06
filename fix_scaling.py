import os

directory = 'pgws'

# Iterate over each file in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the desired lines
    lines[0] = '1\n'
    lines[3] = '-1\n'

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
