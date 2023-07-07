import os
import json
import re

def escape_tags(filename):
    # Read the contents of the input file
    with open(filename, 'r') as file:
        content = file.read()

    # Escape tags that start with '<' and end with '>'
    escaped_content = re.sub(r'<([^>]+)>', r'&lt;\1&gt;', content)

    # Write the modified contents back to the file
    with open(filename, 'w') as file:
        file.write(escaped_content)

# Get the current directory
directory = './tensorflow'

# List to store filenames
filenames = []

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.md') and os.path.isfile(os.path.join(directory, filename)):
        # Escape tags in each .md file
        escape_tags(os.path.join(directory, filename))
        filenames.append(filename)

# Create a dictionary to store filenames
data = {'filenames': filenames}

# Write the dictionary to a JSON file
output_file = 'output1.json'
with open(output_file, 'w') as json_file:
    json.dump(data, json_file)
