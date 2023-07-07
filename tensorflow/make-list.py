import os

def convert_lines_to_list_syntax(filename):
    # Read the contents of the input file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Convert each line into list item syntax
    list_lines = ['- ' + line.strip() for line in lines]

    # Write the modified contents back to the file
    with open(filename, 'w') as file:
        file.write('\n'.join(list_lines))

# Provide the current directory path
current_directory = '.'

# Iterate over all files in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith('.md') and filename != 'index.md':
        # Construct the file path
        file_path = os.path.join(current_directory, filename)
        
        # Convert each line in the file to list item syntax
        convert_lines_to_list_syntax(file_path)
