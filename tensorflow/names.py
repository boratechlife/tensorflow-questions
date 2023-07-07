import os
import json

def read_filenames(directory):
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.md') and os.path.isfile(os.path.join(directory, filename)):
            filenames.append(os.path.splitext(filename)[0])
    return filenames

def write_to_json(filenames, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(filenames, json_file)

# Provide the directory path where the files are located
directory_path = '.'

# Provide the output file path for the JSON file
output_file_path = './output3.json'

# Read filenames from the directory
file_names = read_filenames(directory_path)

# Write filenames to JSON file
write_to_json(file_names, output_file_path)
